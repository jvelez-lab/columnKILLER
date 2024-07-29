import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

# Function to open a file dialog and select a file
def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")]
    )
    if file_path:
        file_path_var.set(file_path)  # Update the file path variable with the selected file path

# Function to delete specified columns from the selected file and save the updated file
def delete_columns():
    file_path = file_path_var.get()
    columns = columns_entry.get().split(',')

    if not file_path:
        messagebox.showerror("Error", "Please select a file")
        return
    
    if not columns:
        messagebox.showerror("Error", "Please enter columns to delete")
        return

    try:
        # Read the selected file into a DataFrame
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            messagebox.showerror("Error", "Unsupported file type")
            return
        
        # Delete the specified columns from the DataFrame
        df.drop(columns=columns, inplace=True)
        
        # Save the updated DataFrame back to the original file
        if file_path.endswith('.csv'):
            df.to_csv(file_path, index=False)
        elif file_path.endswith('.xlsx'):
            df.to_excel(file_path, index=False)

        messagebox.showinfo("Success", "Columns deleted successfully and file updated")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
app = tk.Tk()
app.title("columnKILLER")

file_path_var = tk.StringVar()  # Variable to store the file path

# Create and place the widgets in the window
tk.Label(app, text="File:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(app, textvariable=file_path_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(app, text="Columns to KILL (comma separated):").grid(row=1, column=0, padx=10, pady=10)
columns_entry = tk.Entry(app, width=50)
columns_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(app, text="KILL Column(s)", command=delete_columns).grid(row=2, column=1, pady=10)

app.mainloop()  # Run the main event loop
