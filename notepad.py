import tkinter as tk

def open_file():
    pass
def clear_text():
    pass
def save_file():
    # Get the text from the text area
    text = text_area.get("1.0", "end-1c")

    # Open a file for writing and write the text to it
    with open("saved_text.txt", "w") as f:
        f.write(text)
# Create the main window
window = tk.Tk()
window.title("Notepad")

# Create a text area to enter and display text
text_area = tk.Text(window)
text_area.pack(fill=tk.BOTH, expand=True)


menu_bar = tk.Menu(window)

window.config(menu=menu_bar)



file_menu= tk.Menu (menu_bar, tearoff=False)

edit_menu= tk.Menu(menu_bar, tearoff=False)

menu_bar.add_cascade (label="File", menu=file_menu)

menu_bar.add_cascade (label="Edit", menu=edit_menu)

file_menu.add_command(label="Open", command=open_file)

file_menu.add_command(label="Save", command=save_file)

file_menu.add_command (label="Clear", command=clear_text)



# Create a function to save the text
'''def save_text():
    # Get the text from the text area
    text = text_area.get("1.0", "end-1c")

    # Open a file for writing and write the text to it
    with open("saved_text.txt", "w") as f:
        f.write(text)

# Create a button to save the text

save_button = tk.Button(window, text="Save", command=save_text)
save_button.pack()'''

# Run the main loop
window.mainloop()
