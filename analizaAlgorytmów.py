from algorytmy.FIFO import FIFO
from algorytmy.LRU import LRU
from algorytmy.roundRobin import roundRobin
from algorytmy.FCFS import FCFS
from pomocneSkrypty.Dane import load_pages, load_processes_for_time


def analizuj_procesor():
    liczba_scenariuszy = 4
    liczba_plikow = 100
    
    #Zmienne do trzymania sum wyników ze 100 plików dla Round Robin
    timeQuanta=[0.5, 3, 5]
        
    suma_rr_wait = {q: 0.0 for q in timeQuanta}
    suma_rr_turnaround = {q: 0.0 for q in timeQuanta}
    
    print("Rozpoczynam analizę algorytmów planowania czasu procesora...")
    
    # Główna pętla przechodząca przez 4 wygenerowane scenariusze (od 0 do 3)
    for scenariusz in range(liczba_scenariuszy):
        # Zmienne do trzymania sum wyników ze 100 plików dla FCFS
        suma_fcfs_wait = 0
        suma_fcfs_turnaround = 0
        
        #głowna pętla do analizy
        for i in range(liczba_plikow):
            #FCFS
            
            #wczytujemy plik            
            wait, trunaround=FCFS(load_processes_for_time(f"dane/czas/scenariusz[{scenariusz}]/dane_czas_scenariusz[{scenariusz}]_[{i}].csv"))
            suma_fcfs_wait += wait
            suma_fcfs_turnaround += trunaround
            
            #Round Robin
            for quanta in timeQuanta:
                wait, trunaround=roundRobin(load_processes_for_time(f"dane/czas/scenariusz[{scenariusz}]/dane_czas_scenariusz[{scenariusz}]_[{i}].csv"), quanta)
                suma_rr_wait[quanta] += wait
                suma_rr_turnaround[quanta] += trunaround
        
        #średnia z 100 plików dla danego scenariusza FCFS
        suma_fcfs_turnaround = suma_fcfs_turnaround / liczba_plikow
        suma_fcfs_wait = suma_fcfs_wait / liczba_plikow
        
        #średnia z 100 plików dla danego scenariusza Round Robin
        for q in timeQuanta:
            suma_rr_wait[q] = suma_rr_wait[q]/liczba_plikow
            suma_rr_turnaround[q] = suma_rr_wait[q]/liczba_plikow
        
        # Obliczanie i wypisywanie końcowych średnich dla danego scenariusza
        print(f"\nScenariusz [{scenariusz}]")
        print("\n[FCFS]")
        print(f"Średni czas oczekiwania:       {suma_fcfs_wait}")
        print(f"Średni czas cyklu (Turnaround): {suma_fcfs_turnaround}")
        
        for q in timeQuanta:
            print(f"\n[Round-Robin | kwant = {q}]")
            print(f"Średni czas oczekiwania:       {suma_rr_wait[q]}")
            print(f"Średni czas cyklu (Turnaround): {suma_rr_turnaround[q]}")

            
            
            
def analiza_stron():
    pass

if __name__ == "__main__":
    analizuj_procesor()