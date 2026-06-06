from Proces import Process
from Dane import load_processes_for_time

#algorytm FCFS
def FCFS(input_processes: list[Process]):
    
    #globalny czas symulacji
    time=0
    
    #średnie
    avg_waitingTime=0
    avg_turnAroundTime=0
    
    for process in input_processes:
        #jeśli nie ma procesów przetwarzanych to przewijamy od kolejnego procesu
        if time < process.arrivalTime:
            time = process.arrivalTime

        #zapisujemy metryki
        process.startTime = time # zapisujemy kiedy proces się zaczął
        process.completionTime = time + process.executionTime # kiedy proces się zakończy
        process.turnAroundTime = process.completionTime - process.arrivalTime  #jak długo trwał
        process.waitingTime = process.startTime - process.arrivalTime #jak długo czekał na wykonanie
        
        #aktualizujemy zegar
        time = process.completionTime
        
        #zapisujemy do średniej
        avg_waitingTime += process.waitingTime
        avg_turnAroundTime += process.turnAroundTime
    
    #obliczamy średnią
    avg_turnAroundTime = avg_turnAroundTime/len(input_processes)
    avg_waitingTime = avg_waitingTime/len(input_processes)
    print(f"średnia czekania procesu: {avg_waitingTime}, średnia czas cyklu przetwarzania: {avg_turnAroundTime}")
    
    #zwracamy średnie
    return avg_waitingTime, avg_turnAroundTime
    
if __name__ == "__main__":
    print(f"Algorytm FCFS:")
    FCFS(load_processes_for_time("dane\\dane_czas_scenariusz[0]_[0].csv"))
        