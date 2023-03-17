import pandas as pd
import matplotlib

matplotlib.use('Agg')
from tkinter import *
from tkinter.ttk import *

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
file = askopenfilename(title="SMG Count: Select file",
                       filetypes=(("Excel files", "*.xls"), ("Excel files", "*.xlsx"), ("All files", "*.*")))
df = pd.read_excel(file)
df1 = df.Name
df1.dropna(axis=0, inplace=True)
df2 = df1.value_counts().to_frame()
df2.reset_index(inplace=True)
df2.columns = ["Name", "Count"]
df2.sort_values('Name', inplace=True)
df2
file_out = file + "_RawCount.csv"
df2.to_csv(file_out, index=False)

from tkinter import messagebox

messagebox.showinfo("SMG Count", "Raw Count File Generated Successfully")
