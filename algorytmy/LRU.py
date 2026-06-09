def LRU(pages: list[int], R: int) -> int:
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
        
        #jeśli jest w ramce to przeucamy je na koniec ramki
        else:
            frames.remove(page)
            frames.append(page)
    return page_faults