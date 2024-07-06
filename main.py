import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os
import json


colors = {
    "base": "#1e1e2e",
    "mantle": "#181825",
    "crust": "#11111b",
    "text": "#cdd6f4",
    "subtext0": "#a6adc8",
    "subtext1": "#bac2de",
    "overlay0": "#6c7086",
    "overlay1": "#7f849c",
    "overlay2": "#9399b2",
    "surface0": "#313244",
    "surface1": "#45475a",
    "surface2": "#585b70",
    "blue": "#89b4fa",
    "green": "#a6e3a1",
    "red": "#f38ba8",
    "yellow": "#f9e2af"
}

def process_zip_files(input_folder, output_folder, new_pack_format_number):
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.zip'):
            zip_file_path = os.path.join(input_folder, file_name)
            new_zip_file_path = os.path.join(output_folder, file_name.replace('.zip', '_modified.zip'))

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                with zipfile.ZipFile(new_zip_file_path, 'w') as new_zip_ref:
                    for item in zip_ref.infolist():
                        if item.filename.endswith('.mcmeta'):
                            mcmeta_content = zip_ref.read(item.filename)
                            mcmeta_data = json.loads(mcmeta_content)
                            mcmeta_data['pack']['pack_format'] = new_pack_format_number
                            modified_mcmeta_content = json.dumps(mcmeta_data, indent=2).encode('utf-8')
                            new_zip_ref.writestr(item, modified_mcmeta_content)
                        else:
                            new_zip_ref.writestr(item, zip_ref.read(item.filename))

            print(f"New zip file created: {new_zip_file_path}")
            messagebox.showinfo("Success", f"New zip file created: {new_zip_file_path}")

def select_input_folder():
    folder_selected = filedialog.askdirectory()
    input_folder_var.set(folder_selected)

def select_output_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_var.set(folder_selected)

def on_process():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    try:
        new_pack_format_number = int(pack_format_var.get())
        process_zip_files(input_folder, output_folder, new_pack_format_number)
    except ValueError:
        messagebox.showerror("Error", "Pack format number must be an integer.")

app = tk.Tk()
app.title("Zip Processor")
app.configure(bg=colors["base"])

tk.Label(app, text="Input Folder:", fg=colors["text"], bg=colors["base"]).grid(row=0, column=0, padx=10, pady=5)
input_folder_var = tk.StringVar()
tk.Entry(app, textvariable=input_folder_var, width=50, bg=colors["surface0"], fg=colors["text"], insertbackground=colors["text"]).grid(row=0, column=1, padx=10, pady=5)
tk.Button(app, text="Browse", command=select_input_folder, bg=colors["blue"], fg="black").grid(row=0, column=2, padx=10, pady=5)

tk.Label(app, text="Output Folder:", fg=colors["text"], bg=colors["base"]).grid(row=1, column=0, padx=10, pady=5)
output_folder_var = tk.StringVar()
tk.Entry(app, textvariable=output_folder_var, width=50, bg=colors["surface0"], fg=colors["text"], insertbackground=colors["text"]).grid(row=1, column=1, padx=10, pady=5)
tk.Button(app, text="Browse", command=select_output_folder, bg=colors["blue"], fg="black").grid(row=1, column=2, padx=10, pady=5)

tk.Label(app, text="New pack_format number:", fg=colors["text"], bg=colors["base"]).grid(row=2, column=0, padx=10, pady=5)
pack_format_var = tk.StringVar()
tk.Entry(app, textvariable=pack_format_var, width=50, bg=colors["surface0"], fg=colors["text"], insertbackground=colors["text"]).grid(row=2, column=1, padx=10, pady=5)

tk.Button(app, text="Start Processing", command=on_process, bg=colors["green"], fg="black").grid(row=3, column=0, columnspan=3, padx=10, pady=20)

app.mainloop()
