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
    get_sandwich = True
    while get_sandwich == True:
        get_samount = True
        get_sname = True
        get_again = True
        order_modify = input("Would you like to add or remove something from your order? a for add, r for remove: ").lower()
        if order_modify == 'a':
            show(sandwiches)
            #loop to make sure user doesn't order a sandwich not on the list.
            while get_sname == True:
                try:
                  user_choice = int(input("Please type the number of the sandwich you want: "))
                  if user_choice > len(sandwiches):
                      print("That's not a sandwich on our menu.")
                  elif user_choice <= 0:
                      print("That's not a sandwich on our menu.")
                  else:
                      get_sname = False
                except ValueError:
                    print("Please type a number.")
            #loop to make sure that the sandwich order is under 5
            while get_samount == True:

                try:
                    user_amount = int(input("How many of this sandwich do you want: "))
                    if user_amount + user_order > 5:
                        print("You may only order 5 sandwiches.")
                    elif user_amount + user_order <= 5:
                        sandwiches[user_choice][2] = sandwiches[user_choice][2] + user_amount
                        user_order += user_amount
                        get_samount = False
                        print("Thank-you for adding {} {}".format(user_amount, sandwiches[user_choice - 1][0]))
                        if user_order == 5:
                            print("As you have 5 sandwiches in your order, you shall move to the paying process.")
                            get_sandwich = False
                            get_again = False
                            pay()
                        while get_again == True:
                            again = input("Would you like to add or remove more from your order? y for yes, n for no: ")
                            if again == 'y':
                                get_sandwich = True
                                get_again = False
                            elif again == 'n':
                                get_sandwich = False
                                get_again = False
                            else:
                                print("That's not what I expected.")
                                get_again = True
                except ValueError:
                    print("Please only enter numbers.")
        #checks to see if order is at 5 sandwiches or not
        if user_order == 5:
            print("As you have 5 sandwiches in your order, you shall be moved to the paying process.")
            pay()
    #allows user to remove items from their order
        elif order_modify == 'r':
            review()
            remove = int(input("Please enter the number of the sandwich you would like to remove from your order: "))
            remove_amount = int(input("Please enter how many you would like to remove: "))
            sandwiches[remove - 1][2] = sandwiches[remove - 1][2] - remove_amount
            print("Thank-you. There are now {} {} on your order.".format(sandwiches[remove -1][2], sandwiches[remove - 1][0]))


#function that allows users to review their order
def review():
    global sandwiches
    print("Here is your order: ")
    for i in range(0, len(sandwiches)):
        if sandwiches[i][2] > 0:
            print("{}. {} {} for ${} \n".format(i+1, sandwiches[i][2], sandwiches[i][0], sandwiches[i][1]))


#function that allows users to pay for their order
def pay():
    global user_order
    cost = 0
    for i in range(0, len(sandwiches)):
        if sandwiches[i][2] > 0:
            print("- {} {} for ${} \n".format(sandwiches[i][2], sandwiches[i][0], sandwiches[i][1]))
            cost += sandwiches[i][1]*sandwiches[i][2]
        elif sandwiches[i][2] == 0:
            print("There is nothing in your order to pay for! Try again once ordering at least one sandwich.")
            return
    print("That comes to ${} total.".format(round(cost,2)))
    print("This order has been fulfilled, any sandwiches ordered now will go to a new order.")
    for i in range(0, len(sandwiches)):
        if sandwiches[i][2] > 0:
            sandwiches[i][2] = 0
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

