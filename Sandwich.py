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

past_order = []

#counting system to count how many sandwiches are being ordered
user_order = 0
#counting system that counts how many orders have been ordered
order_number = 0

def return_to_menu():
    global running_order
    get_ask = True
    while get_ask == True:
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
        get_menu = True
        order_modify = input("Would you like to add or remove something from your order? a for add, r for remove: ").lower()
        if order_modify == 'a':
            while get_menu == True:
                ask = input("Would you like to see the menu? y for yes, n for no: ").lower()
                if ask == 'y':
                    show(sandwiches)
                    get_menu = False
                elif ask == 'n':
                    get_menu = False
                else:
                    print("That wasn't an answer I was expecting. Please try again.")
                    get_menu = True
            #loop to make sure user doesn't order a sandwich not on the list.
            while get_sname == True:
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
            #loop to make sure that the sandwich order is under 5
            while get_samount == True:
                try:
                    user_amount = int(input("How many of this sandwich do you want: "))
                    if user_amount + user_order > 5:
                        print("You may only order 5 sandwiches. You are currently ordering {} sandwiches".format(user_order))
                    elif user_amount + user_order <= 5:
                        sandwiches[user_choice-1][2] = sandwiches[user_choice-1][2] + user_amount
                        user_order += user_amount
                        print("Thank-you for adding {} {}".format(sandwiches[user_choice-1][2], sandwiches[user_choice - 1][0]))
                        get_samount = False
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
                                print("That's not what I expected. Please try again.")
                                get_again = True
                except ValueError:
                    print("Please only enter numbers.")
        #checks to see if order is at 5 sandwiches or not
        elif user_order == 5:
            print("As you have 5 sandwiches in your order, you shall be moved to the paying process.")
            pay()
        #allows user to remove items from their order
        elif order_modify == 'r':
            review()
            get_remove = True
            get_remove_amount = True
            while get_remove == True:
                try:
                    remove = int(input("Please enter the number of the sandwich you would like to remove from your order: "))
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
            while get_remove_amount == True:
                try:
                    remove_amount = int(input("Please enter how many you would like to remove: "))
                    if remove_amount > sandwiches[remove - 1][2]:
                        print("You don't have that many in your order! Please try again.")
                    elif remove_amount <=0:
                        print("Please enter a number greater than 0.")
                    else:
                        sandwiches[remove - 1][2] = sandwiches[remove - 1][2] - remove_amount
                        user_order = user_order - remove_amount
                        print("Thank-you. There are now {} {} on your order.".format(sandwiches[remove -1][2], sandwiches[remove - 1][0]))
                        get_remove_amount = False
                except ValueError:
                    print("That's not a number. Try again.")
        else:
            print("That wasn't an answer I was expecting. Please try again.")


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
    global order_number
    get_user_phone = True
    get_pick_or_deliver = True
    sandwich_amount = 0
    cost = 0
    error_phone = "That doesn't look like a viable phone number. A phone number should be between 7 and 10 numbers. Please try again."
    if user_order == 0:
        print("You haven't ordered any sandwiches! Please place an order before trying to pay.")
        return
    user_name = input("What is the name you would like to put this order under? : ")
    while get_user_phone == True:
        try:
            user_phone = int(input("What is the phone number you would like to place this order under? Please exclude the +64: "))
            list_of_digits = [int(i) for i in str(user_phone)]
           # print(list_of_digits)
            if len(list_of_digits) < 7:
                print(error_phone)
            elif len(list_of_digits) > 11:
                print(error_phone)
            else:
                print("Thank you for entering your number.")
                get_user_phone = False
        except ValueError:
            print("Please only type numbers. Try again.")

    for i in range(0, len(sandwiches)):
        if sandwiches[i][2] > 0:
            print("- {} {} for ${} \n".format(sandwiches[i][2], sandwiches[i][0], sandwiches[i][1]))
            cost += sandwiches[i][1]*sandwiches[i][2]
            sandwich_amount += sandwiches[i][2]

    print("Thank-you {} for placing your order,".format(user_name))
    print("That comes to ${} total.".format(round(cost,2)))
    order_number += 1
    while get_pick_or_deliver == True:
        pick_or_deliver = input("Would you like to pick up your order, or have it delivered? There is a $3 delivery fee. p for pick up, d for delivery: ")
        if pick_or_deliver == 'p':
            print("Thank-you for your order. Your order is order #{}, and should take about {} minutes.".format(order_number, sandwich_amount * 10))
            print("We will call you on this number when your order is complete: {}".format(user_phone))
            get_pick_or_deliver = False
        elif pick_or_deliver == 'd':
            address = input("Please input your address here: ")
            cost += 3
            print("Thank-you {}. Your order is order number {}. The total now comes to ${}".format(user_name, order_number, cost))
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

#function that allows users to choose what they want to do
def menu():
    global running_order
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
    """
    lines = "-"*59
    print(lines)
    print(welcome_message)
    print(lines)
    while get_user_input == True:
        answer = input("What would you like to do: ").lower()
        if answer == 's':
            show(sandwiches)
            get_user_input = False
            return_to_menu()
        elif answer == 'm':
            modify()
            get_user_input = False
            return_to_menu()
        elif answer == 'r':
            review()
            get_user_input = False
            return_to_menu()
        elif answer == 'p':
            pay()
            get_user_input = False
            return_to_menu()
        elif answer == 'a':
            running_order = False
            get_user_input = False
            print("Thank-you for using our services.")
        else:
            print("I didn't expect that answer. Try again.")

#running the program
while running_order == True:
    menu()

