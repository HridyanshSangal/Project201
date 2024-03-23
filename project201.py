from tkinter import *
window = Tk()
window.title('Simple Interest Calculator')
window.geometry('380x400')
window.configure(bg = '#00ffab')

def calculateinterest():
    principle = int(principleenter.get())
    rate = int(rateenter.get())/100
    time = int(timeenter.get())
    interest = principle*rate*time
    interest = round(interest,2)
    resultlabel.destroy()
    outputmessage = Label(resultframe, text = f'Your interest is {interest}%',fg = 'black', bg = '#00ffab', font=('Times New Roman',14), width = 42)
    outputmessage.place(x = 20, y = 40)
    outputmessage.pack()
applabel = Label(window, text = 'Simple Interest Calculator', fg = 'black', bg = '#00ffab', font=('Times New Roman',21), bd = 5)
applabel.place(x = 50, y = 20)

principlelabel = Label(window, text = 'Enter Principle: ',fg = 'black', bg = '#00ffab', font=('Times New Roman',14), bd = 5)
principlelabel.place(x = 20, y = 90)

principleenter = Entry(window, text = '', bd = 2, width = 22)
principleenter.place(x = 150, y = 92)

ratelabel = Label(window, text = 'Enter rate: ',fg = 'black', bg = '#00ffab', font=('Times New Roman',14), bd = 5)
ratelabel.place(x = 20, y = 140)

rateenter = Entry(window, text = '', bd = 2, width = 22)
rateenter.place(x = 150, y = 142)

timelabel = Label(window, text = 'Enter time: ',fg = 'black', bg = '#00ffab', font=('Times New Roman',14), bd = 5)
timelabel.place(x = 20, y = 185)

timeenter = Entry(window, text = '', bd = 2, width = 22)
timeenter.place(x = 150, y = 187)

calculatebutton = Button(window,text = 'Calulate', fg = 'black', bg = 'cyan', font=('Times New Roman',14), bd = 5, command = calculateinterest)
calculatebutton.place(x = 20,y = 250)

resultframe = LabelFrame(window, text = 'Result: ',fg = 'black', bg = 'cyan', font=('Times New Roman',14))
resultframe.pack(padx=20, pady = 20)
resultframe.place(x = 20,y = 300)

resultlabel = Label(resultframe, text = '',fg = 'black', bg = 'cyan', font=('Times New Roman',14), width = 33)
resultlabel.place(x = 20,y= 20)
resultlabel.pack()
window.mainloop()