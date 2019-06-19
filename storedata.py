from tkinter import *

root = Tk(className="Validation")
root.config(width=300, height=300)


values = ["jeremias", "perla uriel", "junior", "mario", "jose", "mateo", "perro", "juan", "ezequiel"]


frame = Frame(root)
frame.place(x=50, y=20)

labelVal = StringVar()

vallabel = StringVar()




def createLabelValue(values):
    if values == "" or len(values) > 20:
        if values == "":
            labelVal.set("Introduzca un usuario")
        elif len(values) > 20:
            labelVal.set("usuario demasiado largo")
    else:
        if values == "No encontrado":
            labelVal.set("No encontrado pero\n ha sido almacenado")
        else:
            labelVal.set("Nombre: {}".format(values.upper()))


def valueAdd(n):
    # agregando valores al store(array)
    values.append(n.get())


def getvalue(n1):

    i = 0
    valor = 0
    v = False


    while i < len(values):
        if n1.get() == values[i]:
            v = True
            valor = values[i]
        else:
            createLabelValue("No encontrado")

        i += 1

    if v == True:
        createLabelValue(valor)
    else:
        valueAdd(n1)


def call():
    getvalue(vallabel)


entry = Entry(frame, textvariable=vallabel)
entry.grid(row=1, column=0)
entry.config(justify="center", font="verdana")


label = Label(frame, textvariable=labelVal, font="Arial")
label.grid(row=3, column=0)



button = Button(frame, command=call)
button.grid(row=2, column=0)
button.config(text="Buscar", font="Arial", bd=0, fg="white", bg="blue", padx=20)



program_base = root.mainloop()
