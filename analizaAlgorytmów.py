from algorytmy.FIFO import FIFO
from algorytmy.LRU import LRU
from algorytmy.roundRobin import roundRobin
from algorytmy.FCFS import FCFS
from pomocneSkrypty.Dane import load_pages, load_processes_for_time


def analizuj_procesor():
    num_scenariuszy = 4
    num_files = 100
    
    #Zmienne do trzymania sum wyników ze 100 plików dla Round Robin
    timeQuanta=[0.5, 3, 5]
        
    suma_rr_wait = {q: 0.0 for q in timeQuanta}
    suma_rr_turnaround = {q: 0.0 for q in timeQuanta}
    
    print("Rozpoczynam analizę algorytmów planowania czasu procesora...")
    
    # Główna pętla przechodząca przez 4 wygenerowane scenariusze (od 0 do 3)
    for scenariusz in range(num_scenariuszy):
        # Zmienne do trzymania sum wyników ze 100 plików dla FCFS
        suma_fcfs_wait = 0
        suma_fcfs_turnaround = 0
        
        #głowna pętla do analizy
        for i in range(num_files):
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
        suma_fcfs_turnaround = suma_fcfs_turnaround / num_files
        suma_fcfs_wait = suma_fcfs_wait / num_files
        
        #średnia z 100 plików dla danego scenariusza Round Robin
        for q in timeQuanta:
            suma_rr_wait[q] = suma_rr_wait[q]/num_files
            suma_rr_turnaround[q] = suma_rr_wait[q]/num_files
        
        # Obliczanie i wypisywanie końcowych średnich dla danego scenariusza
        print("-"*25, f"Scenariusz [{scenariusz}]", "-"*25)
        print("\n[FCFS]")
        print(f"Średni czas oczekiwania: {suma_fcfs_wait}")
        print(f"Średni czas cyklu (Turnaround): {suma_fcfs_turnaround}")
        
        print("\n[Round Robin]")
        
        for q in timeQuanta:
            print(f"\n[Round-Robin | kwant = {q}]")
            print(f"Średni czas oczekiwania: {suma_rr_wait[q]}")
            print(f"Średni czas cyklu (Turnaround): {suma_rr_turnaround[q]}")

def analiza_stron():
    scenariusz_num=5
    files_num=100
    
    frame_sizes=[3, 5, 7]
    
    avg_faults_fifo=0
    avg_faults_lru=0
    
    for scenariusz in range(scenariusz_num):

        print("-"*25, f"Scenariusz [{scenariusz}]", "-"*25)
        
        for frame_size in frame_sizes:
            lines = 0
            for i in range(files_num):
                data = load_pages(f"dane/strony/scenariusz[{scenariusz}]/dane_strony[{i}].txt")
                lines=len(data)
                page_faults_fifo=FIFO(data, frame_size)
                page_faults_lru=LRU(data, frame_size)

                avg_faults_fifo+=page_faults_fifo
                avg_faults_lru+=page_faults_lru
            
            avg_faults_fifo = avg_faults_fifo/lines
            avg_faults_lru = avg_faults_lru/lines
            print(f"Wielkość ramki: {frame_size}")
            
            print("[FIFO]")
            print(f"średnia błędów: {avg_faults_fifo}")
            print(f"ilość linijek: {lines}\n")
            
            print("[LRU]")
            print(f"średnia błędów: {avg_faults_lru}")
            print(f"ilość linijek: {lines}\n")
            
if __name__ == "__main__":
    analizuj_procesor()
    analiza_stron()