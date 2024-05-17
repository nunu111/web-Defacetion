import os
import sys
import tkinter as tk
from tkinter import filedialog

def get_program_directory():
    # หา path ของโฟลเดอร์ที่โปรแกรมนี้อยู่
    program_path = os.path.dirname(sys.argv[0])
    return program_path

def open_History_folder(program_path):
    # ระบุ path ของโฟลเดอร์ที่ต้องการเปิด
    folder_path = program_path+r"\History"  # เปลี่ยนเป็น path ที่ต้องการเปิด

    # เปิดโฟลเดอร์ด้วยโปรแกรมเริ่มต้นของระบบ Windows
    os.startfile(folder_path)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Open History Folder")

# สร้างปุ่ม "Open History Folder" และกำหนดให้เมื่อคลิกเรียกใช้ฟังก์ชัน open_History_folder
button_open = tk.Button(root, text="History Folder", command=lambda: open_History_folder(get_program_directory()))
button_open.pack(pady=20)

# เริ่มการทำงานของ GUI
root.mainloop()
