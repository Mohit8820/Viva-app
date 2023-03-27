import tkinter as tk
import os
import random as r
from tkinter import messagebox as mb

win=tk.Tk()
win.title("Viva")
win.geometry("1200x700")
win.minsize(width=1000,height=600)
p1 = tk.PhotoImage(file = 'D:/Coding Projects/Python projects/Viva app/vivaIcon.png')   
# Icon set for program window
win.iconphoto(False, p1) 

def goHomeorExit():
    if mb.askyesno("Continue","Press YES to go home or NO to exit"):
        main()
    else:
        win.destroy()

def deleteF2():
    for child in f2.winfo_children():
        child.destroy()

def quit():
    if mb.askyesno("Exit","Want to exit?"):
        win.destroy()


#global f2
#global entry
fname=tk.StringVar(value="temp_viva.txt")
heading=tk.StringVar(value="Welcome")
studList=[]

def reset(studNo,quesNo,quesList,studList):
    deleteF2()
    l1 = tk.Label(f2, text = "Questions:", font=("Century Gothic", 12,"bold"),bg="#1f2937",fg="white").grid(pady=10,sticky=tk.W)
    questions=r.sample(quesList,int(quesNo))
    f4=tk.Frame(f2)
    f5=tk.Frame(f4,height=400,width=1000)
    canvas = tk.Canvas(f5,bg="#1f2937")
    scrollbar = tk.Scrollbar(f5, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas,bg="#1f2937")
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind_all("<MouseWheel>",
                    lambda e: canvas.yview_scroll(-1*int(e.delta/120), "units"))
    c=1
    for i in questions:
        question = tk.Label(scrollable_frame, text = "Q"+str(c)+" - "+i,
                            font=("Century Gothic", 12),bg="#1f2937",fg="white",
                            wraplength=950,justify=tk.LEFT).pack(anchor=tk.W)
        c=c+1
    f5.pack()
    f5.pack_propagate(0)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    f4.grid()
    
    if(len(studList)>=int(studNo)):
        students=r.sample(studList,int(studNo))
    else:
        students=studList
    f3=tk.Frame(f2,bg="#1f2937")
    f3.grid(pady=10)
    l2 = tk.Label(f3, text = "Student Roll Numbers:", font=("Century Gothic", 12,"bold"),
                  bg="#1f2937",fg="white").grid(row=100,column=0,sticky=tk.W,ipady=10)
    k=1
    for j in students:
        student = tk.Label(f3, text = j,bg="#fde047",bd=3,fg="#000",font=("Century Gothic", 12)).grid(row=100,column=k,padx=10,ipadx=10)
        k=k+1
    if(len(studList)>int(studNo)):
        resetBtn = tk.Button(f2, text = 'Reset',
                             command=lambda:reset(studNo,quesNo,quesList,studList),
                             bg="#fde047",bd=3,fg="#000",font=("Century Gothic", 12),
                             relief=tk.RIDGE).grid(pady=50,ipadx=20)
    else:
        doneBtn = tk.Button(f2, text = 'Done',
                             command=goHomeorExit,bg="#fde047",bd=3,fg="#000",
                            font=("Century Gothic", 12),relief=tk.RIDGE).grid(pady=50,ipadx=20)
        
    for j in students:
        studList.remove(j)
    #print(studList)
    

# def vivaFunc(r1,r2,studNo,quesNo):
#     heading.set("Viva")
#     quesFile=open(fname.get(),'r')
#     quesList=quesFile.readlines()
#     #check student and ques size should be less than their list
#     studList=[*range(int(r1), int(r2)+1, 1)]
#     #print(studList)
#     reset(studNo,quesNo,quesList,studList)
    
    
def validate(r1,r2,studNo,quesNo):
    try:
        r1=int(r1)
        r2=int(r2)
        studNo=int(studNo)
        quesNo=int(quesNo)
        quesFile=open(fname.get(),'r')
        quesList=quesFile.readlines()
        if(r1>r2 or r1<1):
            mb.showerror("Wrong input","Please enter valid roll number range")
        elif(studNo<1 or quesNo<1):
            mb.showerror("Wrong input","Please enter integer numbers greater than 0")
        elif(studNo>(r2-r1+1)):
            mb.showerror("Wrong input","Number of students exceed the roll number range")
        elif(quesNo>len(quesList)):
            mb.showerror("Wrong input","Number of questions mentioned exceed the number of questions in file")
        else:
            heading.set("Viva")
            studList=[*range(int(r1), int(r2)+1, 1)]
            #print(studList)
            reset(studNo,quesNo,quesList,studList)
    except  Exception as e: 
        print(e)
        mb.showerror("Wrong input","Please enter integer numbers greater than 0")
    

def beginViva():
    deleteF2()
    heading.set("Fill the required information and start")    
    info1=tk.Label(f2, text="Enter range of roll no:", font=("Century Gothic", 12,"bold"),bg="#1f2937",fg="white").grid(pady=10,row=0,column=0,sticky=tk.W)
    r1= tk.Entry(f2, width= 10, font=("Century Gothic", 12),justify=tk.CENTER)
    r1.grid(row=0,column=1, ipady=10)
    r1.insert(0, 1)
    dash=tk.Label(f2, text="-", font=("Century Gothic", 12,"bold"),bg="#1f2937",fg="white").grid(pady=10,row=0,column=2)
    r2= tk.Entry(f2, width= 10, font=("Century Gothic", 12),justify=tk.CENTER)
    r2.grid(row=0,column=3, ipady=10)
    r2.insert(0, 20)
    info2=tk.Label(f2, text="Enter no. of students to be examined at a time:", font=("Century Gothic", 12,"bold"),bg="#1f2937",fg="white").grid(pady=20,sticky=tk.W)
    studNo= tk.Entry(f2, width= 10, font=("Century Gothic", 12),justify=tk.CENTER)
    studNo.grid(row=1,column=2, ipady=10)
    studNo.insert(0, 3)
    info3=tk.Label(f2, text="Enter no. of questions to be displayed for above mentioned no. of students:", font=("Century Gothic", 12,"bold"),bg="#1f2937",fg="white").grid(pady=10,sticky=tk.W)
    quesNo= tk.Entry(f2, width= 10, font=("Century Gothic", 12),justify=tk.CENTER)
    quesNo.grid(row=2,column=2, ipady=10)
    quesNo.insert(0, 5)
    beginBtn = tk.Button(f2, text = 'Start',command=lambda:validate(r1.get(),r2.get(),studNo.get(),quesNo.get()),bg="#fde047",bd=3,fg="#000",font=("Century Gothic", 12), relief=tk.RIDGE).grid(columnspan=4,pady=50,ipadx=20)

def addQues(ques):
    #print(ques)
    if(ques!= ""):
        quesFile=open(fname.get(),'a')
        quesFile.write(str(ques)+"\n")
        quesFile.close()
    typeQues()

def typeQues():
    deleteF2()
    if str(fname.get()).endswith("_viva.txt")==False:
        fname.set(fname.get()+"_viva.txt")
    heading.set("Add Question")   
    info=tk.Label(f2, text="Enter a question:", font=("Century Gothic", 12,"bold"),bg="#1f2937",fg="white").grid(pady=10)
    q= tk.Entry(f2, width= 120, font=("Century Gothic", 12))
    q.grid(ipady=20)
    f3=tk.Frame(f2,bg="#1f2937")
    f3.grid(pady=50)
    vivaBtn = tk.Button(f3, text = 'Begin Viva',command=beginViva,bg="#fde047",bd=3,fg="#000",font=("Century Gothic", 12), relief=tk.RIDGE).grid(row=20,column=0,padx=30)
    addBtn = tk.Button(f3, text = 'Add',command=lambda:addQues(q.get()),bg="#fde047",bd=3,fg="#000",font=("Century Gothic", 12), relief=tk.RIDGE).grid(row=20,column=1,padx=30)



def selectFile():
    deleteF2()
    heading.set("Select file")
    f3=tk.Frame(f2,bg="#fde047")
    f3.grid(ipadx=100,pady=5,columnspan=3)
    k=0
    for x in os.listdir():
        if x.endswith("_viva.txt"):
            k=k+1
            R1 = tk.Radiobutton(f3, text=str(x).replace(".txt",""), variable=fname, value=str(x),font =("Century Gothic", 12),bg="#fde047")
            R1.grid(sticky=tk.W)
    if k==0:
        info=tk.Label(f2, text = "No previous file found", font=("Century Gothic", 12,"bold"),bg="#1f2937",fg="white").grid(pady=10)
        newFileBtn = tk.Button(f2, text = 'Create new File',command=newFile,bg="#fde047",bd=3,fg="#000",font=("Century Gothic", 12), relief=tk.RIDGE).grid(row=200,column=0,pady=50)
    else:
        vivaBtn = tk.Button(f2, text = 'Begin Viva',command=beginViva,bg="#fde047",bd=3,fg="#000",font=("Century Gothic", 12), relief=tk.RIDGE).grid(row=200,column=0,pady=50)
        addBtn = tk.Button(f2, text = 'Add Questions',command=typeQues,bg="#fde047",bd=3,fg="#000",font=("Century Gothic", 12), relief=tk.RIDGE).grid(row=200,column=2,pady=50)

def newFile():
    deleteF2()
    heading.set("New file")
    l1 = tk.Label(f2, text = "Name of file", font=("Century Gothic", 12,"bold"),bg="#1f2937",fg="white").grid(pady=10)
    newFname= tk.Entry(f2, width= 40, textvariable=fname, font=("Century Gothic", 12))
    newFname.grid(ipady=10)
    addBtn = tk.Button(f2, text = 'Add Questions',command=typeQues,bg="#fde047",bd=3,fg="#000",font=("Century Gothic", 12), relief=tk.RIDGE).grid(row=20,column=0,padx=30,pady=50)


def main():
    deleteF2()
    heading.set("Welcome")
    l1 = tk.Label(f2, text = "Select a file and begin", font=("Century Gothic", 12,"bold"),bg="#1f2937",fg="white").grid(pady=30)
    photo = tk.PhotoImage(file="D:/Coding Projects/Python projects/Viva app/vivaGif.gif")
    img = tk.Label(f2, image=photo)
    img.image = photo
    img.grid()

menubar = tk.Menu(win)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=selectFile)
menubar.add_cascade(label="File", menu=filemenu)

menubar.add_command(label="Home", command=main)

menubar.add_command(label="Exit", command=quit)

win.config(menu=menubar)
head=tk.Label(win,textvariable = heading,font =("Century Gothic", 22,"bold"),bg="#fde047",foreground="#1f2937").pack(fill = tk.X, ipady = 15)
f1=tk.Frame(win,bg="#1f2937",borderwidth=1)
f1.pack(fill=tk.BOTH,expand=True)
f2=tk.Frame(f1,bg="#1f2937")
f2.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
main()
win.mainloop()
