import csv
import numpy as np
import os
from Proces import Process

def generate_test_data_to_file(filename: str, num_processes: int, scenario: int):
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
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["arrivalTime", "executionTime"]) # Nagłówek
        
        # Zapisujemy wszystkie posortowane rzędy
        writer.writerows(generated_data)
            
    print(f"Wygenerowano pomyślnie {num_processes} procesów do pliku '{filename}' (Scenariusz {scenario}).")

#wczytywanie procesów z pliku csv
def load_processes_from_file(filename: str) -> list:
    #lista z załodwanymi procesami
    loaded_processes = []
    
    #otwieramy plik
    with open(filename, mode='r') as file:
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

if __name__ == "__main__":
    choice = int(input("Wygeneruj dane dla(1/2):\n1.(planowanie czasu procesora)\n2.(zamiana stron)\n: "))
    
    if not os.path.exists("dane"):
            os.mkdir("dane")
            
    if choice == 1:
        for i in range(0, 100):
            generate_test_data_to_file(f"dane/dane_czas_scenariusz[0]_[{i}].csv", 100, 0)
    else:
        pass
        