from pomocneSkrypty.Dane import load_pages

#funkcja wykonująca algorymt FIFO
def FIFO(pages: list[int], R: int) -> int:
    frames = []
    page_faults = 0
    
    #iterujmy przez wszystkie strony w danych
    for page in pages:
        #sprawdzamy czy strony nie ma obecnie w pamięci
        if page not in frames:
            #zwieszenie licznika błędów
            page_faults += 1
            
            #jeśli pamięć jest pełna wyzucamy z ramki pierwszy element by zrobic dla nie miejsce
            if len(frames) >= R:
                frames.pop(0)
            
            #dodajemy strone do ramki
            frames.append(page)
    
    #zwracmy licznik błędów
    return page_faults