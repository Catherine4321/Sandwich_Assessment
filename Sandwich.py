"""This program is meant to allow a user to order sandwiches online."""
# when this is true, it keeps the program running in a loop
running_order = True
# list of sandwiches customers can buy
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
# list that could store previous orders
# past_order = []

# counting system to count how many sandwiches are being ordered
user_order = 0
# counting system that counts how many orders have been ordered
order_number = 0


# function that checks if user wants to return to menu
def return_to_menu():
    """Allow the user to return to the main menu."""
    global running_order
    get_ask = True
    # loop that validates user's response
    while get_ask is True:
        ask = input("would you like to go back to the menu? y for yes, n for no: ")
        if ask == 'y':
            running_order = True
            get_ask = False
        elif ask == 'n':
            if user_order > 0:
                pay()
                print("Thank you for using our system.")
            else:
                print("Thank-you for using our system.")
            running_order = False
            get_ask = False
        else:
            print("That's not an answer I was expecting. Please try again.")


# function that shows sandwich menu
def show(m):
    """Show the sandwich menu to the user."""
    print("Here is the menu: ")
    for i in range(0, len(m)):
        sandwich_list = "{}. {}, ${}".format(i+1, m[i][0], m[i][1])
        print(sandwich_list)


# function that allows users to add or remove sandwiches from their order
def modify():
    """Allow the user to add or remove sandwiches from their order."""
    global sandwiches
    global user_order
    get_sandwich = True
    while get_sandwich is True:
        get_samount = True
        get_sname = True
        get_again = True
        get_menu = True
        modify_text = "Would you like to add or remove something from your order? a for add, r for remove: "
        order_modify = input(modify_text).lower()
        # loop to check if user wants to see the menu
        if order_modify == 'a':
            while get_menu is True:
                ask = input("Would you like to see the menu? y for yes, n for no: ").lower()
                if ask == 'y':
                    show(sandwiches)
                    get_menu = False
                elif ask == 'n':
                    get_menu = False
                else:
                    print("That wasn't an answer I was expecting. Please try again.")
                    get_menu = True
            # loop to make sure user doesn't order a sandwich not on the list.
            user_choice = 0
            while get_sname is True:
                try:
                    user_choice = int(input("Please type the number of the sandwich you want: "))
                    if user_choice > len(sandwiches):
                        print("That's not a sandwich on our menu. Please try again.")
                    elif user_choice <= 0:
                        print("That's not a sandwich on our menu. Please try again.")
                    else:
                        get_sname = False
                except ValueError:
                    print("Please type a number.")
            # loop to make sure that the sandwich order is under 5
            while get_samount is True:
                try:
                    user_amount = int(input("How many of this sandwich do you want: "))
                    if user_amount + user_order > 5:
                        only_5 = "You may only order 5 sandwiches. You are currently ordering {} sandwiches"
                        print(only_5.format(user_order))
                    elif user_amount <= 0:
                        print("Please do not add less than 0 sandwiches.")
                    elif user_amount + user_order <= 5:
                        sandwiches[user_choice-1][2] = sandwiches[user_choice-1][2] + user_amount
                        user_order += user_amount
                        adding_message = "Thank-you for adding {} {}"
                        print(adding_message.format(sandwiches[user_choice-1][2], sandwiches[user_choice - 1][0]))
                        get_samount = False
                        if user_order == 5:
                            print("As you have 5 sandwiches in your order, you shall move to the paying process.")
                            get_sandwich = False
                            get_again = False
                            pay()
                        while get_again is True:
                            again = input("Would you like to add or remove more from your order? y for yes, n for no: ")
                            if again == 'y':
                                get_sandwich = True
                                get_again = False
                            elif again == 'n':
                                get_sandwich = False
                                get_again = False
                            else:
                                print("That's not what I expected. Please try again.")
                                get_again = True
                except ValueError:
                    print("Please only enter numbers.")
        # checks to see if order is at 5 sandwiches or not
        elif user_order == 5:
            print("As you have 5 sandwiches in your order, you shall be moved to the paying process.")
            pay()
        # allows user to remove items from their order
        elif order_modify == 'r':
            get_remove = True
            get_remove_amount = True
            if user_order == 0:
                print("There's nothing in your order! Try again when you've added something to your order!")
                return
            review()
            # loop that validates user input to make sure sandwich can be removed from order
            remove = 0
            while get_remove is True:
                try:
                    remove_text = "Please enter the number of the sandwich you would like to remove from your order: "
                    remove = int(input(remove_text))
                    if sandwiches[remove - 1][2] == 0:
                        print("You haven't ordered any of this sandwich. Please try again.")
                    elif remove > len(sandwiches) + 1:
                        print("That isn't a sandwich on the menu. Please try again.")
                    elif remove <= 0:
                        print("That's not a sandwich on the menu. Please try again.")
                    else:
                        get_remove = False
                except ValueError:
                    print("Please only type numbers. Try again.")
            # loop that makes sure that user doesn't try to remove more or less sandwiches than they have in their order
            while get_remove_amount is True:
                try:
                    remove_amount = int(input("Please enter how many you would like to remove: "))
                    if remove_amount > sandwiches[remove - 1][2]:
                        print("You don't have that many in your order! Please try again.")
                    elif remove_amount <= 0:
                        print("Please enter a number greater than 0.")
                    else:
                        sandwiches[remove - 1][2] = sandwiches[remove - 1][2] - remove_amount
                        user_order = user_order - remove_amount
                        thanks_text = "Thank-you. There are now {} {} on your order."
                        print(thanks_text.format(sandwiches[remove - 1][2], sandwiches[remove - 1][0]))
                        get_remove_amount = False
                except ValueError:
                    print("That's not a number. Try again.")
        else:
            print("That wasn't an answer I was expecting. Please try again.")


# function that allows users to review their order
def review():
    """Allow the user to look at what sandwiches they are ordering."""
    global sandwiches
    global user_order
    if user_order == 0:
        print("There's nothing in your order!")
    else:
        print("Here is your order: ")
        for i in range(0, len(sandwiches)):
            if sandwiches[i][2] > 0:
                print("{}. {} {} for ${} \n".format(i+1, sandwiches[i][2], sandwiches[i][0], sandwiches[i][1]))


# function that allows users to pay for their order
def pay():
    """Allow the user to pay."""
    global user_order
    global order_number
    get_user_phone = True
    get_pick_or_deliver = True
    sandwich_amount = 0
    cost = 0
    error_phone = "A phone number should be between 7 and 11 numbers. Please try again."
    if user_order == 0:
        print("You haven't ordered any sandwiches! Please place an order before trying to pay.")
        return
    user_name = input("What is the name you would like to put this order under? : ")
    # loop that validates the user's phone number
    user_phone = 0
    while get_user_phone is True:
        try:
            what_phone = "What phone number you would like to place this order under? Please exclude the +64: "
            user_phone = int(input(what_phone))
            list_of_digits = [int(i) for i in str(user_phone)]
            if len(list_of_digits) < 7:
                print(error_phone)
            elif len(list_of_digits) > 11:
                print(error_phone)
            else:
                print("Thank you for entering your number.")
                get_user_phone = False
        except ValueError:
            print("Please only type numbers. Try again.")
    # prints out the user's order and cost of each sandwich
    for i in range(0, len(sandwiches)):
        if sandwiches[i][2] > 0:
            print("- {} {} for ${} \n".format(sandwiches[i][2], sandwiches[i][0], sandwiches[i][1]))
            cost += sandwiches[i][1]*sandwiches[i][2]
            sandwich_amount += sandwiches[i][2]
    print("Thank-you {} for placing your order,".format(user_name))
    print("That comes to ${} total.".format(round(cost, 2)))
    order_number += 1
    # loop that validates if the user would like to have their order picked up or delivered
    while get_pick_or_deliver is True:
        pick_or_deliver = input("Pick up or delivery? There is a $3 delivery fee. p for pick up, d for delivery: ")
        if pick_or_deliver == 'p':
            time_taken = "Thank-you. Your order is order #{}, and should take about {} minutes."
            print(time_taken.format(order_number, sandwich_amount * 10))
            print("We will call you on this number when your order is complete: {}".format(user_phone))
            get_pick_or_deliver = False
        elif pick_or_deliver == 'd':
            address = input("Please input your address here: ")
            cost += 3
            total_text = "Thank-you {}. Your order is order #{}. The total now comes to ${}"
            print(total_text.format(user_name, order_number, round(cost, 2)))
            print("Your order should be delivered to {} in {} minutes.".format(address, (sandwich_amount + 1) * 10))
            print("If there any issues with your order, we will call this number: {}".format(user_phone))
            get_pick_or_deliver = False
        else:
            print("That wasn't an answer I was expecting. Please try again.")
    print("This order has been fulfilled, any sandwiches ordered now will go to a new order.")
    for i in range(0, len(sandwiches)-1):
        if sandwiches[i][2] > 0:
            sandwiches[i][2] = 0
    user_order = 0


# function that lets user abandon their current order
def abandon():
    """Allow the user to abandon current order"""
    global user_order
    global order_number
    # code that removes all sandwiches from order
    for i in range(0, len(sandwiches) - 1):
        if sandwiches[i][2] > 0:
            sandwiches[i][2] = 0
    # code that resets counter that counts how many sandwiches in order
    user_order = 0
    # line that adds 1 to the order number
    order_number += 1
    print("All sandwiches added to the order now are on a new order.")


# function that allows users to choose what they want to do
def menu():
    """Allow the user to see a list of possible actions for this program."""
    global running_order
    global user_order
    global order_number
    get_user_input = True
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
q) Quit program
    """
    lines = "-"*59
    # loop that validates the user's answer to what they would like to do
    while get_user_input is True:
        print(lines)
        print(welcome_message)
        print(lines)
        answer = input("What would you like to do: ").lower()
        if answer == 's':
            show(sandwiches)
            return_to_menu()
            get_user_input = False
        elif answer == 'm':
            modify()
            return_to_menu()
            get_user_input = False
        elif answer == 'r':
            review()
            return_to_menu()
            get_user_input = False
        elif answer == 'p':
            pay()
            return_to_menu()
            get_user_input = False
        elif answer == 'a':
            abandon()
            return_to_menu()
            get_user_input = False
        elif answer == 'q':
            print("Thank-you for using our services. No sandwiches have been purchased.")
            running_order = False
            get_user_input = False
        else:
            print("I didn't expect that answer. Try again.")


# running the program
while running_order is True:
    menu()
