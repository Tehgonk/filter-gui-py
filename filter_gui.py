import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import json

# Create the main window
window = tk.Tk()
window.title("Filter GUI")
window.geometry("460x660")

# Create the label widgets
#top_label = tk.Label(text="Use the text boxes below to create a filter rule. Rules get added to 'rules.txt' and can be copy+pasted into the filter rules of the extension.", font="Arial 8 bold", wraplength=380)
instructions_label_1 = tk.Label(text="Separate each value with a comma", wraplength=380)
character_label = tk.Label(text="Character(s):")
item_label = tk.Label(text="Item(s):")
blessing_label = tk.Label(text="Blessing(s):")
perk_label = tk.Label(text="Perk(s):")
instructions_label_2 = tk.Label(text="Single integer value", wraplength=380)
minStats_label = tk.Label(text="Min. stats:")
MinRating_label = tk.Label(text="Min. rating:")
MinBlessingRarity_label = tk.Label(text="Min. blessing rarity (1-4):")
MinPerkRarity_label = tk.Label(text="Min. perk rarity (1-4):")
instructions_label_3 = tk.Label(text="Either 'credits' or 'marks' (Melk)", wraplength=380)
shop_label = tk.Label(text="Shop type:")
instructions_label_4 = tk.Label(text="Output", font="Arial 8 bold", wraplength=380)

# Create the entry widgets
character_entry = tk.Entry(width=35)
item_entry = tk.Entry(width=35)
blessing_entry = tk.Entry(width=35)
perk_entry = tk.Entry(width=35)
minStats_entry = tk.Entry(width=35)
minRating_entry = tk.Entry(width=35)
minBlessingRarity_entry = tk.Entry(width=35)
minPerkRarity_entry = tk.Entry(width=35)
shop_entry = tk.Entry(width=35)

# Create a separator widget
#separator_1 = ttk.Separator(window, orient=tk.HORIZONTAL)
separator_2 = ttk.Separator(window, orient=tk.HORIZONTAL)
separator_3 = ttk.Separator(window, orient=tk.HORIZONTAL)
separator_4 = ttk.Separator(window, orient=tk.HORIZONTAL)

# Add the top label, separator, and entry widgets to the grid
#top_label.grid(row=0, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(10, 0))

#separator_1.grid(row=1, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(10, 0), padx=(10, 0))

instructions_label_1.grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(10, 0))
character_label.grid(row=3, column=0, padx=(10, 0), pady=(10, 0))
character_entry.grid(row=4, column=0, padx=(10, 0), pady=(0, 10))
item_label.grid(row=3, column=1, padx=(10, 0), pady=(10, 0))
item_entry.grid(row=4, column=1, padx=(10, 0), pady=(0, 10))
blessing_label.grid(row=5, column=0, padx=(10, 0))
blessing_entry.grid(row=6, column=0, padx=(10, 0), pady=(0, 10))
perk_label.grid(row=5, column=1, padx=(10, 0))
perk_entry.grid(row=6, column=1, padx=(10, 0), pady=(0, 10))

separator_2.grid(row=7, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(10, 0), padx=(10, 0))

instructions_label_2.grid(row=8, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(10, 0))
minStats_label.grid(row=9, column=0, padx=(10, 0), pady=(10, 0))
minStats_entry.grid(row=10, column=0, padx=(10, 0), pady=(0, 10))
MinRating_label.grid(row=9, column=1, padx=(10, 0), pady=(10, 0))
minRating_entry.grid(row=10, column=1, padx=(10, 0), pady=(0, 10))
MinBlessingRarity_label.grid(row=11, column=0, padx=(10, 0))
minBlessingRarity_entry.grid(row=12, column=0, padx=(10, 0), pady=(0, 10))
MinPerkRarity_label.grid(row=11, column=1, padx=(10, 0))
minPerkRarity_entry.grid(row=12, column=1, padx=(10, 0), pady=(0, 10))

separator_3.grid(row=13, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(10, 0), padx=(10, 0))

instructions_label_3.grid(row=14, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(10, 0))
shop_label.grid(row=15, column=0, columnspan=2, padx=(10, 0), pady=(10, 0))
shop_entry.grid(row=16, column=0, columnspan=2, padx=(10, 0), pady=(0, 10))

separator_4.grid(row=17, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(10, 0), padx=(10, 0))

instructions_label_4.grid(row=18, column=0, columnspan=2, sticky=tk.W+tk.E, pady=(10, 0))

# Create a frame to hold the output text widget
output_frame = tk.Frame(window)
output_frame.grid(row=19, column=0, columnspan=2, sticky=tk.W+tk.E)

# Create a scrollable text widget to display the JSON output
output_text = tk.Text(output_frame, width=50, height=8, wrap=tk.WORD, yscrollcommand=True)
output_text.pack(pady=10)

# Create a list to store the data for all entries
data_list = []

# Create the add button
def add_entry():
    # Create the data dictionary
    data = {}

    # Get the values from the textboxes and add them to the dictionary if they are not empty
    character = character_entry.get()
    if character:
        values = character.split(", ")
        if len(values) > 1:
            data["character"] = values
        else:
            data["character"] = values[0]

    item = item_entry.get()
    if item:
        values = item.split(", ")
        if len(values) > 1:
            data["item"] = values
        else:
            data["item"] = values[0]

    blessing = blessing_entry.get()
    if blessing:
        values = blessing.split(", ")
        if len(values) > 1:
            data["blessing"] = values
        else:
            data["blessing"] = values[0]

    perk = perk_entry.get()
    if perk:
        values = perk.split(", ")
        if len(values) > 1:
            data["perk"] = values
        else:
            data["perk"] = values[0]

    minStats = minStats_entry.get()
    if minStats:
        data["minStats"] = int(minStats)

    minRating = minRating_entry.get()
    if minRating:
        data["minRating"] = int(minRating)

    minBlessingRarity = minBlessingRarity_entry.get()
    if minBlessingRarity:
        data["minBlessingRarity"] = int(minBlessingRarity)

    minPerkRarity = minPerkRarity_entry.get()
    if minPerkRarity:
        data["minPerkRarity"] = int(minPerkRarity)

    shop = shop_entry.get()
    if shop:
        data["shop"] = shop

    # Clear the contents of the entry fields
    character_entry.delete(0, "end")
    item_entry.delete(0, "end")
    blessing_entry.delete(0, "end")
    perk_entry.delete(0, "end")
    minStats_entry.delete(0, "end")
    minRating_entry.delete(0, "end")
    minBlessingRarity_entry.delete(0, "end")
    minPerkRarity_entry.delete(0, "end")
    shop_entry.delete(0, "end")

    # Add the data to the data list
    data_list.append(data)

    # Format the data list as JSON and add it to the text widget
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, json.dumps(data_list, indent=4))

add_button = tk.Button(text="Add", command=add_entry)
add_button.configure(width=10)
add_button.grid(row=20, column=0, pady=(10, 0))

# Create the copy button
def copy():
    # Get the contents of the text widget
    data = output_text.get("1.0", "end-1c")

    # Copy the data to the clipboard
    window.clipboard_clear()
    window.clipboard_append(data)

copy_button = tk.Button(text="Copy", command=copy)
copy_button.configure(font=("Arial 7 bold"), bg="white", activebackground="white", bd=0)
copy_button.place(x=390, y=455)

# undo function
def undo(event):
    # Remove the last entry from the data list
    data_list.pop()

    # Format the data list as JSON and add it to the text widget
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, json.dumps(data_list, indent=4))

window.bind("<Control-z>", undo)

# Create the export button
def export():
    # Get the contents of the text widget
    data = output_text.get("1.0", "end-1c")

    # Create a file dialog to save the file
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")

    # Write the data to the file
    file.write(data)

    # Close the file
    file.close()

export_button = tk.Button(text="Export", command=export)
export_button.configure(width=10)
export_button.grid(row=20, column=1, pady=(10, 0))

# Run the main loop
window.mainloop()