import time
from rich import print

class Timer:
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        print(f'started [red]{self.name}[/red]')
        self.t0 = time.time()
        
    def __exit__(self, a1, a2, a3):
        print(f'completed [green]{self.name}[/green] in [blue bold]{time.time()-self.t0:.5f}[/blue bold]s')
        print()