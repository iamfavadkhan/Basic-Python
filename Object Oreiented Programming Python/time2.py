class PrintTime:
    def __init__(self , hours , minutes , seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def print_time(self):
        print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")

time = PrintTime(9,3,45)
time.print_time()
