from tkinter import *


# Create window object
app = Tk()
global ans
def calculate():
    print("test")
    g = (ccg1.get() + ccg2.get() + ccg3.get() + ccg4.get() + ccg5.get())
    z = ((crds.get())+(crs.get()*3))
    #print(g)
    if (z != 0):
        print(((((ccg.get()) * (crds.get())) / 3 + g) /z)*3)
       # ans =((((ccg.get()) * (crds.get())) / 3 + g) / z) * 3
        ans= ((((ccg.get()) * (crds.get())) / 3 + g) / z) * 3
        part_label = Label(app, text='Your updated cgpa is ' + (str(ans))[:4], font=('bold', 20), pady=15)
        part_label.grid(row=3, column=4, sticky=W)
        part_label = Label(app, text='Your semester cgpa is ' + (str(g/(crs.get())))[:4], font=('bold', 20), pady=15)
        part_label.grid(row=4, column=4, sticky=W)


#question1
ccg = DoubleVar()
part_label = Label(app, text='your current cgpa :', font=('bold', 14), pady=15)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=ccg)
part_entry.grid(row=0, column=1)

#question2
crds = DoubleVar()
part_label = Label(app, text='how many credit you have completed :', font=('bold', 14), pady=15)
part_label.grid(row=1, column=0, sticky=W)
part_entry = Entry(app, textvariable=crds)
part_entry.grid(row=1, column=1)

#question2.5
crs = DoubleVar()
part_label = Label(app, text='how many course did you took :', font=('bold', 14), pady=15)
part_label.grid(row=2, column=0, sticky=W)
part_entry = Entry(app, textvariable=crs)
part_entry.grid(row=2, column=1)


#question3
ccg1 = DoubleVar()
part_label = Label(app, text='your gpa of course 1:', font=('bold', 14), pady=15)
part_label.grid(row=3, column=0, sticky=W)
part_entry = Entry(app, textvariable=ccg1)
part_entry.grid(row=3, column=1)


#question4
ccg2 = DoubleVar()
part_label = Label(app, text='your gpa of course 2:', font=('bold', 14), pady=15)
part_label.grid(row=4, column=0, sticky=W)
part_entry = Entry(app, textvariable=ccg2)
part_entry.grid(row=4, column=1)


#question5
ccg3 = DoubleVar()
part_label = Label(app, text='your gpa of course 3:', font=('bold', 14), pady=15)
part_label.grid(row=5, column=0, sticky=W)
part_entry = Entry(app, textvariable=ccg3)
part_entry.grid(row=5, column=1)

#question6
ccg4 = DoubleVar()
part_label = Label(app, text='your gpa of course 4:', font=('bold', 14), pady=15)
part_label.grid(row=6, column=0, sticky=W)
part_entry = Entry(app, textvariable=ccg4)
part_entry.grid(row=6, column=1)

#question7
ccg5 = DoubleVar()
part_label = Label(app, text='your gpa of course 5:', font=('bold', 14), pady=15)
part_label.grid(row=7, column=0, sticky=W)
part_entry = Entry(app, textvariable=ccg5)
part_entry.grid(row=7, column=1)


part_label = Label(app, text='ridwanshihab', font=('Arial', 5), pady=15)
part_label.grid(row=9, column=9, sticky=W)

#ans
#if calculate() is None:
 #   ans = ccg.get()
#else:
#ans =calculate()
#part_label = Label(app, text='The Square Root of ' + str(ans) + ' is:', font=('bold', 25), pady=15)
#part_label.grid(row=3, column=4, sticky=W)



# Buttons

add_btn = Button(app, text='Calculate', width=12, command=calculate)
add_btn.grid(row=8, column=0, pady=20)


app.title('CGcalculator')
app.geometry('1000x600')
# Start program
app.mainloop()



