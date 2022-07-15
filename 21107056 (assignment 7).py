# Question 1
# import all functions/classes from the tkinter   

from tkinter import *
  
# Function for finding GST rate
def findGst():
  
    # take a value from the respective entry boxes
    # get method returns current text as string
    org_cost= int(org_priceField.get())
     
    N_price = int(net_priceField.get())
  
    # calculate GST rate
    gst_rate = ((N_price - org_cost) * 100) / org_cost
  
    # insert method inserting the  
    # value in the text entry box.
    gst_rateField.insert(10, str(gst_rate) + " % ")
    
      
# Function for clearing the  
# contents of all text entry boxes
def clearAll():
      
      
    # deleting the content from the entry box
    org_priceField.delete(0, END)
      
    net_priceField.delete(0, END)
      
    gst_rateField.delete(0, END)
      
  
# Driver Code
if __name__ == "__main__":
  
    # Create a GUI window
    gui = Tk()
    
    # Set the background colour of GUI window  
    gui.configure(background = "light green")
    
    # set the name of tkinter GUI window 
    gui.title("GST Rate Finder")
    
    # Set the configuration of GUI window
    gui.geometry("300x300")
  
    # Create a Original Price: label 
    org_price = Label(gui, text = "Original Price",
                      bg = "blue")
    
    # Create a Net Price : label
    net_price = Label(gui, text = "Net Price",
                      bg = "blue")
  
    # Create a Find Button and attached to
    # findGst function
    find = Button(gui, text = "Find", fg = "Black",
                  bg = "Red",
                  command = findGst)
      
    # Create a Gst Rate : label 
    gst_rate = Label(gui, text = "Gst Rate", bg = "blue")
  
    # Create a Clear Button and attached to
    # clearAll function
    clear = Button(gui, text = "Clear", fg = "Black",
                   bg = "Red",
                   command = clearAll)
  
    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure .
  
    # padx attributed provide x-axis margin 
    # from the root window to the widget.
  
    # pady attributed provide y-axis
    # margin from the widget.
    org_price.grid(row = 1, column = 1,padx = 10,pady = 10)
                   
    net_price.grid(row = 2, column = 1, padx = 10, pady = 10)
     
    find.grid(row = 3, column = 2,padx = 10,pady = 10)
      
    gst_rate.grid(row = 4, column = 1,padx = 10, pady = 10)
      
    clear.grid(row = 5, column = 2, padx = 10, pady = 10)
  
    # Create a text entry box for filling or typing the information.  
    org_priceField = Entry(gui)
      
    net_priceField = Entry(gui)
      
    gst_rateField = Entry(gui)
  
    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure .
    org_priceField.grid(row = 1, column = 2 ,padx = 10,pady = 10)
      
    net_priceField.grid(row = 2, column = 2, padx = 10,pady = 10)
      
    gst_rateField.grid(row = 4, column = 2, padx = 10,pady = 10)
      
    # Start the GUI
    gui.mainloop()


# Question 2
# import all methods and classes from the tkinter  
from tkinter import *
 
# import calendar module
import calendar
 
# Function for showing the calendar of the given year
def showCal():
 
    # Create a GUI window
    new_gui = Tk()
     
    # Set the background colour of GUI window
    new_gui.config(background = "white")
 
    # set the name of tkinter GUI window
    new_gui.title("CALENDAR")
 
    # Set the configuration of GUI window
    new_gui.geometry("550x600")
 
    # get method returns current text as string
    fetch_year = int(year_field.get())
 
    # calendar method of calendar module return
    # the calendar of the given year .
    cal_content = calendar.calendar(fetch_year)
 
    # Create a label for showing the content of the calendar
    cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal_year.grid(row = 5, column = 1, padx = 20)
     
    # start the GUI
    new_gui.mainloop()
 
     
# Driver Code
if __name__ == "__main__" :
 
    # Create a GUI window
    gui = Tk()
     
    # Set the background colour of GUI window
    gui.config(background = "white")
 
    # set the name of tkinter GUI window
    gui.title("CALENDAR")
 
    # Set the configuration of GUI window
    gui.geometry("250x140")
 
    # Create a CALENDAR : label with specified font and size
    cal = Label(gui, text = "CALENDAR", bg = "dark gray",
                            font = ("times", 28, 'bold'))
 
    # Create a Enter Year : label
    year = Label(gui, text = "Enter Year", bg = "light green")
     
    # Create a text entry box for filling or typing the information. 
    year_field = Entry(gui)
 
    # Create a Show Calendar Button and attached to showCal function
    Show = Button(gui, text = "Show Calendar", fg = "Black",
                              bg = "Red", command = showCal)
 
    # Create a Exit Button and attached to exit function
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
     
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(row = 1, column = 1)
 
    year.grid(row = 2, column = 1)
 
    year_field.grid(row = 3, column = 1)
 
    Show.grid(row = 4, column = 1)
 
    Exit.grid(row = 6, column = 1)
     
    # start the GUI
    gui.mainloop()


# Question 3
# Python program to create a simple GUI
# calculator using Tkinter
 
# import everything from tkinter module
from tkinter import *
 
# globally declare the expression variable
expression = ""
 
 
# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
 
 
# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""
 
 
# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
 
    # set the background colour of GUI window
    gui.configure(background="light green")
 
    # set the title of GUI window
    gui.title("Simple Calculator")
 
    # set the configuration of GUI window
    gui.geometry("270x150")
 
    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()
 
    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)
 
    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='red',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='red',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='red',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='red',
                command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='red',
                command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='black', bg='red',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()

# Question 4
# Function to find the partition position
def partition(lst_to_sort, low, high):
  
  # Choose the rightmost element as pivot
  pivot = lst_to_sort[high]
  
  # Pointer for greater element
  i = low - 1
  
  # Traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if lst_to_sort[j] <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
  
      # Swapping element at i with element at j
      (lst_to_sort[i], lst_to_sort[j]) = (lst_to_sort[j], lst_to_sort[i])
  
  # Swap the pivot element with the greater element specified by i
  (lst_to_sort[i + 1], lst_to_sort[high]) = (lst_to_sort[high], lst_to_sort[i + 1])
  
  # Return the position from where partition is done
  return i + 1
  
# Function to perform quicksort
def quick_sort(lst_to_sort, low, high):
  if low < high:
  
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(lst_to_sort, low, high)
  
    # Recursive call on the left of pivot
    quick_sort(lst_to_sort, low, pi - 1)
  
    # Recursive call on the right of pivot
    quick_sort(lst_to_sort, pi + 1, high)
  
    
          
# Driver code
input_str = input("Enter marks separated by space: ")
lst = list(input_str.split(" "))
lst_to_sort = [int(i) for i in lst]
quick_sort(lst_to_sort, 0, len(lst_to_sort) - 1)
  
print(f'Sorted array: {lst_to_sort}')


# Question 5

def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
  
# Driver code to test above
input_str = input("Enter integers separated by space (including duplicates): ")
lst = list(input_str.split(" "))
array = [int(i) for i in lst]
bubbleSort(array)
  
print("Sorted array is:")
print('[', end = " ")
for i in range(len(array)):
    print("%d" % array[i], end=" ")
print("]")
print("")


# if x is present in arr[] then 
# returns the count of occurrences
# of x, otherwise returns -1. 
def count(arr, x, n):
  
    # get the index of first
    # occurrence of x 
    i = first(arr, 0, n-1, x, n)
   
    # If x doesn't exist in 
    # arr[] then return -1 
    if i == -1:
        return "error: The given no. doesn't exist in the list."
      
    # Else get the index of last occurrence
    # of x. Note that we are only looking
    # in the subarray after first occurrence   
    j = last(arr, i, n-1, x, n);     
      
    # return count 
    return j-i+1
  
# if x is present in arr[] then return
# the index of FIRST occurrence of x in
# arr[0..n-1], otherwise returns -1 
def first(arr, low, high, x, n):
    if high >= low:
  
        # low + (high - low)/2
        mid = (low + high)//2      
          
        if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        else:
            return first(arr, low, (mid -1), x, n)
    return -1
   
# if x is present in arr[] then return
# the index of LAST occurrence of x 
# in arr[0..n-1], otherwise returns -1 
def last(arr, low, high, x, n):
    if high >= low:
  
        # low + (high - low)/2
        mid = (low + high)//2; 
   
        if(mid == n-1 or x < arr[mid+1]) and arr[mid] == x :
            return mid
        elif x < arr[mid]:
            return last(arr, low, (mid -1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)     
    return -1
  
# driver program to test above functions 
x = int(input("Enter the integer whose no. of occurrences is to be counted: "))  # Element to be counted in array[]
n = len(array)
c = count(array, x, n)
print(f"No. of occurrences of element {x} is: {c}")

# Question 6

# Python code to remove duplicate elements
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
     
# Driver Code
input_str = input("Enter integers separated by space (including duplicates): ")
lst = list(input_str.split(" "))
array = [int(i) for i in lst]
print(Remove(array))
array = Remove(array)

# Python program for implementation of Bubble Sort
 
def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
 
 
# Driver code to test above

 
bubbleSort(array)
 
print("Sorted array (using bubble sort) is: ")
print("[", end = " ")
for i in range(len(array)):
    print("% d" % array[i], end=" ")
print("]")

def selection_sort(array):  
    length = len(array)  
      
    for i in range(length-1):  
        minIndex = i  
          
        for j in range(i+1, length):  
            if array[j]<array[minIndex]:  
                minIndex = j  
                  
        array[i], array[minIndex] = array[minIndex], array[i]  
          
          
    return array      
  
print("The sorted array (using selection sort) is: ", selection_sort(array))  