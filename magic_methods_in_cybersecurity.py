# LogEntry and LogMonitor classes to store and monitor logs in cybersecurity

# LogEntry class with the most relevant attributes 

class LogEntry:
    def __init__(self, timestamp, severity, message):
        self.timestamp = timestamp
        self.severity = severity
        self.message = message
   
   # showing readable alerts

    def __str__(self):
        return f'{[self.timestamp]} {(self.severity)} {self.message}'

    # comparing entries
    
    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.message == other.message
   
   # sorting by time

    def __lt__(self, other):
        return self.timestamp < other.timestamp
   
   # gives log entry count

    def __len__(self):
        return len(self.message)
   
# Log Monitor class storing the log entries    
class LogMonitor:
    def __init__(self, entries):
        self.entries = entries
        self.index = 0
   
   # iterating through logs

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.entries):
            current = self.entries[self.index]
            self.index += 1
            return current
        raise StopIteration

# log entries from a monitoring tool e.g splunk

entries = [

        LogEntry("2025-04-11 10:22", "WARNING", "Multiple failed SSH attempts"),
        LogEntry("2025-04-11 10:25", "CRITICAL", "Root login from unknown IP"),
        ]

monitor = LogMonitor(entries)

for entry in monitor:
    print(entry)

print(len(entries[0])) # length of the message
print(entries[0] == entries[1]) # compare messages
print(entries[0] < entries[1]) # compare timestamps
    
    
