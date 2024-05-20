import tkinter as tk  # PEP8: `import *` is not preferred
import time

# --- functions ---  # PEP8: all functions before main code

def b1():
    global running

    running = True
    
    loop()
    
def loop():    
    print('MY MAIN CODE')
    
    if running:
        # repeat after 100ms (0.1s)
        top.after(100, loop)  # funcion's name without ()
    else:
        print('STOP')
        
def b2(): 
    global running
    
    running = False
    
# --- main ---

running = True

top = tk.Tk()

but1 = tk.Button(top, text="On",  command=b1)   # PEP8: inside `()` use `=` without spaces
but2 = tk.Button(top, text="Off", command=b2)
but1.pack()
but2.pack()

top.mainloop()