from tkinter import *
bisque_Mug_amount = 0
        
Bisque_Santa_ornament_amount=0

bisque_Elephant_monkey_box_amount = 0


Bisque_Sitting_puppy_ornament_amount=0


BiskqueStarfish_amount=0
root = Tk()
# creating title and window
root.title("clay guild app")
root.geometry("1200x800")
# creating input box
Input = Entry(root, width=100)
Input.pack()
Input.get()  # gets what is entered into input box


# making the search button
def searchButtonClick():
    if Input.get() == "Steve":
        top = Toplevel()  # creates new window and sets size
        top.geometry("1200x800")
        orderLabel = Label(top, text="Order here", font="32")
        orderLabel.place(x=100, y=100)

        order_Basket_label=Label(top,text = "Basket",font = "32")
        order_Basket_label.place(x=900,y=100)


        titleLabel = Label(top, text="Order and order history screen", font="64")
        titleLabel.place(x=550, y=0)

        #Creating Basket labels
        BisqueMug_order = Label(top, text=str(bisque_Mug_amount)+"xBisque Mug-£3.30", font=32)
        BisqueMug_order.place(x=900, y=150)

        Bisque_Santa_ornament_order = Label(top, text=str(Bisque_Santa_ornament_amount)+"xBisque santa ornament-£1.68", font=32)
        Bisque_Santa_ornament_order.place(x=900, y=200)

        Bisque_Elephant_monkey_box_order = Label(top, text=str(bisque_Elephant_monkey_box_amount)+"xBisque elephant money box-£6.96", font=32)
        Bisque_Elephant_monkey_box_order.place(x=900, y=250)

        Bisque_Sitting_puppy_ornament = Label(top, text=str(Bisque_Sitting_puppy_ornament_amount)+"xBisque sitting puppy ornament-£2.40", font=32)
        Bisque_Sitting_puppy_ornament.place(x=900, y=300)
        global BisqueStarfish_order
        BisqueStarfish_order= Label(top, text=str(BiskqueStarfish_amount)+"xBisque starfish-£4.96", font=32)
        BisqueStarfish_order.place(x=900, y=350)

        def BisqueMug_click():
            global bisque_Mug_amount
            bisque_Mug_amount += 1
            BisqueMug_order.config(text=str(bisque_Mug_amount)+"xBisque Mug-£3.30")


        def Bisque_Santa_ornament_click():
            global Bisque_Santa_ornament_amount
            Bisque_Santa_ornament_amount += 1
            Bisque_Santa_ornament_order.config(text=str(Bisque_Santa_ornament_amount)+"xBisque santa ornament-£1.68")

        def bisque_Elephant_monkey_box_click():
            global bisque_Elephant_monkey_box_amount
            bisque_Elephant_monkey_box_amount += 1
            Bisque_Elephant_monkey_box_order.config(text=str(bisque_Elephant_monkey_box_amount)+"xBisque elephant money box-£6.96")
        
        def Bisque_Sitting_puppy_ornament_click():
            global Bisque_Sitting_puppy_ornament_amount
            Bisque_Sitting_puppy_ornament_amount += 1
            Bisque_Sitting_puppy_ornament.config(text=str(Bisque_Sitting_puppy_ornament_amount)+"xBisque sitting puppy ornament-£2.40")

        def BisqueStarfish_click():
            global BiskqueStarfish_amount
            BiskqueStarfish_amount += 1
            BisqueStarfish_order.config(text= str(BiskqueStarfish_amount)+"xBisque starfish-£4.96")

        # Creating order buttons
        biskqueMug = Button(top, text="Bisque Mug-£3.30 plus VAT-PT21234", command=BisqueMug_click)
        biskqueMug.place(x=100, y=150)

        biskque_Santa_ornament = Button(top, text="Bisque santa ornament-£1.68 plus VAT-PT32676 ",command=Bisque_Santa_ornament_click)
        biskque_Santa_ornament.place(x=100, y=200)

        biskque_Elephant_money_box = Button(top, text="Bisque Elephant monkey box-£6.96 plus VAT-PTH042 ",command=bisque_Elephant_monkey_box_click)
        biskque_Elephant_money_box.place(x=100, y=250)

        biskque_Sitting_puppy_ornament = Button(top, text="Bisque sitting puppy ornament-£2.40 plus VAT-PT21444 ",command=Bisque_Sitting_puppy_ornament_click)
        biskque_Sitting_puppy_ornament.place(x=100, y=300)
  
        biskqueStarfish = Button(top, text="Bisque starfish-£4.96 plus VAT-PT37485 ", command=BisqueStarfish_click)
        biskqueStarfish.place(x=100, y=350)

        top and root.mainloop()





searchButton = Button(root, text="login", padx="50", command=searchButtonClick)  # root= 1st window
searchButton.pack()

# creating mainloop
root.mainloop()