import matplotlib.pyplot as plt
import os

def LruFifoGraph(scenariusz: int, frame_size: int, avg_fault: list[float], lines:list[int] , name_of_algorithm: str, path: str):
    
    name = f"Scenariusz[{scenariusz}], wielkoś ramki: {frame_size},  dla {name_of_algorithm}"    
    fig, ax = plt.subplots(figsize=(8,5))
    
    ax.barh(lines, avg_fault)
    
    ax.set_title(name)
    ax.set_xlabel('page_misses')
    ax.set_ylabel('ilość ramek')
    
    ax.set_yticks(lines)
    max_val = max(avg_fault)
    ax.set_xlim(0, max_val * 1.1)
    
    plt.tight_layout
    plt.savefig(path, dpi=100)
    plt.close()
    
def FcfsRoundRobinGraph(scenariusz:int, avg_wait: dict, avg_turnaround: dict, Quanta: int, path: str):
    labels = ["średnia czas czekania", "średni czas cyklu"]
    
    avg_wait_FCFS = avg_wait["FCFS"]
    avg_wait_RoundRobin = avg_wait["RR"]
    
    avg_turnaround_FCFS = avg_turnaround["FCFS"]
    avg_turnaround_RoundRobin = avg_turnaround["RR"]
    
    figs, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    #wykres FCFS
    bars1=ax1.bar(labels, (avg_wait_FCFS, avg_turnaround_FCFS))
    ax1.set_title(f"Scenariusz[{scenariusz}], algorytm FCFS")
    ax1.set_ylim(0, (max((avg_wait_FCFS, avg_turnaround_FCFS))+100))
    ax1.bar_label(bars1, padding=3, fmt='%.2f') 
    
    #wykres Round Robin
    bars2=ax2.bar(labels, (avg_wait_RoundRobin, avg_turnaround_RoundRobin))
    ax2.set_title(f"Scenariusz[{scenariusz}], algorytm Round Robin dla kwanty: {Quanta}")
    ax2.set_ylim(0, (max((avg_wait_RoundRobin, avg_turnaround_RoundRobin))+100))
    ax2.bar_label(bars1, padding=3, fmt='%.2f')
    
    plt.tight_layout
    plt.savefig(path, dpi=100)
    plt.close()
    
#LruFifoGraph(1, 3, [88.96, 66, 30], [25, 20, 10], "CHUJ")
#FcfsRoundRobinGraph(1, {"FCFS":800, "RR":750}, {"FCFS":820, "RR":800}, 3)