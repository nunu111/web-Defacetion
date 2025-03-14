import requests
from bs4 import BeautifulSoup
import csv
import whois
import os
from datetime import datetime
from urllib.parse import urlparse
import tkinter as tk
from tkinter import filedialog, messagebox

def fetch_website_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        return None

def find_defacement(url, url_main_sub, rateLimit=3):
    found = []
    paths = ['']
    url_found = []
    founding = []
    url_notfound = []
    url_cannot_fetch = []

    fetched = set()
    fetch_domain = url.strip()
    sub_fetch_domain = url_main_sub.strip()
    isNotFinish = True
    paths = [fetch_domain + sub_fetch_domain]
    limit = 1

    result = ""

    try:
        open('keyword.txt', "x")
        result += 'keyword.txt does not exist. Now it was created, please write keyword in the file\n'
        return result
    except FileExistsError:
        while (isNotFinish and (limit <= rateLimit or rateLimit == 0)):
            limit += 1
            if len(paths) == 0: break
            else: fetch_url = paths.pop(0)
            found = []
            website_content = fetch_website_content(fetch_url)
            fetched.add(fetch_url)

            if website_content == None:
                url_cannot_fetch.append(fetch_url)
                continue
            soup = BeautifulSoup(website_content, 'html.parser')
            links = soup.find_all('a', href=True)
            with open('keyword.txt', 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for keyword in csv_reader:
                    if soup.find(string=lambda text: text and keyword[0] in text):
                        found.append(keyword[0])
                if found:
                    result += f"Defacement detected on the website: {fetch_url}\n"
                    result += f"Summary keyword that were found: {found}\n"
                    url_found.append(fetch_url)
                    founding.append(found)
                else:
                    result += f"No defacement detected on the website: {fetch_url}\n"
                    url_notfound.append(fetch_url)
            for link in links:
                path = link['href']
                path = path.strip()
                if path == None: continue
                if len(path) > 1:
                    if path.startswith('/'):
                        path = url + path
                    elif path.startswith(url):
                        path = path
                    else: continue
                    if not (path.endswith('.pdf') or path.endswith('.jpg') or path.endswith('.png')):
                        if (path not in paths) and (path not in fetched):
                            paths.append(path)
        write_result(url, url_found, founding, url_notfound, url_cannot_fetch)
        return result

def write_result(Domain, url_found, founding, url_notfound, url_cannot_fetch):
    os.makedirs("./History", exist_ok=True)
    current_date = datetime.now().date()
    f = open(f"./History/{str(urlparse(Domain).netloc)}-{current_date}.txt", "w", encoding='utf-8')
    f.write(f"{str(datetime.now().time())}\n")
    f.write(str(get_domain_info(Domain)))
    f.write("[Defacement detected]\n")
    if not url_found: f.write("-\n")
    for i in range(len(url_found)):
        f.write(f"{url_found[i]}\n")
        f.write(f"found: {founding[i]}\n")

    f.write("[No defacement detected]\n")
    if not url_notfound: f.write("-\n")
    for i in url_notfound:
        f.write(f"{i}\n")
    f.write("[Cannot fetch URL]\n")
    if not url_cannot_fetch: f.write("-\n")
    for i in url_cannot_fetch:
        f.write(f"{i}\n")
    f.write("------------------------------------------------------------------")
    f.close()

def check_internet_connection(url='http://www.google.com/', timeout=5):
    try:
        response = requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False

if check_internet_connection():
    print("Internet connection is available.")
else:
    print("No internet connection.")

def get_domain_info(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        return domain_info
    except Exception as e:
        return f"An error occurred: {e}"

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Note App")
        self.root.geometry("600x800")

        self.welcome_label = tk.Label(self.root, text="URL Scanner", font=('Arial', 16))
        self.welcome_label.pack(pady=(10, 0))

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.entry_number_frame = tk.Frame(self.root)
        self.entry_number_frame.pack(pady=10)

        self.entry_label = tk.Label(self.entry_frame, text="URL :")
        self.entry_label.pack(side='left')

        self.entry = tk.Entry(self.entry_frame, width=50)
        self.entry.pack(side='left', padx=5)

        self.entry_number = tk.Label(self.entry_number_frame, text="Rate limit:")
        self.entry_number.pack(side='left')
        validate_cmd = root.register(self.validate_input)
        self.entryNumber = tk.Entry(self.entry_number_frame, validate="key", width=45, validatecommand=(validate_cmd, '%P'))
        self.entryNumber.insert(0,0)
        self.entryNumber.pack(side='left', padx=5)

        self.keyword_label = tk.Label(self.root, text="Keyword", font=('Arial', 12))
        self.keyword_label.pack(pady=(10, 0))

        self.text_frame = tk.Frame(self.root, width=400, height=300)
        self.text_frame.pack(padx=10, pady=10, expand=True, fill='both')
        self.text_frame.pack_propagate(False)

        self.text = tk.Text(self.text_frame, wrap='word')
        self.text.pack(expand=1, fill='both', side='left')

        self.scrollbar = tk.Scrollbar(self.text_frame, command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)

        self.open_button = tk.Button(self.button_frame, text="Open", command=self.open_file)
        self.open_button.pack(side='left', padx=5)

        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_file)
        self.save_button.pack(side='left', padx=5)

        self.quit_button = tk.Button(self.button_frame, text="Exit", command=self.root.quit)
        self.quit_button.pack(side='left', padx=5)

        self.run_button = tk.Button(self.root, text="Run", command=self.show_message)
        self.run_button.pack(pady=10)

        self.result_text = tk.Text(self.root, wrap='word', height=10, state='disabled')
        self.result_text.pack(padx=10, pady=10, fill='both', expand=True)

        self.back_button = tk.Button(self.root, text="Back", command=self.go_back)
        self.back_button.pack_forget()

        self.open_file()

    def validate_input(self, new_value):
        return new_value == '' or new_value.isdigit()

    def show_message(self):
        website_url_sub1 = self.entry.get()
        website_url_sub2 = ""
        rateLimit = int(self.entryNumber.get()) if not self.entryNumber.get() == '' else 0
        result = find_defacement(website_url_sub1, website_url_sub2, rateLimit)
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state='disabled')
        self.hide_widgets_except_result_and_back()

    def go_back(self):
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state='disabled')
        self.show_all_widgets()

    def hide_widgets_except_result_and_back(self):
        self.entry_frame.pack_forget()
        self.entry_number_frame.pack_forget()
        self.welcome_label.pack_forget()
        self.keyword_label.pack_forget()
        self.text_frame.pack_forget()
        self.button_frame.pack_forget()
        self.run_button.pack_forget()
        self.back_button.pack(pady=20)

    def show_all_widgets(self):
        self.welcome_label.pack(pady=(10, 0))
        self.entry_frame.pack(pady=10)
        self.entry_number_frame.pack(pady=10)
        self.keyword_label.pack(pady=(10, 0))
        self.text_frame.pack(padx=10, pady=10, expand=True, fill='both')
        self.button_frame.pack(padx=10, pady=10)
        self.run_button.pack(pady=10)
        self.back_button.pack_forget()

    def open_file(self):
        try:
            with open('keyword.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, content)
        except FileNotFoundError:
            open('keyword.txt', "x", encoding='utf-8')
            messagebox.showinfo("File not found", "keyword.txt not found. Created keyword.txt in this directory.")

    def save_file(self):
        content = self.text.get(1.0, tk.END)
        try:
            with open('keyword.txt', 'w', encoding='utf-8') as file:
                file.write(content)
                messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

root = tk.Tk()
app = NoteApp(root)
root.mainloop()
