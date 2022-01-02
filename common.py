import time
from threading import Thread
from tkinter import END
import requests

class ThreadedTask(Thread):
    def __init__(self, text_board, start, step, prompt):
        super().__init__()
        self.text_board = text_board
        self.step_val = step
        self.prompt = prompt
        self.should_stop = False
        self.current = start

    def stop(self):
        self.should_stop = True

    def run(self):
        while True:
            if self.should_stop:
                break
            self.current += self.step_val
            self.text_board.insert(END, f"{self.prompt}{self.current}\n")
            self.text_board.see(END)
            time.sleep(0.01)
