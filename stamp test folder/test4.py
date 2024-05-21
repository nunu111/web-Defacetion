import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")
        
        self.counter = 0
        self.running = True
        
        self.label = tk.Label(root, text=str(self.counter), font=("Helvetica", 48))
        self.label.pack(pady=20)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack(side="left", padx=20)
        
        self.resume_button = tk.Button(root, text="Resume", command=self.resume)
        self.resume_button.pack(side="right", padx=20)
        
        self.update_counter()

    def update_counter(self):
        if self.running:
            self.counter += 1
            self.label.config(text=str(self.counter))
        self.root.after(1000, self.update_counter)
        
    def pause(self):
        self.running = False
        
    def resume(self):
        self.running = True

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
