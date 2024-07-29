import tkinter as tk
from tkinter import messagebox
from colorama import Fore, Style, init


init()


def print_large_title():
    title_art = """

    """
    print(Fore.GREEN + title_art + Style.RESET_ALL)  


def submit_data():
    app_site = entry_app_site.get()
    username = entry_username.get()
    password = entry_password.get()
    
    if app_site and username and password:
        
        with open('users.txt', 'a') as file:
            file.write(f'App/site: {app_site:<20} Username: {username:<20} Password: {password:<20} <------\n')
        
        
        messagebox.showinfo("Success", "User data saved successfully!")
        
        
        entry_app_site.delete(0, tk.END)
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter app/site, username, and password.")


def toggle_password():
    global password_visible
    if password_visible:
        entry_password.config(show="*")
        button_toggle.config(text="Show")
    else:
        entry_password.config(show="")
        button_toggle.config(text="Hide")
    password_visible = not password_visible


print_large_title()


root = tk.Tk()
root.title("User Data Entry")


black = '#000000'  
green = '#39a754'  


root.configure(bg=black)


title_art = """
▒█░░▒█ ░█▀▀█ ▒█▀▀▄ ▒█▀▀▀█ 　 ▒█▀▀▄ ░█▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█▀▀█ ░█▀▀█ ▒█▀▀▀█ ▒█▀▀▀ 
▒█▒█▒█ ▒█▄▄█ ▒█░▒█ ▒█░░▒█ 　 ▒█░▒█ ▒█▄▄█ ░▒█░░ ▒█▄▄█ ▒█▀▀▄ ▒█▄▄█ ░▀▀▀▄▄ ▒█▀▀▀ 
▒█▄▀▄█ ▒█░▒█ ▒█▄▄▀ ▒█▄▄▄█ 　 ▒█▄▄▀ ▒█░▒█ ░▒█░░ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄▄
"""

title_label = tk.Label(root, text=title_art, font=("Courier", 10), justify=tk.LEFT, bg=black, fg=green)
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

label_app_site = tk.Label(root, text="App/Site:", bg=black, fg=green)
label_app_site.grid(row=1, column=0, padx=10, pady=10)
entry_app_site = tk.Entry(root, bg=black, fg=green, insertbackground='green')  
entry_app_site.grid(row=1, column=1, padx=10, pady=10)


label_username = tk.Label(root, text="Username:", bg=black, fg=green)
label_username.grid(row=2, column=0, padx=10, pady=10)
entry_username = tk.Entry(root, bg=black, fg=green, insertbackground='green')  
entry_username.grid(row=2, column=1, padx=10, pady=10)


label_password = tk.Label(root, text="Password:", bg=black, fg=green)
label_password.grid(row=3, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*", bg=black, fg=green, insertbackground='green')  
entry_password.grid(row=3, column=1, padx=10, pady=10)


password_visible = False
button_toggle = tk.Button(root, text="Show", command=toggle_password, bg=green, fg=black)
button_toggle.grid(row=3, column=2, padx=10, pady=10)


button_submit = tk.Button(root, text="Submit", command=submit_data, bg=green, fg=black)
button_submit.grid(row=4, column=0, columnspan=3, pady=10)


root.mainloop()
