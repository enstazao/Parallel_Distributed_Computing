# Processes Linked List
from dstructure.SLL import SLL
import os
import signal

def pointer_to_pointer_processes_ll(no_of_processes):
    processes_ll = SLL()
    
    for i in range(no_of_processes):
        pid = os.fork()
        processes_ll.insert(pid)
        os.kill(pid, signal.SIGKILL)

    return processes_ll

processes_ll = pointer_to_pointer_processes_ll(5)
processes_ll.print()
