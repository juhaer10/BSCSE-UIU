import tkinter as tk
from tkinter import Button, Label, LEFT

class StopWatch:
    def __init__(self, master):
        self.master = master
        self.running = False
        self.time = 0

        self.label = Label(master, text="00:00:00")
        self.label.pack()

        Button(master, text='Start', command=self.start).pack(side=LEFT)
        Button(master, text='Stop', command=self.stop).pack(side=LEFT)
        Button(master, text='Reset', command=self.reset).pack(side=LEFT)

    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")

    def update_timer(self):
        if self.running:
            self.time += 1
            self.label.config(text=self.format_time(self.time))
            self.master.after(1000, self.update_timer)

    def format_time(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

def main():
    root = tk.Tk()
    sw = StopWatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
