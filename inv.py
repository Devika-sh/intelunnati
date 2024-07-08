import tkinter as tk
root=tk.Tk()
root.geometry('600x350')
root.title('INTEL PROJECT')

def add():
    error_label.config(text="")
    name = e1.get()
    try:
        number = int(e2.get())
    except ValueError:
        return  # If entry_number is not a valid integer, do nothing
    
    if number > 1000:
        # Display a message or handle the case where number is >= 1000
        error_label.config(text="SORRY IT IS FILLED")
        return
    
    if name in dic:
        current_value = dic[name]
        new_value = current_value + number
        dic[name] = new_value
        e2.delete(0, tk.END)
        e2.insert(0, str(new_value))
    else:
        dic[name] = number
        preview()

def subtract():
    name = e1.get()
    try:
        number = int(e2.get())
    except ValueError:
        return  # If entry_number is not a valid integer, do nothing
    if number <= 0 and number >1000:
        # Display a message or handle the case where number is >= 0
         error_label.config(text="SORRY PLEASE BUY ITEMS, WE ARE OUT OF IT")
         return
    if name in dic:
        current_value = dic[name]
        new_value = current_value - number # Perform subtraction
        if new_value<0:
            error_label.config(text="WE DON'T HAVE IT THAT MUCH")
            return
        dic[name] = new_value
        e2.delete(0, tk.END)
        e2.insert(0, str(new_value))
    else:
        # Handle case where name doesn't exist (not specified in original request, so leaving empty for simplicity)
        pass
    preview()

def preview():
    preview_text.config(state=tk.NORMAL)
    preview_text.delete("1.0", tk.END)  # Clear previous content
    for name, number in dic.items():
        preview_text.insert(tk.END, f"{name}: {number}\n")
    preview_text.config(state=tk.DISABLED)

dic = {}

l1 = tk.Label(root,text='ENTER ITEM NAME ')
l2 = tk.Label(root,text='ENTER AMOUNT OF THE ITEM ')


error_label = tk.Label(root, text="", font=('Arial', 12), fg="red")


l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
error_label.grid(row=3, column=0, columnspan=4)


error_label = tk.Label(root, text="", font=('Arial', 12), fg="red")
error_label.grid(row=4, column=0, columnspan=4)
e1=tk.Entry(root)
e2=tk.Entry(root)


e1.grid(row=0,column=1)
e2.grid(row=1,column=1)


preview_text = tk.Text(root, height=10, width=30, state=tk.DISABLED)
preview_text.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

b1 = tk.Button(root,text='ADD',command=add)
b2 = tk.Button(root,text='REMOVE',command = subtract)


b1.grid(row=3,column=1)
b2.grid(row=3,column=2)

root.mainloop()
