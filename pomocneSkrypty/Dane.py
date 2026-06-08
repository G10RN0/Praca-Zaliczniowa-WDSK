import csv
import numpy as np
import os

#funckja generująca różne dane dla algorytmów FCFS i Round Robin
def generate_test_data_for_time(filename: str, num_processes: int, scenario: int):
    #Tworzymy pustą listę, do której będziemy wrzucać wygenerowane procesy
    generated_data = []
    
    #Generujemy dane dla różnych scenariuszy i dodajemy do listy
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

        #dodajemy wygenerowanę wartości do listy
        generated_data.append([arrival_time, execution_time])
        
    #Sortujemy listę rosnąco według czasu przybycia
    generated_data.sort(key=lambda x: x[0])

    #zapisujemy liste do pliku csv
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

#funkcja generują dane dla algorytmów zamiany stron
def generate_test_data_for_pages(filename: str, num_pages: int, num_lines: int):
    #tworzymy nowy plik tekstowy
    with open(filename, 'w') as file:
        #generujemy plik
        for _ in range(0, num_lines):
            #losujemy liczbe od 1 do maksymalnego numeru liczby stron pamięci
            side = str(np.random.randint(1, num_pages+1))+"\n"
            file.write(side) # zapisujemy do pliku

#funckja wczytująca dane dla algorytmów zaminy stron
def load_pages(filename: str) -> list:
    #tworzymy liste która przechwouje strony
    sides=[]
    #otwieramy plik
    with open(filename, 'r') as file:
        #wczytujemy dane i dodajmy do listy
        for line in file.readlines():
            sides.append(int(line.strip()))
            
    #zwracmy liste
    return sides           

if __name__ == "__main__":
    #jeśli wykonuje skrypt użytkownik to wczytuje Process w taki sposób
    from Proces import Process
    
    #sprawdzamy czy istnieje folder dane jak nie to go tworzymy 
    if not os.path.exists("dane"):
            os.mkdir("dane")
    #sprawdzamy czy istnieje folder czas w folderze dane jak nie to go tworzymy 
    if not os.path.exists("dane/czas"):
        os.mkdir("dane/czas")
    
    #sprawdzamy czy istnieje folder strony w folderze dane jak nie to go tworzymy 
    if not os.path.exists("dane/strony"):
        os.mkdir("dane/strony")
    
    #generacja danych
    for scenariusz in range(0, 4):
        #tworzmy folder dla danych scenariuszy
        os.makedirs(f"dane/czas/scenariusz[{scenariusz}]", exist_ok=True)
        for i in range(0, 100):
            generate_test_data_for_time(f"dane/czas/scenariusz[{scenariusz}]/dane_czas_scenariusz[{scenariusz}]_[{i}].csv", 100, scenariusz)
                
    #generujemy dane dla zamiany stron
    #ilość zamian na plik
    lines=[100, 150, 200, 250, 300]
    for i in range(len(lines)):
        #tworzmy folder dla danych scenariuszy
        os.makedirs(f"dane/strony/scenariusz[{i}]", exist_ok=True)
        for j in range (0, 100):
            generate_test_data_for_pages(f"dane/strony/scenariusz[{i}]/dane_strony[{j}].txt", 20, lines[i])
            
    print("Dane zostały wygenerowane")
else:
    #importujemy Process jesli skrypt jest wywołany przez inny skrypt
    from pomocneSkrypty.Proces import Process