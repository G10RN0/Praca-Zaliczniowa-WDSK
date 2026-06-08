import matplotlib.pyplot as plt
import os

FOLDER = "Wyniki"

def LruFifoGraph(scenariusz: int, frame_size: int, avg_fault: list[float], lines:list[int] , name_of_algorithm: str):
    
    name = f"Scenariusz[{scenariusz}], wielkoś ramki: {frame_size},  dla {name_of_algorithm}"    
    fig, ax = plt.subplots(figsize=(8,5), facecolor="white")
    ax.set_facecolor("white")
    
    ax.barh(lines, avg_fault)
    
    ax.set_title(name)
    ax.set_xlabel('page_misses')
    ax.set_ylabel('ilość ramek')
    
    ax.set_yticks(lines)
    
    # Dla wartości 88.98 limit 75/90 uetnie wykres, warto go trochę podbić:
    max_val = max(avg_fault)
    ax.set_xlim(0, max_val * 1.1)
    
    plt.tight_layout()
    plt.show()
    


if __name__ == "__main__":
    LruFifoGraph(1, 3, [88.96, 66, 30], [25, 20, 10], "CHUJ")