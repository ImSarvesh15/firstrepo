from tkinter import*
from tkinter import messagebox
import tkinter.messagebox
import random
import time;

root=Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Managaement System")

text_Input=StringVar()
operator=""

Tops=Frame(root,width=1600,height=50,bg="powder blue",relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#======================================time==========================
localtime=time.asctime(time.localtime(time.time()))
#===========================info==================================
lblInfo=Label(Tops,font=('arial',50,'bold'),text="Gurukrupa Restaurant",fg="Crimson",
bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Crimson",
bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#=========================calculator========================================
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
def Ref():
    x=random.randint(2020,50876)
    randomRef=str(x)
    rand.set(randomRef)

    CoF=float(Fries.get())
    CoD=float(Drinks.get())
    CoP=float(Pizza.get())
    CoBurger=float(Burger.get())
    CoSamosa=float(Samosa.get())
    CoPattice=float(Pattice.get())

    CostofFries=CoF*40
    CostofDrinks=CoD*30
    CostofPizza=CoP*60
    CostofBurger=CoBurger*45
    CostofSamosa=CoSamosa*15
    CostofPattice=CoPattice*15

    CostofMeal="₹",str('%.2f' % (CostofFries + CostofDrinks + CostofPizza + CostofBurger
                                   +CostofSamosa + CostofPattice))
    PayTax=((CostofFries + CostofDrinks + CostofPizza + CostofBurger
                                   +CostofSamosa + CostofPattice)*0.2)
    TotalCost=((CostofFries + CostofDrinks + CostofPizza + CostofBurger
                                   +CostofSamosa + CostofPattice))
    Ser_Charge=((CostofFries + CostofDrinks + CostofPizza + CostofBurger
                                   +CostofSamosa + CostofPattice)/99)

    Service="₹",str('%.2f' % Ser_Charge )
    OverallCost="₹",str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    PaidTax="₹",str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverallCost)

def qExit():
    qExit=tkinter.messagebox.askyesno("Restaurant Management System","Confirm you want to Exit?")
    if qExit>0:
        root.destroy()
    return

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Pizza.set("")
    Total.set("")
    Service_Charge.set("")
    SubTotal.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Samosa.set("")
    Pattice.set("")


txtDisplay=Entry(f2,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,
bg="cadet blue",justify='right')    
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="powder blue",
command=lambda:btnClick(7)).grid(row=2,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="powder blue",
command=lambda:btnClick(8)).grid(row=2,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="powder blue",
command=lambda:btnClick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="powder blue",
command=lambda:btnClick("+")).grid(row=2,column=3)
#====================================================================================================
btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="powder blue",
command=lambda:btnClick(4)).grid(row=3,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="powder blue",
command=lambda:btnClick(5)).grid(row=3,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="powder blue",
command=lambda:btnClick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="powder blue",
command=lambda:btnClick("-")).grid(row=3,column=3)
#============================================================================================
btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="powder blue",
command=lambda:btnClick(1)).grid(row=4,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="powder blue",
command=lambda:btnClick(2)).grid(row=4,column=1)

btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text ="3",bg="powder blue",
command=lambda:btnClick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="powder blue",
command=lambda:btnClick("*")).grid(row=4,column=3)
#===================================================================================================
btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",bg="powder blue",
command=lambda:btnClick(0)).grid(row=5,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="C",
bg="powder blue",command=btnClearDisplay).grid(row=5,column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="=",
bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",bg="powder blue",
command=lambda:btnClick("/")).grid(row=5,column=3)
#================================Restro info=========================================================
rand=StringVar()
Fries=StringVar()
Burger=StringVar()
Pizza=StringVar()
Total=StringVar()
Service_Charge=StringVar()
SubTotal=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Samosa=StringVar()
Pattice=StringVar()

lblReference=Label(f1,font=('arial',16,'bold'),text="Reference",bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtReference.grid(row=0,column=1)

lblFries=Label(f1,font=('arial',16,'bold'),text="French Fries",bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtFries.grid(row=1,column=1)

lblBurger=Label(f1,font=('arial',16,'bold'),text="Burger",bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtBurger.grid(row=2,column=1)

lblPizza=Label(f1,font=('arial',16,'bold'),text="Pizza",bd=16,anchor='w')
lblPizza.grid(row=3,column=0)
txtPizza=Entry(f1,font=('arial',16,'bold'),textvariable=Pizza,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtPizza.grid(row=3,column=1)

lblSamosa=Label(f1,font=('arial',16,'bold'),text="Samosa",bd=16,anchor='w')
lblSamosa.grid(row=4,column=0)
txtSamosa=Entry(f1,font=('arial',16,'bold'),textvariable=Samosa,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtSamosa.grid(row=4,column=1)

lblPattice=Label(f1,font=('arial',16,'bold'),text="Pattice",bd=16,anchor='w')
lblPattice.grid(row=5,column=0)
txtPattice=Entry(f1,font=('arial',16,'bold'),textvariable=Pattice,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtPattice.grid(row=5,column=1)
#================================Restro info 2==================================================
lblDrinks=Label(f1,font=('arial',16,'bold'),text="Drinks",bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtDrinks.grid(row=0,column=3)

lblCost=Label(f1,font=('arial',16,'bold'),text="Cost of Meal",bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtCost.grid(row=1,column=3)

lblService_Charge=Label(f1,font=('arial',16,'bold'),text="Service_Charge",bd=16,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge=Entry(f1,font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtService_Charge.grid(row=2,column=3)

lblTax=Label(f1,font=('arial',16,'bold'),text="State Tax",bd=16,anchor='w')
lblTax.grid(row=3,column=2)
txtTax=Entry(f1,font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtTax.grid(row=3,column=3)

lblSubTotal=Label(f1,font=('arial',16,'bold'),text="Sub Total",bd=16,anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtSubTotal.grid(row=4,column=3)

lblTotal=Label(f1,font=('arial',16,'bold'),text="Total Cost",bd=16,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,
bg="powder blue",justify='right')
txtTotal.grid(row=5,column=3)
#===================================Buttons================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="Black",font=('arial',16,'bold'),width=10,
text="Total",bg="cadet blue",command=Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="Black",font=('arial',16,'bold'),width=10,
text="Reset",bg="cadet blue",command=Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8,bd=16,fg="Black",font=('arial',16,'bold'),width=10,
text="Exit",bg="cadet blue",command=qExit).grid(row=7,column=3)


root.mainloop()