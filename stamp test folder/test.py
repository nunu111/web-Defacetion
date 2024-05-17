import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import urllib.request


def run():
    title.place_forget()
    by.place_forget()
    internet_text.place_forget()
    Internet_Label.place_forget()
    URL_text.place_forget()
    URL_Entry.place_forget()
    Scan_limit_text.place_forget()
    Scan_Limit_Entry.place_forget()
    keyword.place_forget()
    text_frame.place_forget()
    button1.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()

    result_title.place(x=150, y=10)
    result_Label.place(x=150, y=50)
    internet_text.place(x=150, y=85)
    Internet_Label.place(x=235, y=85)
    config_text.place(x=150, y=110)
    result_frame.place(x=100, y=140, width=500, height=250)
    button2.place(x=270, y=400)
    button5.place(x=370, y=400)


def back():
    result_title.place_forget()
    result_Label.place_forget()
    internet_text.place_forget()
    Internet_Label.place_forget()
    config_text.place_forget()
    result_frame.place_forget()
    button2.place_forget()
    button5.place_forget()

    title.place(x=225,y=10)
    by.place(x=285,y=40)
    internet_text.place(x=130,y=85)
    Internet_Label.place(x=225,y=85)
    URL_text.place(x=185,y=115)
    URL_Entry.place(x=225,y=115)
    Scan_limit_text.place(x=155, y=145)
    Scan_Limit_Entry.place(x=225, y=145)
    keyword.place(x=155,y=180)
    text_frame.place(x=225, y=180, width=150, height=275)
    button1.place(x=410,y=180)
    button2.place(x=410,y=215)
    button3.place(x=410,y=250)
    button4.place(x=410,y=430)



def open_file():
        try:
            with open('keyword.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                text.delete(1.0, tk.END)
                text.insert(tk.END, content)
        except FileNotFoundError:
            open('keyword.txt', "x", encoding='utf-8')
            messagebox.showinfo("File not found","keyword.txt not found. created keyword.txt on this direction.")

def save_file():
        content = text.get(1.0, tk.END)
        try:
            with open('keyword.txt', 'w', encoding='utf-8') as file:
                file.write(content)
                messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

# ฟังก์ชั่นเพื่อตรวจสอบการเชื่อมต่ออินเทอร์เน็ต
def check_internet_connection():
    try:
        # พยายามเชื่อมต่อไปยัง Google
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except:
        return False

# ฟังก์ชั่นสำหรับอัพเดตสถานะการเชื่อมต่อ
def update_status():
    if check_internet_connection():
        Internet_Label.config(text="Connected", fg="green")
    else:
        Internet_Label.config(text="Disconnected", fg="red")
    # ตั้งค่าให้ฟังก์ชั่นนี้ถูกเรียกอีกครั้งใน 3 วินาที
    root.after(3000, update_status)

def get_program_directory():
    # หา path ของโฟลเดอร์ที่โปรแกรมนี้อยู่
    program_path = os.path.dirname(sys.argv[0])
    return program_path

def open_History_folder(program_path):
    # ระบุ path ของโฟลเดอร์ที่ต้องการเปิด
    folder_path = program_path+r"\History"  # เปลี่ยนเป็น path ที่ต้องการเปิด

    # เปิดโฟลเดอร์ด้วยโปรแกรมเริ่มต้นของระบบ Windows
    os.startfile(folder_path)

def validate_entry(new_value):
    if new_value == "No Limit" or new_value == "":
        return True
    try:
        int(new_value)
        return True
    except ValueError:
        return False

def on_focus_in(event):
    if event.widget.get() == "No Limit":
        event.widget.delete(0, tk.END)

def on_focus_out(event):
    if event.widget.get() == "":
        event.widget.insert(0, "No Limit")

root = tk.Tk()
root.title("Open History Folder")
root.geometry('700x500+350+100')

title = tk.Label(root, text='Web Defacetion Scanner', font=('Arial', 16))
title.place(x=225,y=10)
by = tk.Label(root, text='by ITSC Intern 2024', font=('Arial', 10))
by.place(x=285,y=40)

internet_text = tk.Label(root, text="Internet Status :")
internet_text.place(x=130,y=85)
Internet_Label = tk.Label(root, text="Checking . . .")
Internet_Label.place(x=225, y=85)

URL_text = tk.Label(root, text="URL :")
URL_text.place(x=185,y=115)
URL_Entry = tk.Entry(root, width=45)
URL_Entry.place(x=225,y=115)

Scan_limit_text = tk.Label(root, text="Scan limit :")
Scan_limit_text.place(x=155, y=145)
validate_cmd = root.register(validate_entry)
Scan_Limit_Entry = tk.Entry(root, validate="key", validatecommand=(validate_cmd, '%P'), width=45)
Scan_Limit_Entry.insert(0, "No Limit")
Scan_Limit_Entry.bind("<FocusIn>", on_focus_in)
Scan_Limit_Entry.bind("<FocusOut>", on_focus_out)
Scan_Limit_Entry.place(x=225, y=145)


keyword = tk.Label(root, text="Keyword :")
keyword.place(x=155,y=180)
# Frame for Text Editor
text_frame = tk.Frame(root)
text_frame.place(x=225, y=180, width=150, height=275)
# Text Widget for displaying and editing the content
text = tk.Text(text_frame, wrap='word')
text.pack(fill=tk.BOTH, expand=True)

# Create three buttons
button1 = tk.Button(root, text="Save Keyword", command=save_file)
button1.place(x=410,y=180)
button2 = tk.Button(root, text="View History", command=lambda: open_History_folder(get_program_directory()))
button2.place(x=410,y=215)
button3 = tk.Button(root, text="Start Scan", command=run)
button3.place(x=410,y=250)
button4 = tk.Button(root, text="Exit Program", command=root.quit)
button4.place(x=410,y=430)


button5 = tk.Button(root, text="Back", command=back)
button5.place_forget()

result_title = tk.Label(root, text="Web Defacetion Scanner by ITSC Intern 2024")
result_title.place_forget()

result_Label = tk.Label(root, text="Result", font=('Arial', 16))
result_Label.place_forget()

config_text = tk.Label(root,text="URL : "+str(URL_Entry)+" | Scan limit :"+str(Scan_Limit_Entry))


result_frame = tk.Frame(root)
result_frame.place_forget()

result_text = tk.Text(result_frame, wrap='word')
result_text.pack(fill=tk.BOTH, expand=True)


root.after(0, update_status)
root.after(0, open_file)

root.mainloop()