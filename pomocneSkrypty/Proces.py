#Process któremu bedzie trzeba przypisać czas
class Process:
    def __init__(self, arrivalTime, executionTime):
        self.arrivalTime=arrivalTime
        self.executionTime=executionTime
        
        #statystyki
        self.startTime: float = -1
        self.completionTime: float = 0
        self.waitingTime: float = 0
        self.turnAroundTime: float = 0
        
        #Round robin ~ zmienne
        self.remainingTime: float = self.executionTime