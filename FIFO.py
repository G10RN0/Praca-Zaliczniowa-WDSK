from Dane import load_pages

#funkcja wykonująca algorymt FIFO
def FIFO(pages: list[int], R: int) -> int:
    frames = []
    page_faults = 0
    for page in pages:
        if page not in frames:
            page_faults += 1
            
            if len(frames) >= R:
                frames.pop(0)
                
            frames.append(page)
        
    return page_faults

if __name__ == "__main__":
    pages = load_pages("dane/strony/dane_strony[0].txt")
    
    for size in [3, 5, 7]:
        fifo_faults = FIFO(pages, size)
        print(f"Błędy stron dla FIFO (R={size}): {fifo_faults}")