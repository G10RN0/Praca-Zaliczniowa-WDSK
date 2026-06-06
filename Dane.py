import csv
import numpy as np
import os
from Proces import Process

def generate_test_data_for_time(filename: str, num_processes: int, scenario: int):
    # 1. Tworzymy pustą listę, do której będziemy wrzucać wygenerowane procesy
    generated_data = []
    
    # 2. Generujemy dane i dodajemy do listy (zamiast od razu do pliku)
    for _ in range(num_processes):
        if scenario == 1:
            arrival_time = np.random.randint(0, 101)
            execution_time = 5
            
        elif scenario == 2:
            arrival_time = 0
            execution_time = np.random.randint(1, 11)
            
        elif scenario == 3:
            arrival_time = max(0, int(np.random.normal(loc=20, scale=5)))
            execution_time = max(1, int(np.random.normal(loc=10, scale=2)))
            
        else:
            arrival_time = np.random.randint(0, 50)
            execution_time = np.random.randint(1, 20)

        # Dodajemy jako małą listę [czas_przybycia, czas_wykonania]
        generated_data.append([arrival_time, execution_time])
        
    # 3. Sortujemy listę rosnąco według czasu przybycia (indeks 0 to arrival_time)
    generated_data.sort(key=lambda x: x[0])

    # 4. Zapisujemy już POSORTOWANE dane do pliku CSV
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["arrivalTime", "executionTime"]) # Nagłówek
        
        # Zapisujemy wszystkie posortowane rzędy
        writer.writerows(generated_data)


#wczytywanie procesów z pliku csv
def load_processes_for_time(filename: str) -> list:
    #lista z załodwanymi procesami
    loaded_processes = []
    
    #otwieramy plik
    with open(filename, 'r') as file:
        #czytamy plik csv
        reader = csv.DictReader(file)
        
        #czytamy linie z pliku
        for row in reader:
            # Tworzymy nowe obiekty Process na podstawie danych z pliku
            arr_time = int(row["arrivalTime"])
            exe_time = int(row["executionTime"])
            #zapisujemy do listy
            loaded_processes.append(Process(arr_time, exe_time))
    
    #zwracamy liste
    return loaded_processes

def generate_test_data_for_pages(filename: str, num_pages: int, num_lines: int):
    with open(filename, 'w') as file:
        for _ in range(0, num_lines):
            side = str(np.random.randint(1, num_pages+1))+"\n"
            file.write(side)

def load_pages(filename: str) -> list:
    sides=[]
    with open(filename, 'r') as file:
        for line in file.readlines():
            sides.append(int(line.strip()))
    return sides           

if __name__ == "__main__":
    choice = int(input("Wygeneruj dane dla(1/2):\n1.(planowanie czasu procesora)\n2.(zamiana stron)\n: "))
    
    if not os.path.exists("dane"):
            os.mkdir("dane")
            
    if choice == 1:
        if not os.path.exists("dane/czas"):
            os.mkdir("dane/czas")
        for scenariusz in range(0, 4):
            os.makedirs(f"dane/czas/scenariusz[{scenariusz}]", exist_ok=True)
            for i in range(0, 100):
                generate_test_data_for_time(f"dane/czas/scenariusz[{scenariusz}]/dane_czas_scenariusz[{scenariusz}]_[{i}].csv", 100, scenariusz)
    else:
        if not os.path.exists("dane/strony"):
            os.mkdir("dane/strony")
        for i in range (0, 100):
            generate_test_data_for_pages(f"dane/strony/dane_strony[{i}].txt", 20, 100)
        