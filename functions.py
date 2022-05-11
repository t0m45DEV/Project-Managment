from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import io


def init():
    defaultlanguage = io.open("Defaults/language.txt", "r")
    readeddefaultlanguage = defaultlanguage.readlines()
    chooselanguage(readeddefaultlanguage)

    defaultcolor = io.open("Defaults/color.txt", "r")
    readeddefaultcolor = defaultcolor.readlines()
    variables.windowcolor = readeddefaultcolor[0].replace("\n", "")

    variables.root = tk.Tk()
    variables.root.title(variables.windowtitle)
    variables.root.config(bg=variables.windowcolor)
    variables.root.resizable(0, 0)

    windowmenu()
    createcolumns()
    createlistboxes()
    createbuttons()

    variables.root.mainloop()


def chooselanguage(language):
    global variables
    language = language[0].replace("\n", "")
    predeterminatelanguage(language)

    if language == "español":
        import espvariables as variables

    elif language == "english":
        import engvariables as variables

    else:
        messagebox.showwarning(variables.error02[0], variables.error02[1])


def windowmenu():
    variables.windowmenu = tk.Menu(variables.root)
    variables.root.config(menu=variables.windowmenu)

    variables.filemenu = tk.Menu(variables.windowmenu, tearoff=0)
    variables.filemenu.add_command(label=variables.savetext,
        command=savetasklist)
    variables.filemenu.add_command(label=variables.quicksavetext,
        command=quicksavetasklist)
    variables.filemenu.add_command(label=variables.loadtext,
        command=loadtasklist)

    variables.colormenu = tk.Menu(variables.windowmenu, tearoff=0)
    variables.colormenu.add_command(label=variables.colorsnames[0],
        command=lambda:changecolor(variables.colors[0]))
    variables.colormenu.add_command(label=variables.colorsnames[1],
        command=lambda:changecolor(variables.colors[1]))
    variables.colormenu.add_command(label=variables.colorsnames[2],
        command=lambda:changecolor(variables.colors[2]))

    variables.languagemenu = tk.Menu(variables.windowmenu, tearoff=0)
    variables.languagemenu.add_command(label=variables.espanishtext,
        command=lambda:changelanguage("español"))
    variables.languagemenu.add_command(label=variables.englishtext,
        command=lambda:changelanguage("english"))

    variables.helpmenu = tk.Menu(variables.windowmenu, tearoff=0)
    variables.helpmenu.add_command(label=variables.abouttext,
        command=aboutwindow)

    variables.windowmenu.add_cascade(label=variables.filetext,
        menu=variables.filemenu)
    variables.windowmenu.add_cascade(label=variables.colortext,
        menu=variables.colormenu)
    variables.windowmenu.add_cascade(label=variables.languagetext,
        menu=variables.languagemenu)
    variables.windowmenu.add_cascade(label=variables.helptext,
        menu=variables.helpmenu)


def changelanguage(language):
    if predeterminatelanguage(language) == 0:
        pass
    else:
        variables.root.destroy()
        init()


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


def changecolor(color):
    if predeterminatecolor(color) == 0:
        pass
    else:
        variables.root.destroy()
        init()


def predeterminatecolor(color):

    bydefault = io.open("Defaults/color.txt", "r+")
    readedbydefault = bydefault.read()

    if color in readedbydefault:
        return 0

    else:
        bydefault.seek(0)
        bydefault.truncate(0)
        bydefault.write(color)
        return 1

    bydefault.close()


def aboutwindow():
    messagebox.showinfo(variables.aboutinfo[0], variables.aboutinfo[1])


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


def deletetask():
    todo  = variables.todolistbox.curselection()
    doing = variables.doinglistbox.curselection()
    done  = variables.donelistbox.curselection()

    if todo != doing and todo != done:
        selectedtask = variables.todolistbox.curselection()[0]
        variables.todolistbox.delete(selectedtask)

    elif doing != todo and doing != done:
        selectedtask = variables.doinglistbox.curselection()[0]
        variables.doinglistbox.delete(selectedtask)

    elif done != todo and done != doing:
        selectedtask = variables.donelistbox.curselection()[0]
        variables.donelistbox.delete(selectedtask)

    else:
        messagebox.showwarning(variables.error03[0], variables.error03[1])


def movetask():
    todo  = variables.todolistbox.curselection()
    doing = variables.doinglistbox.curselection()
    done  = variables.donelistbox.curselection()

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


def addtask(column):
    if "|" in variables.entrytext.get():
        messagebox.showwarning(variables.error05[0], variables.error05[1])

    else:
        if variables.entrytext.get() != "":
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


def savetasklist():
    try:
        saveroute = filedialog.asksaveasfilename(title=variables.savefileas,
            filetypes=((variables.textfiles, "*.txt"), (variables.allfiles, "*.*")),
            initialdir="Saves")
        savedfile = io.open(saveroute, "w")
        variables.quicksaveroute = saveroute
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

    except TypeError:
        pass
    except FileNotFoundError:
        pass


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


def loadtasklist():
    try:
        loadroute = filedialog.askopenfilename(title=variables.openfile,
            filetypes=((variables.textfiles, "*.txt"), (variables.allfiles, "*.*")),
            initialdir="Saves")
        loadedfile = io.open(loadroute, "r")
        variables.quicksaveroute = loadroute

        variables.todolistbox.delete(0, variables.todolistbox.size())
        variables.doinglistbox.delete(0, variables.doinglistbox.size())
        variables.donelistbox.delete(0, variables.donelistbox.size())

        turn = 0
        for i in loadedfile.readlines():
            turn += 1
            addedtask = ""
            i = i.replace("\n", "")
            for b in i:
                if b == "|":
                    if turn == 1:
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

        for i in variables.todotasklist:
            variables.todolistbox.insert(tk.END, i)
        for i in variables.doingtasklist:
            variables.doinglistbox.insert(tk.END, i)
        for i in variables.donetasklist:
            variables.donelistbox.insert(tk.END, i)

        waitlist(0)
        loadedfile.close()

    except TypeError:
        pass
    except FileNotFoundError:
        pass


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
