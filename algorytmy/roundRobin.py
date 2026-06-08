from pomocneSkrypty.Dane import load_processes_for_time
from pomocneSkrypty.Proces import Process


def roundRobin(processes: list[Process], timeQuanta: float):
    
    #tworzymy kopie listy
    unprocessed = processes.copy()
    #sortujemy listę
    unprocessed.sort(key=lambda x: x.arrivalTime)
    
    #procesy które zostały zakończone
    complited_process = []
    #procesy które są w trakcie trwania
    queued = []
    
    #globalny czas symulacji
    time=0
    
    #pętla bedzie aktywna do póki obie listy nie będą puste
    while unprocessed or queued:
        
        #jęsli lista unprocessed nie jest pusta i pierwszy proces ma arrivalTime mniejszy od obecnego czasu 
        #przenosimy go do listy
        while unprocessed and unprocessed[0].arrivalTime <= time:
            queued.append(unprocessed.pop(0))
            
        #Jeśli nikt nie czeka, ale w przyszłości pojawią się procesy to przewijamy czas do tego procesu
        if not queued and unprocessed:
            time = unprocessed[0].arrivalTime
            continue # Wracamy na początek pętli
            
        #Pobieramy pierwszy proces z kolejki gotowych do przetworzenia
        current = queued.pop(0)
        
        #Zapisujemy start tylko za pierwszym razem
        if current.startTime == -1:
            current.startTime = time
            
        #Obliczamy, ile czasu proces faktycznie zajmie procesorowi
        time_spent = min(current.remainingTime, timeQuanta)
        
        #odejmujemy czas spędzony w procesie
        current.remainingTime -= time_spent
        time += time_spent # Aktualizujemy zegar TYLKO o czas faktycznie spędzony
        
        #Zanim wrzucimy proces z powrotem, sprawdzamy czy w trakcie
        #jego działania nie przybyły do systemu jakieś nowe procesy!
        while unprocessed and unprocessed[0].arrivalTime <= time:
            queued.append(unprocessed.pop(0))
            
        #Sprawdzamy, czy proces się zakończył.
        #Jeśli tak to aktualizujemy metryki
        if current.remainingTime == 0:
            current.completionTime = time
            current.turnAroundTime = current.completionTime - current.arrivalTime
            current.waitingTime = current.turnAroundTime - current.executionTime
            complited_process.append(current) # Zapisujemy skończony proces
        else:
            queued.append(current)
    
    #obliczmy średnią dla wszystkich zakończnych procesów
    avg_turnAroundTime = sum(process.turnAroundTime for process in complited_process) / len(complited_process)
    avg_waitingTime = sum(process.waitingTime for process in complited_process) / len(complited_process)
        
    #zwracamy średnie
    return avg_waitingTime, avg_turnAroundTime