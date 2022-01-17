from tkinter import *

window = Tk()
window.title('Konwerter')

def konwerter():
    grams=(float(kilo.get())*1000)
    pounds=(float(kilo.get())*2.20462)
    ounces=(float(kilo.get())*35.274)

    e1.delete("0", END)
    e1.insert(END, grams)

    e2.delete('0', END)
    e2.insert(END, pounds)

    e3.delete('0', END)
    e3.insert(END, ounces)

kg=Label(window, justify='center', text='KG')
kg.grid(row=0, column=0)

kilo=StringVar()
insert_kg=Entry(window, textvariable=kilo)
insert_kg.grid(row=0, column=1)

btn=Button(window, text="Convert", command=konwerter)
btn.grid(row=0, column=2)

#e1_value=StringVar()
#e2_value=StringVar()
#e3_value=StringVar()

e1=Entry(window)
e2=Entry(window)
e3=Entry(window)

e1.grid(row=1, column=0)
e2.grid(row=1, column=1)
e3.grid(row=1, column=2)

g=Label(window, justify='center', text='Grams')
p=Label(window, justify='center', text='Pounds')
o=Label(window, justify='center', text='Ounces')

g.grid(row=2, column=0)
p.grid(row=2, column=1)
o.grid(row=2, column=2)

window.mainloop()