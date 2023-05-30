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

def show(L):
    print("Here is the menu: ")
    for i in range(0, len(L)):
        sandwich_list = "{}. {}, ${}".format(i+1, L[i][0], L[i][1])
        print(sandwich_list)


def modify():
    print("test text")

def review():
    print("test text")

def pay():
    print("test text")

def menu():
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
    elif answer == 'm':
        modify()
    elif answer == 'r':
        review()
    elif answer == 'p':
        pay()
    else:
        print("I didn't expect that answer.")

menu()

