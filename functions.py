# Projectbot by t0m45DEV
# This is the version 2.0


# ---------------------------------------------------
# -- Here we call some of the libraries we'll need --
# ---------------------------------------------------

# A color palette window
from tkinter import colorchooser
# Messagebox create the pop-up windows
from tkinter import messagebox
# This will help us with the saving and loading txt files
from tkinter import filedialog
# Tkinter will create the graphical user interface
import tkinter as tk
# Io will help us writing and reading txt files
import io


# ---------------------------------------------------
# ---- Next are the functions of the app itself  ----
# ---------------------------------------------------

# This will initiate the program
def init():
    # Here we read the last choosed language
    defaultlanguage = io.open("Defaults/language.txt", "r")
    readeddefaultlanguage = defaultlanguage.readlines()
    chooselanguage(readeddefaultlanguage)

    # Here we read the last choosed color
    defaultcolor = io.open("Defaults/color.txt", "r")
    readeddefaultcolor = defaultcolor.readlines()
    variables.windowcolor = readeddefaultcolor[0].replace("\n", "")

    # Here we create the window
    variables.root = tk.Tk()
    variables.root.title(variables.windowtitle)
    variables.root.config(bg=variables.windowcolor)
    variables.root.resizable(0, 0)

    # This are my functions, that put everything inside the window
    windowmenu()
    createcolumns()
    createlistboxes()
    createbuttons()

    # Finally, this is the tkinter mainloop
    variables.root.mainloop()


# -------------------------------------------------------------
# -- Those are functions that create the stuff in the window --
# -------------------------------------------------------------

# This function create the upper section of the window
# The "cascade buttons"
def windowmenu():
    variables.windowmenu = tk.Menu(variables.root)
    variables.root.config(menu=variables.windowmenu)

    # Here is the saving files section
    variables.filemenu = tk.Menu(variables.windowmenu, tearoff=0)
    variables.filemenu.add_command(label=variables.savetext,
        command=savetasklist)
    variables.filemenu.add_command(label=variables.quicksavetext,
        command=quicksavetasklist)
    variables.filemenu.add_command(label=variables.loadtext,
        command=loadtasklist)

    # This are the theme or color section
    variables.colormenu = tk.Menu(variables.windowmenu, tearoff=0)
    variables.colormenu.add_command(label=variables.changebackground,
        command=lambda:changecolor(colorchooser.askcolor()[1]))

    # Language section
    variables.languagemenu = tk.Menu(variables.windowmenu, tearoff=0)
    variables.languagemenu.add_command(label=variables.espanishtext,
        command=lambda:changelanguage("esp"))
    variables.languagemenu.add_command(label=variables.englishtext,
        command=lambda:changelanguage("eng"))

    # Help and info section
    variables.helpmenu = tk.Menu(variables.windowmenu, tearoff=0)
    variables.helpmenu.add_command(label=variables.abouttext,
        command=aboutwindow)

    # Here we add all the before mentioned buttons to the window itself
    variables.windowmenu.add_cascade(label=variables.filetext,
        menu=variables.filemenu)
    variables.windowmenu.add_cascade(label=variables.colortext,
        menu=variables.colormenu)
    variables.windowmenu.add_cascade(label=variables.languagetext,
        menu=variables.languagemenu)
    variables.windowmenu.add_cascade(label=variables.helptext,
        menu=variables.helpmenu)


# Disclaimer: The next functions works with the same logic, they
# just create buttons and tkinter stuff, but I separate them for
# order and better code reading

# This creates the buttons on top of the lists. I called it create
# columns because they start at the column 0 of the tkinter frame
# grid system. It's just a normal tkinter button creation, nothing
# new
def createcolumns():
    variables.todobutton = tk.Button(variables.root,
        text=variables.listsnames[0],
        command=lambda:addtask(0))
    variables.todobutton.grid(row=0, column=0, padx=variables.padx,
        pady=variables.pady, sticky="nsew")

    variables.doingbutton = tk.Button(variables.root,
        text=variables.listsnames[1],
        command=lambda:addtask(1))
    variables.doingbutton.grid(row=0, column=1, padx=variables.padx,
        pady=variables.pady, sticky="nsew")

    variables.donebutton = tk.Button(variables.root,
        text=variables.listsnames[2],
        command=lambda:addtask(2))
    variables.donebutton.grid(row=0, column=2, padx=variables.padx,
        pady=variables.pady, sticky="nsew")


# Now this is the lists themselves, same logic as createcolumns()
def createlistboxes():
    variables.todolistbox = tk.Listbox(variables.root)
    variables.todolistbox.grid(row=1, column=0,
        padx=variables.padx, pady=variables.pady)

    variables.doinglistbox = tk.Listbox(variables.root)
    variables.doinglistbox.grid(row=1, column=1,
        padx=variables.padx, pady=variables.pady)

    variables.donelistbox = tk.Listbox(variables.root)
    variables.donelistbox.grid(row=1, column=2,
        padx=variables.padx, pady=variables.pady)


# This create the column number 3, which have the entry text box, and
# the last two buttons
def createbuttons():
    variables.entrytext = tk.StringVar()
    variables.entrybutton = tk.Entry(variables.root,
        textvariable=variables.entrytext)
    variables.entrybutton.grid(row=2, column=0,
        padx=variables.padx, pady=variables.pady)

    variables.movebutton = tk.Button(variables.root,
        text=variables.movetext, command=movetask)
    variables.movebutton.grid(row=2, column=1,
        padx=variables.padx, pady=variables.pady)

    variables.erasebutton = tk.Button(variables.root,
        text=variables.erasetext, command=deletetask)
    variables.erasebutton.grid(row=2, column=2,
        padx=variables.padx, pady=variables.pady)


# -------------------------------------------------------------------------
# -- Primary buttons functions: create, move and delete tasks from lists --
# -------------------------------------------------------------------------

# This will read the entry box, and create a new task in the specified column
def addtask(column):
    # First we check for possible errors, like having a | in the entr box or
    # having nothing at all
    if "|" in variables.entrytext.get():
        messagebox.showwarning(variables.error05[0], variables.error05[1])

    else:
        if variables.entrytext.get() != "":
            # After that, we use the parameter column (which is the button
            # one) to know where the task was, and where we want to move it
            # Also, remember to erase anything in the entry box
            if column == 0:
                variables.todolistbox.insert(tk.END, variables.entrytext.get())
                variables.entrytext.set("")

            if column == 1:
                variables.doinglistbox.insert(tk.END, variables.entrytext.get())
                variables.entrytext.set("")

            if column == 2:
                variables.donelistbox.insert(tk.END, variables.entrytext.get())
                variables.entrytext.set("")

        else:
            messagebox.showwarning(variables.error01[0], variables.error01[1])


# This will erase the selected taks
def deletetask():
    # Here we chek, in every task column, the current selection. The one that
    # has the selection, will have a value, the others will be null
    todo  = variables.todolistbox.curselection()
    doing = variables.doinglistbox.curselection()
    done  = variables.donelistbox.curselection()

    # Here we check if to-do-list has the current selection
    if todo != doing and todo != done:
        selectedtask = variables.todolistbox.curselection()[0]
        variables.todolistbox.delete(selectedtask)

    # Here we check if the doing-list has the selection
    elif doing != todo and doing != done:
        selectedtask = variables.doinglistbox.curselection()[0]
        variables.doinglistbox.delete(selectedtask)

    # Here we check if the done-list has the selection
    elif done != todo and done != doing:
        selectedtask = variables.donelistbox.curselection()[0]
        variables.donelistbox.delete(selectedtask)

    else:
        messagebox.showwarning(variables.error03[0], variables.error03[1])


# This works kinda like a combination of addtask and deletetask, but
# the tricky part comes in knowing where to put the erased task
def movetask():
    todo  = variables.todolistbox.curselection()
    doing = variables.doinglistbox.curselection()
    done  = variables.donelistbox.curselection()

    # Here, after cheking where is the current selection, I save the
    # text of it in a variable (selectedtask) and then insert it in
    # the next column
    # In the last column, the selected task it's just erased
    if todo != doing and todo != done:
        task = variables.todolistbox.get(variables.todolistbox.curselection())
        selectedtask = variables.todolistbox.curselection()[0]
        variables.todolistbox.delete(selectedtask)
        variables.doinglistbox.insert(tk.END, task)

    elif doing != todo and doing != done:
        task = variables.doinglistbox.get(variables.doinglistbox.curselection())
        selectedtask = variables.doinglistbox.curselection()[0]
        variables.doinglistbox.delete(selectedtask)
        variables.donelistbox.insert(tk.END, task)

    elif done != todo and done != doing:
        task = variables.donelistbox.get(variables.donelistbox.curselection())
        selectedtask = variables.donelistbox.curselection()[0]
        variables.donelistbox.delete(selectedtask)

    else:
        messagebox.showwarning(variables.error04[0], variables.error04[1])


# ---------------------------------------------------
# ----- Saving and loading lists from txt files -----
# ---------------------------------------------------

# This takes every value in the 3 lists, and put them into python
# lists that I can handle
def waitlist(inout):
    if inout == 1:
        for i in range(variables.todolistbox.size()):
            variables.todotasklist.append(variables.todolistbox.get(i))

        for i in range(variables.doinglistbox.size()):
            variables.doingtasklist.append(variables.doinglistbox.get(i))

        for i in range(variables.donelistbox.size()):
            variables.donetasklist.append(variables.donelistbox.get(i))

    elif inout == 0:
        variables.todotasklist  = []
        variables.doingtasklist = []
        variables.donetasklist  = []


# This open a save file window, and create a txt file with the lists
def savetasklist():
    try:
        # Here we create the window and the file itself
        saveroute = filedialog.asksaveasfilename(title=variables.savefileas,
            filetypes=((variables.textfiles, "*.txt"), (variables.allfiles, "*.*")),
            initialdir="Saves")
        savedfile = io.open(saveroute, "w")
        variables.quicksaveroute = saveroute
        waitlist(1)

        # And here, using the lists from waitlist(1), we write the file,
        # puting every value between |, and every line is a column
        for i in variables.todotasklist:
            savedfile.write(i + "|")
        savedfile.write("\n")
        for i in variables.doingtasklist:
            savedfile.write(i + "|")
        savedfile.write("\n")
        for i in variables.donetasklist:
            savedfile.write(i + "|")

        # Then we close the file and clean up the python lists
        waitlist(0)
        savedfile.close()

    except TypeError:
        # Here is the TypeError exception, that appears when a
        # route to a file is typed wrong
        pass
    except FileNotFoundError:
        # This one jumps out when a file is not found
        pass


# This work exactly as savetasklist() but without a window or
# noticing the user
def quicksavetasklist():
    if variables.quicksaveroute == "":
        savetasklist()

    else:
        savedfile = io.open(variables.quicksaveroute, "w")
        variables.quicksaveroute = variables.quicksaveroute
        waitlist(1)

        for i in variables.todotasklist:
            savedfile.write(i + "|")
        savedfile.write("\n")
        for i in variables.doingtasklist:
            savedfile.write(i + "|")
        savedfile.write("\n")
        for i in variables.donetasklist:
            savedfile.write(i + "|")

        waitlist(0)
        savedfile.close()


# This one starts same as savetasklist(), but the tricky part comes
# with the reading
def loadtasklist():
    try:
        # Load the file to read
        loadroute = filedialog.askopenfilename(title=variables.openfile,
            filetypes=((variables.textfiles, "*.txt"), (variables.allfiles, "*.*")),
            initialdir="Saves")
        loadedfile = io.open(loadroute, "r")
        variables.quicksaveroute = loadroute

        # Erasing the lists on the columns
        variables.todolistbox.delete(0, variables.todolistbox.size())
        variables.doinglistbox.delete(0, variables.doinglistbox.size())
        variables.donelistbox.delete(0, variables.donelistbox.size())

        # Prepare a turn which we'll use as a counter
        turn = 0
        for i in loadedfile.readlines():
            turn += 1
            addedtask = ""
            # Ignore the line jumps
            i = i.replace("\n", "")
            for b in i:
                # Check the |
                if b == "|":
                    if turn == 1:
                        # Write it into the python list
                        variables.todotasklist.append(addedtask)
                        addedtask = ""
                    elif turn == 2:
                        variables.doingtasklist.append(addedtask)
                        addedtask = ""
                    elif turn == 3:
                        variables.donetasklist.append(addedtask)
                        addedtask = ""
                else:
                    addedtask += b

        # Here we write the values into the real tasks columns
        for i in variables.todotasklist:
            variables.todolistbox.insert(tk.END, i)
        for i in variables.doingtasklist:
            variables.doinglistbox.insert(tk.END, i)
        for i in variables.donetasklist:
            variables.donelistbox.insert(tk.END, i)

        # Then we close the file and erase the wait lists
        waitlist(0)
        loadedfile.close()

    # Controlling a few exceptions
    except TypeError:
        pass
    except FileNotFoundError:
        pass


# ------------------------------------------------------------
# -- Secondary buttons functions: color, language and info --
# ------------------------------------------------------------

# The short version, is that we search for the default language
# file, we read it, and we import the variables from that language
# If anything wrong happened, the error 2 window will pop up
def chooselanguage(language):
    global variables
    language = language[0].replace("\n", "")
    predeterminatelanguage(language)

    if "esp" in language:
        import espvariables as variables

    elif "eng" in language:
        import engvariables as variables

    else:
        messagebox.showwarning(variables.error02[0], variables.error02[1])


# First we check if the actual language is the same that the user choosed
# In that case, we just ignore that input. If the user really wants to
# change the language, we destroy the actual window and create another one
# with the new language
def changelanguage(language):
    if predeterminatelanguage(language) == 0:
        pass
    else:
        variables.root.destroy()
        init()


# Here comes the magic. First we read the last language file, then we check
# if the choosed one if the actual one. If this is not the case, we erase
# everything in the langage.txt file, and write inside it the new language
def predeterminatelanguage(language):

    bydefault = io.open("Defaults/language.txt", "r+")
    readedbydefault = bydefault.read()

    if language in readedbydefault:
        return 0

    else:
        bydefault.seek(0)
        bydefault.truncate(0)
        bydefault.write(language)
        return 1

    bydefault.close()


# This and the next function works exactly as the language ones, but checks
# the color of the window instead
def changecolor(color):
    if predeterminatecolor(color) == 0:
        pass
    else:
       variables.root.config(bg=color)


# Same logic as predeterminatelanguage()
def predeterminatecolor(color):

    if color == None:
        pass

    else:
        bydefault = io.open("Defaults/color.txt", "r+")
        readedbydefault = bydefault.read()

        if (color in readedbydefault):
            return 0

        else:
            bydefault.seek(0)
            bydefault.truncate(0)
            bydefault.write(color)
            return 1

        bydefault.close()


# This creates the about window, pretty simple function
def aboutwindow():
    messagebox.showinfo(variables.aboutinfo[0], variables.aboutinfo[1])
