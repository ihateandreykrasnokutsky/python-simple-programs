import tkinter as tk

def createWindow(): #create a window
    windowA=tk.Tk() 
    windowA.title("My first Tkinter program")
    windowA.geometry("700x300")
    windowA.configure(bg="lightblue")
    windowA.iconbitmap("./python-simple-programs/015. tkinter pic/tkinter.ico")

    exit_button=tk.Button( #create a button on the window
        windowA,
        text="Exit shit",
        command=windowA.quit,
        bg="red",
        fg="white",
        font=("Arial", 18, "bold"),
        width=10
    )
    exit_button.pack(pady=10) #pack it with the window?

    windowA.mainloop() #loop

if __name__ == "__main__":
    createWindow()