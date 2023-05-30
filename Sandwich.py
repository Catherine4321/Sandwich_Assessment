#when this is true, it keeps the program running in a loop
running_order = True
#list of sandwiches customers can buy
sandwiches = [["Halloumi and Apricot Jam", 15.95, 0],
                  ["Banh Mi With Five-Spice Crispy Pork Belly, Pickled Carrot, Chilli, Coriander and Cucumber", 18.95, 0],
                  ["Roasted Beetroot, Carrot, Spiced Nuts and Whipped Feta", 15.95, 0],
                  ["Sausage and Egg", 14.95, 0],
                  ["Smoked Salmon Deluxe", 15.95, 0],
                  ["Ham Sandwich in a French Baguette", 16.95, 0],
                  ["Kiwi and Roo's 'Lucky Beef' Steak Sandwich", 18.95, 0],
                  ["Buttermilk Chicken, Scotch Bonnet Jam, Pickled Cabbage and Crispy Shallots", 18.95, 0],
                  ["Balik Ekmek - Griddled Mackerel in a Baguette With Tomato, Lettuce, Onion, Chilli and Sumac", 18.95, 0],
                  ["Milanese and Gremolata Panini", 16.95, 0],
                  ["Fish Finger Sandwich With Nordic Dill Salsa", 15.95, 0],
                  ["Grilled Cheddar and Jalapeño Popper Sandwich", 15.95, 0]]

#counting system to count how many sandwiches are being ordered
user_order = 0

def return_to_menu():
    global running_order
    ask = input("would you like to go back to the menu? y for yes, n for no: ")
    if ask == 'y':
        running_order = True
    elif ask == 'n':
        running_order = False
        print("Thank-you for using our system.")

#function that shows sandwich menu
def show(L):
    print("Here is the menu: ")
    for i in range(0, len(L)):
        sandwich_list = "{}. {}, ${}".format(i+1, L[i][0], L[i][1])
        print(sandwich_list)

#function that allows users to add or remove sandwiches from their order
def modify():
    global sandwiches
    global user_order
    order_modify = input("Would you like to add or remove something from your order? a for add, r for remove: ").lower()
    if order_modify == 'a':
        show(sandwiches)
        user_choice = int(input("Please type the number of the sandwich you want: "))
        user_amount = int(input("How many of this sandwich do you want: "))
        sandwiches[user_choice][2] = sandwiches[user_choice][2] + user_amount
        print("Thank-you for adding {}".format(sandwiches[user_choice-1][0]))
        user_order += user_amount
        #I plan to allow the user to remove an item from their order list
        #I shall do this below


#function that allows users to review their order
def review():
    print("test text")

#function that allows users to pay for their order
def pay():
    global user_order
    cost = 0
    for i in range(0, len(sandwiches)):
        if sandwiches[i][2] > 0:
            print("- {} {} for ${} \n".format(sandwiches[i][2], sandwiches[i][0], sandwiches[i][1]))
            cost += sandwiches[i][1]*sandwiches[i][2]
    print("That comes to ${} total.".format(round(cost,2)))
    user_order = 0

#function that allows users to choose what they want to do
def menu():
    global running_order
    welcome_message = """
Welcome to Marsden Gourmet Sandwich Bar's online ordering system.
We only sell 5 sandwiches per customer.
Please select which option you would like to do from below:
-----------------------------------------------------------
s) Show menu of sandwiches for sale
m) Modify order
r) Review order
p) Pay for order
a) Abandon order
    """
    lines = "-"*59
    print(lines)
    print(welcome_message)
    print(lines)
    answer = input("What would you like to do: ").lower()
    if answer == 's':
        show(sandwiches)
        return_to_menu()
    elif answer == 'm':
        modify()
        return_to_menu()
    elif answer == 'r':
        review()
        return_to_menu()
    elif answer == 'p':
        pay()
        return_to_menu()
    elif answer == 'a':
        running_order = False
        print("Thank-you for using our services.")
    else:
        print("I didn't expect that answer.")

#running the program
while running_order == True:
    menu()

