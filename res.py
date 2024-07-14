import tkinter as tk
from tkinter import messagebox


inventory = {}

def add():
    item = itementry.get()
    quantity = int(quantityentry.get())

    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] =quantity
   
    updateddisplay()

def checkrestock():
    threshold = int(thresholdentry.get())
    restockitems = []

    for item, quantity in inventory.items():
        if quantity < threshold:
            restockitems.append(item)
   
    if not restockitems:
        messagebox.showinfo("No Items to Restock", "All items are above the threshold.")
    else:
        restockapproval(restockitems)

def restockapproval(items):
    message = f"The following items are below the threshold:\n\n"
    for item in items:
        message += f"{item}: {inventory[item]} units\n"
   
    message += "\nDo you want to restock these items?"
   
    if messagebox.askyesno("Restock Confirmation", message):
        for item in items:
            inventory[item] += 10
       
        updateddisplay()

def updateddisplay():
    display.delete('1.0', tk.END)
    for item, quantity in inventory.items():
        display.insert(tk.END, f"{item}: {quantity} units\n")

root = tk.Tk()
root.title("Smart Inventory System")


additem = tk.Frame(root)
additem.pack(pady=10)

tk.Label(additem, text="Item Name:").grid(row=0, column=0)
itementry = tk.Entry(additem)
itementry.grid(row=0, column=1)

tk.Label(additem, text="Quantity:").grid(row=0, column=2)
quantityentry = tk.Entry(additem)
quantityentry.grid(row=0, column=3)

addbutton = tk.Button(additem, text="Add Item", command=add)
addbutton.grid(row=0, column=4, padx=10)


restock= tk.Frame(root)
restock.pack(pady=10)

tk.Label(restock, text="Threshold:").grid(row=0, column=0)
thresholdentry = tk.Entry(restock)
thresholdentry.grid(row=0, column=1)

checkrestockbutton = tk.Button(restock, text="Check & Restock", command=checkrestock)
checkrestockbutton.grid(row=0, column=2, padx=10)


display = tk.Text(root, height=10, width=50)
display.pack(pady=20)

updateddisplay()

root.mainloop()
