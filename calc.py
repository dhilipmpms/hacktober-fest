#a Gui program for calculator using tkinter
from tkinter import*

#Tkinter container
root = Tk()
root.geometry("390x280")

#this resizable is used for resizing the windows
root.title("CALCULATOR")    

expression = ""
def btn_click(item,input_text):
    """ this function is used for getting the input from the user """
    global expression 
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear(input_text):
    """ this function is used for clearing the screen """
    global expression 
    expression = ""
    input_text.set("")

def btn_equal(input_text):
    """ this function is used for calculating purpose """
    
    try:
        global expression 
        #eval()fuction calculates the expression directly
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        print("invalid format")
        expression = ""

#StringVar()is used for get the instance of the input field
input_text = StringVar()
input_field = Entry(root, textvariable = input_text)
input_field.place(height = 100)

#this set of code is for arrangement of the widgets
input_field.grid(columnspan = 4,ipadx = 100, ipady = 5)

"""remainder of this session defines the button widgets arranged in 4 rows
within the Frame widget.we position the buttons using grid()Layout Manager.
Each button has an event that can be triggered with a mouse action 
configured in the previous section E.g: btn_click() """

#first row includes two buttons ,'Clear(Clear)'and 'Divide(/)':
clear = Button(root,text = "Clear", fg = "black", width = 7, height = 2,
        bd = 0, bg = "white",
        command = lambda: btn_clear(input_text)).grid(row = 5, column = 2)
divide = Button (root, text = "/", fg = "black", width = 7, height = 2,
        bd = 0, bg = "white",  
        command = lambda: btn_click("/",input_text)).grid(row = 4, column = 1)

#second row includes 4buttons,'7','8','9' and multiply(*)
seven = Button(root, text = "7", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda: btn_click("7",input_text)).grid(row = 1, column = 0) 

eight = Button(root, text = "8", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda: btn_click("8",input_text)).grid(row = 1, column = 1)

nine = Button(root, text = "9", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda: btn_click("9",input_text)).grid(row = 1, column = 2)

multiply = Button(root, text = "*", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda:btn_click("*",input_text)).grid(row = 1, column = 3)

#third row includes 4buttons, '4','5','6' and 'subract(-)'
four = Button(root, text = "4", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white",
        command = lambda:btn_click("4",input_text)).grid(row = 2, column = 0)

five = Button(root, text = "5", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white",
        command = lambda:btn_click("5",input_text)).grid(row = 2, column = 1)

six = Button(root, text = "6", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda:btn_click("6",input_text)).grid(row = 2, column = 2)
                
subract = Button(root, text = "-", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda:btn_click("-",input_text)).grid(row = 2, column = 3)

#fourth row includes 4 Buttons,'1','2','3' and 'addition(+)'
one = Button(root, text = "1", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda:btn_click("1",input_text)).grid(row = 3, column = 0)
                
two = Button(root, text = "2", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda:btn_click("2",input_text)).grid(row = 3, column = 1)
            
three = Button(root, text = "3", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda:btn_click("3",input_text)).grid(row = 3, column = 2)

addition = Button(root, text = "+", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white",
        command = lambda:btn_click("+",input_text)).grid(row = 3,column = 3)

#five row includes 4
zero = Button(root, text = "o", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda:btn_click("0",input_text)).grid(row = 4, column = 0)
                

point = Button(root, text = ".", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white", 
        command = lambda:btn_click(".",input_text)).grid(row = 4, column = 2)
                
equal = Button(root, text = "=", fg = "black", width = 7,
        height = 2, bd = 0, bg = "white",
        command = lambda:btn_equal(input_text)).grid(row = 4, column = 3)
                



root.mainloop()
