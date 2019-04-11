from tkinter import filedialog
import tkinter as tk
from read import ReadCSVClass
import csv
from fields import status_fields,value_fields
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class Application:
    """
    GUI Application which counts how many visitors enter the building.
    The application prints the count of visitors in the console
    """
    def __init__(self, master):
        self.master = master
        self.ReadCSVClass = ReadCSVClass(self)
        self.filename = None
        self.tempLabel = None
        self.driverError = None
        topFrame = tk.Frame(self.master, height=300, width=500)
        self.topFrame = topFrame
        topFrame.pack()
        bottomFrame = tk.Frame(self.master, bg="Blue")
        self.bottomFrame = bottomFrame
        bottomFrame.pack(side=tk.BOTTOM)

        self.button1 = tk.Button(bottomFrame, text="Open", command=self.open_file)
        self.button2 = tk.Button(bottomFrame, text="Fetch", command=self.fetch_file)
        self.button3 = tk.Button(bottomFrame, text="Exit", command=self.close_window)

        self.button1.pack(side=tk.LEFT)
        self.button2.pack(side=tk.LEFT)
        self.button3.pack(side=tk.LEFT)

        try:
            browser = webdriver.Chrome()
            browser.close()
        except Exception as e:
            self.button1.pack_forget()
            self.button2.pack_forget()
            self.button3.pack_forget()
            tk.Label(self.topFrame, text=(e), wraplength=500, justify=tk.LEFT).pack(pady=0,padx=20)
            self.driverError = e
            # return e


        self.button_clicks = 0
    def takeUpdate(self, update):
        # tk.Label(self.topFrame, text=(update)).pack(pady=0,padx=20)
        self.stv.set(update)
        self.master.update()
        # print(update)

    def fetch_file(self):
        self.ReadCSVClass.subscribe(self.takeUpdate)
        if self.filename is None:
            self.tempLabel = tk.Label(self.topFrame, text=('Please open a file'))
            self.tempLabel.pack(pady=0,padx=20)
            return
        self.files = self.ReadCSVClass.readCSV(self.filename)
        filename =  filedialog.asksaveasfilename(initialdir = "/home/priyanka/work",title = "Select file",filetypes = [("CSV files","*.csv"), ('all files', '.*')])
        col = status_fields + value_fields
        try:
            with open(filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=col, extrasaction='ignore')
                writer.writeheader()
                for data in self.files:
                    writer.writerow(data)
        except IOError as e:
            self.stv.set(e)
            return
        self.stv.set('Successfully saved file at '+filename)


    def open_file(self):
        filename =  filedialog.askopenfilename(initialdir = "/home/priyanka/work",title = "Select file",filetypes = [("CSV files","*.csv"), ('all files', '.*')])
        self.filename = filename
        if self.tempLabel is not None:
            self.tempLabel.pack_forget()
        tk.Label(self.topFrame, text=('Will fetch - '+ filename), justify=tk.LEFT).pack(pady=10,padx=20)
        tk.Label(self.topFrame, text=('To replace file click open, To Start fetching click Fetch'), justify=tk.LEFT).pack(pady=10,padx=20)
        self.stv = tk.StringVar()
        tk.Label(self.topFrame, textvariable=self.stv).pack(pady=0,padx=20)
    def close_window(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    root.geometry("500x400")
    root.title('Google auto crawl')
    # tk.Label(root, text='Python').pack(pady=20,padx=50)
    Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()