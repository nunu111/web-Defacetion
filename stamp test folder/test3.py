import tkinter as tk
from tkinter import messagebox
import urllib.request

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
        status_label.config(text="Connected", fg="green")
    else:
        status_label.config(text="Disconnected", fg="red")
    # ตั้งค่าให้ฟังก์ชั่นนี้ถูกเรียกอีกครั้งใน 5 วินาที
    root.after(3000, update_status)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Internet Connection Status")

# สร้าง Label เพื่อแสดงสถานะการเชื่อมต่อ
status_label = tk.Label(root, text="Checking...", font=("Helvetica", 16))
status_label.pack(pady=20)

# เรียกฟังก์ชั่นเพื่ออัพเดตสถานะการเชื่อมต่อครั้งแรก
root.after(0, update_status)

# เริ่มต้นการทำงานของ GUI
root.mainloop()
