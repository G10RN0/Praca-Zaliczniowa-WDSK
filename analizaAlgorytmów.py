from algorytmy.FIFO import FIFO
from algorytmy.LRU import LRU
from algorytmy.roundRobin import roundRobin
from algorytmy.FCFS import FCFS
from pomocneSkrypty.Dane import load_pages, load_processes_for_time
from pomocneSkrypty.wykresy import *
import os

#Przeprowadzmy eksperyment i analizujemy jego wyniki dla algorytmów FCFS i dla Round Robin
def analizuj_procesor():
    
    #sprawdzmy foldery istnieją jak nie to je tworzymy
    if not os.path.exists("wykresy"):
        os.mkdir("wykresy")
    if not os.path.exists("wykresy/czas"):
        os.mkdir("wykresy/czas")
    
    #specyfikacja danych dla eksperymentów
    num_scenariuszy = 4
    num_files = 100
    
    #Zmienne do trzymania sum wyników ze 100 plików dla Round Robin
    timeQuanta=[0.5, 3, 5]
    
    print("Rozpoczynam analizę algorytmów planowania czasu procesora...")
    
    # Główna pętla przechodząca przez 4 wygenerowane scenariusze (od 0 do 3)
    for scenariusz in range(num_scenariuszy):
        # Zmienne do trzymania sum wyników ze plików dla FCFS
        suma_fcfs_wait = 0
        suma_fcfs_turnaround = 0

        # Zmienne do trzymania sum wyników ze plików dla Round Robin
        suma_rr_wait = {q: 0.0 for q in timeQuanta}
        suma_rr_turnaround = {q: 0.0 for q in timeQuanta}
        
        #tworzymy foldery dla wykresów dla różnych scenariuszy
        os.makedirs(f"wykresy/czas/scenariusz[{scenariusz}]", exist_ok=True)
        
        #głowna pętla do analizy
        for i in range(num_files):
            #FCFS
            
            #wczytujemy plik i wykonujemy algorytm FCFS  
            wait, trunaround=FCFS(load_processes_for_time(f"dane/czas/scenariusz[{scenariusz}]/dane_czas_scenariusz[{scenariusz}]_[{i}].csv"))
            #dodajemy wartości do zmiennych
            suma_fcfs_wait += wait
            suma_fcfs_turnaround += trunaround
            
            #Round Robin
            for quanta in timeQuanta:
                #wczytujemy plik i wykonujemy algorytm Round Robin 
                wait, trunaround=roundRobin(load_processes_for_time(f"dane/czas/scenariusz[{scenariusz}]/dane_czas_scenariusz[{scenariusz}]_[{i}].csv"), quanta)
                
                #dodajemy wartości do zmiennych
                suma_rr_wait[quanta] += wait
                suma_rr_turnaround[quanta] += trunaround
        
        #średnia z plików dla danego scenariusza FCFS
        suma_fcfs_turnaround = suma_fcfs_turnaround / num_files
        suma_fcfs_wait = suma_fcfs_wait / num_files
        
        #średnia z plików dla danego scenariusza Round Robin
        for q in timeQuanta:
            suma_rr_wait[q] = suma_rr_wait[q]/num_files
            suma_rr_turnaround[q] = suma_rr_turnaround[q]/num_files
        
        #wypisywanie końcowych średnich dla danego scenariusza
        print("-"*25, f"Scenariusz [{scenariusz}]", "-"*25)
        print("\n[FCFS]")
        print(f"Średni czas oczekiwania: {suma_fcfs_wait}")
        print(f"Średni czas cyklu (Turnaround): {suma_fcfs_turnaround}")
        
        print("\n[Round Robin]")
        
        for q in timeQuanta:
            print(f"\n[Round-Robin | kwant = {q}]")
            print(f"Średni czas oczekiwania: {suma_rr_wait[q]}")
            print(f"Średni czas cyklu (Turnaround): {suma_rr_turnaround[q]}")
            
            #tworzymy nazwe pliku dla wykresu
            wykres_file=f"wykresy/czas/scenariusz[{scenariusz}]/wykres_FCFS_RR_quanta[{q}].png"
            
            #pakujemy dane w słownik dla funkcji do generacji wykresów
            wait_data={"FCFS": suma_fcfs_wait, "RR": suma_rr_wait[q]}
            trunaround_data={"FCFS": suma_fcfs_turnaround, "RR": suma_rr_turnaround[q]}
            
            #tworzenie wkresów dla algorytmów
            FcfsRoundRobinGraph(scenariusz, wait_data, trunaround_data, q, wykres_file)

#Przeprowadzmy eksperyment i analizujemy jego wyniki dla algorytmów FIFO i LRU
def analiza_stron():
    
    #sprawdzmy foldery istnieją jak nie to je tworzymy
    if not os.path.exists("wykresy"):
        os.mkdir("wykresy")
    if not os.path.exists("wykresy/strony"):
        os.mkdir("wykresy/strony")
    
    #specyfikacje dla eksperymentu
    scenariusz_num=5
    files_num=100
    
    #wielkości ramek
    frame_sizes=[3, 5, 7]
    
    #słowniki które przechowują wszytkie dane, w zależności od wielkości ramki
    faults_fifo = {3: [], 5: [], 7: []}
    faults_lru = {3: [], 5: [], 7: []}
    history_lines = {3: [], 5: [], 7: []}
    
    #Główna pętla przechodząca przez 5 wygenerowanych scenariuszy (od 0 do 4)
    for scenariusz in range(scenariusz_num):

        print("-"*25, f"Scenariusz [{scenariusz}]", "-"*25)

        #iterujemy po każdej wielkości ramki
        for frame_size in frame_sizes:
            
            #zmienne przechowują średnie z jednej porcji danych
            avg_faults_fifo=0
            avg_faults_lru=0
            
            #ilość zmian stron na caly plik
            lines = 0
            for i in range(files_num):
                #wczytujemy plik z danymi dla danego przypadku
                data = load_pages(f"dane/strony/scenariusz[{scenariusz}]/dane_strony[{i}].txt")
                
                #ilość zmian
                lines=len(data)
                
                #wykonujemy algorytmy dla zaladowanych danych
                page_faults_fifo=FIFO(data, frame_size)
                page_faults_lru=LRU(data, frame_size)
                
                #dodajemy wartości by pozniej móc z nich obliczyć średnie
                avg_faults_fifo+=page_faults_fifo
                avg_faults_lru+=page_faults_lru
            
            #obliczamy średnie dla wartości błędów w algorytmach
            avg_faults_fifo = avg_faults_fifo/files_num
            avg_faults_lru = avg_faults_lru/files_num
            
            #wypisujemy infomacje analizy ekspermynetów
            print(f"Wielkość ramki: {frame_size}")
            
            print("[FIFO]")
            print(f"średnia błędów: {avg_faults_fifo}")
            print(f"ilość linijek: {lines}\n")
            
            print("[LRU]")
            print(f"średnia błędów: {avg_faults_lru}")
            print(f"ilość linijek: {lines}\n")
            
            #dodajmy nasze średnie do słowników które przechwoują średnia dla różnych ramek
            faults_fifo[frame_size].append(avg_faults_fifo)
            faults_lru[frame_size].append(avg_faults_lru)
            history_lines[frame_size].append(lines)
    
    #tworzymy wykresy dla przechowywanych danych
    for frame_size in frame_sizes:
        LruFifoGraph(frame_size, faults_fifo[frame_size], history_lines[frame_size], "FIFO", f"wykresy/strony/wykres_FIFO_ramka[{frame_size}].png")
        LruFifoGraph(frame_size, faults_lru[frame_size], history_lines[frame_size], "LRU", f"wykresy/strony/wykres_LRU_ramka[{frame_size}].png")

if __name__ == "__main__":
    analizuj_procesor()
    analiza_stron()