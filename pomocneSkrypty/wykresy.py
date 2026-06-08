import matplotlib.pyplot as plt

#Konfiguracja stylu dla wszystkich wykresów
plt.style.use('seaborn-v0_8-whitegrid') #Czysty styl z siatką
plt.rcParams['font.size'] = 10 #ustawiamy wielkość czcionki
plt.rcParams['axes.titlesize'] = 12 #ustawiamy wielkość tytułu
plt.rcParams['axes.labelsize'] = 10 #ustawimy wielkość opisu

#funkcja które generuje wykresy dla algorytmów LRU i FIFO
def LruFifoGraph(frame_size: int, avg_fault: list[float], lines:list[int] , name_of_algorithm: str, path: str):
    
    #tworzymy nazwe dla wykresu
    name = f"wielkość ramki: {frame_size}, dla {name_of_algorithm}"
    
    #tworzymy obiekt wykresu
    fig, ax = plt.subplots(figsize=(8,5))
    
    #dodajemy wykres słupkowy o danych lines i avg_fault
    ax.barh(lines, avg_fault, height=10)
    
    #ustawiamy nazwe wykresu
    ax.set_title(name)
    
    #ustawiamy nazwe danych dla osi x i y
    ax.set_xlabel('ilość błędów')
    ax.set_ylabel('ilość ramek')
    
    # ustawiamy znaczniki osi y zgodnie z listą ramek
    ax.set_yticks(lines)

    # ustawiamy zakres osi x tak, aby był trochę szerszy niż maksymalna liczba błędów
    max_val = max(avg_fault)
    ax.set_xlim(0, max_val * 1.15)
    
    #zapisujemy wykres do pliku
    plt.tight_layout()
    plt.savefig(path, dpi=120)
    plt.close()

#funckja która tworzy wykresy dla FCFS i Round Robin
def FcfsRoundRobinGraph(scenariusz:int, avg_wait: dict, avg_turnaround: dict, Quanta: int, path: str):
    #opisy danych na wykresie
    labels = ["średnia czas czekania", "średni czas cyklu"]
    
    #wyądrebniamy dane z słownika dla algorytmów
    avg_wait_FCFS = avg_wait["FCFS"]
    avg_wait_RoundRobin = avg_wait["RR"]
    avg_turnaround_FCFS = avg_turnaround["FCFS"]
    avg_turnaround_RoundRobin = avg_turnaround["RR"]
    
    #tworzymy nowy obiekt wykresu z dwoma miejscami na wykresy
    figs, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    #wykres FCFS
    #tworzymy wykres słupkowy o opisach z labels, oraz danych avg_wait_FCFS, avg_turnaround_FCFS
    bars1=ax1.bar(labels, (avg_wait_FCFS, avg_turnaround_FCFS))
    #ustawiamy nazwe wykresu
    ax1.set_title(f"Scenariusz[{scenariusz}], algorytm FCFS")
    #dopasowujemy zakres osi y, żeby słupki nie dotykały górnej krawędzi wykresu
    ax1.set_ylim(0, max((avg_wait_FCFS, avg_turnaround_FCFS))*1.1)
    #dodajemy etykiety wartości nad słupkami
    ax1.bar_label(bars1, padding=3, fmt='%.2f') 
    
    #wykres Round Robin
    #tworzymy wykres słupkowy o opisach z labels, oraz danych avg_wait_RoundRobin, avg_turnaround_RoundRobin
    bars2=ax2.bar(labels, (avg_wait_RoundRobin, avg_turnaround_RoundRobin))
    #ustawiamy nazwe wykresu
    ax2.set_title(f"Scenariusz[{scenariusz}], algorytm Round Robin dla kwanty: {Quanta}")
    #dopasowujemy zakres osi y dla wykresu Round Robin
    ax2.set_ylim(0, max((avg_wait_RoundRobin, avg_turnaround_RoundRobin))*1.1)
    #dodajemy etykiety wartości nad słupkami Round Robin
    ax2.bar_label(bars2, padding=3, fmt='%.2f')
    
    #zapisujemy wykres
    plt.tight_layout()
    plt.savefig(path, dpi=120)
    plt.close()