class LogEntry:
    def __init__(self, timestamp, severity, message):
        self.timestamp = timestamp
        self.severity = severity
        self.message = message
        
    def __str__(self):
        return f'{[self.timestamp]} {(self.severity)} {self.message}'
    
    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.message == other.message
    
    def __lt__(self, other):
        return self.timestamp < other.timestamp
    
    def __len__(self, other):
        return len(self.message)
    
class LogMonitor:
    def __init__(self, entries):
        self.entries = entries
        self.index = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.entries):
            current = self.entries[self.index]
            self.index += 1
            return current
        raise StopIteration


entries =      
    
    