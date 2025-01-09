### Vending Machine
print("Please wait...")

#-----------------------------------------------------------------------------------------------------------#
###                              ### ----- GLOBAL VARIABLES ----- ###                                     ###
#-----------------------------------------------------------------------------------------------------------#

'''
NOTES:
Variables with Capitals should be reserved for Global Variables
'''

# User Values #
Cash = 0
Money = Cash
Current = "Unassigned"
ListCurrent = "Currently idle", "Browsing the store", "Purchasing items", "At the bank"

## HUD ##

# Settings #
MXLenI, MXLenP = 15, 9
MaxLen = MXLenI
space = 0

# HUD Elements #
Blanks = " "
NewPage = "\n\n\n"
NewPage = NewPage*15
Divider = "-"
Divider = (f"""
{Divider*125}
""")

# Items #
Type = ["Drink", "Snack"]

# Maximum Characters for naming Items is [15]

Menus1 = { # Drinks
        "Regular Water"   :50,
        "Mineral Water"   :150,
        "Soda Beverage"   :100,
        "Orange Juice"    :70,
        "Apple Juice"     :75,
        "Cow Milk"        :80
        }

ItemsP1 = list(Menus1.keys())
PricesP1 = list(Menus1.values())

Menus2 = { # Snacks
        "Corn Chips"      :100,
        "Potato Chips"    :120, 
        "Sliced Bread"    :60,
        "Croissant"       :150,
        "Cholocate Bar"   :90,
        "Vanilla Bar"     :90
        }

ItemsP2 = list(Menus2.keys())
PricesP2 = list(Menus2.values())

MenuNo, Active, Action = 0, 1, 0
LastAction = 0
PrintedHUD = 1

## Functions ##

# Menu/HUD #

def HUD(type, inputs): # For displaying formats

    #--------NOTES--------#
    # 1 =                 #
    # 2 = INTERACTIONS    #
    # 3 = INFORMATION     #
    #---------------------#

    Current = ListCurrent[Action] # Update

    if type == 1: # Menu
        print(type)
    if type == 2: # Bank
        print(type)
    if type == 3: # Store
        print(f"{Divider}Money:{Cash}\n{Current}...{Divider}Vending Machine{Divider}", end=''), printStoreMenu(inputs)
        if Action == 2:
            print(f"{Divider}99[Back]\nItems Dispensed:")
        else:
            print(f"{Divider}8[Buy] 9[Deposit] 99[Back]\nItems Dispensed:")
    else:
        print("Function 'HUD' did not return from int 1-3, You may have entered out of value or a str.")

default_stock = 10

def printItemMenu(no,item,price,stock,price_,stock_): # from printStoreMenu()
    if Action == 2:
        print(f"{no}[{item}{price_}]   {price}{stock_}{stock}")
    else:
        print(f" [{item}{price_}]   {price}{stock_}{stock}")

def printStoreMenu(Num):
    print(f" Item{Blanks*16}Value    Stock")
    num, go = 0, 0

    if   Num == 1:     # Page Numbers
        ItemsNum, PricesNum, go = ItemsP1, PricesP1, 1
    elif Num == 2:
        ItemsNum, PricesNum, go = ItemsP2, PricesP2, 1
    else:
        print('Menu does not exist...'), go == 0

    if go == 1:     # Print Menu
        for item, price in zip(ItemsNum, PricesNum):
            I = MXLenI - len(item)
            P = MXLenP - len(str(price))
            I = Blanks * I
            P = Blanks * P
            printItemMenu(num,item,PricesNum[num],default_stock,I,P)
            num += 1

    if Action == 2:   
        print(f"\n6[Back] Page {Num}/2 7[Next]{Divider}")
    else:
        print(f"\n1[Back] Page {Num}/2 2[Next]{Divider}")

def Interact():
    print("Interact")


#-----------------------------------------------------------------------------------------------------------#
###                              ### ----- END OF VARIABLES ----- ###                                     ###
#-----------------------------------------------------------------------------------------------------------#


# Boot/Menu
def DasBoot():
    print(NewPage,Divider,end='')
    Current = ListCurrent[Action]
    print(f'''{Current}...{Divider}What would you like to do today?
1[Shop] 2[Withdraw/Deposit] 99[Leave]''')

DasBoot()

## CYCLE
while True: 
    try: 
        if PrintedHUD == 1:
            Input = int(input("Input:"))
        PrintedHUD = 1

        print(f"{Divider}\nDEBUG:")
        print(f"Var [Action]:{Action}")
        print(f"Var [Input]:{Input}")
        print(Divider)

        #-----------NOTES-----------#
        # 0 = Initiate Console      #
        # 1 = Browsing Shop         #
        # 2 = Buying Items          #
        # 3 = Deposit/Withdraw Cash #
        #---------------------------#

        if Action == 0:# Initiaton

            if Input == 1:
                Action = 1
            if Input == 2:
                Action = 3
                print("Withdraw/Deposit")
            if Input == 99:
                print("Terminal shut down...")
                break
            if not Input == 1 or 2 or 99:
                print("Script Broke")

            print(NewPage,Divider,end='')
            print(f'''Browsing the store...{Divider}What would you like to do today?\n1[Shop] 2[Withdraw/Deposit] 99[Leave]''')

        if Action == 1:# Browser

            if Input == 8:
                Action = 2
                HUD(3,1)
            elif Input == 9:
                Action = 3
                HUD(3,1)
            elif Input == 1 or 2:
                HUD(3,Input)
            elif not Input == 1 or 2 or 8 or 9:
                print("Input unknown")

        if Action == 2:# Buying 
            print(f"Var [Action]:{Action} 'You're in the buy menu.'")
            HUD(3,1)

        if Action == 3:# Deposit/Withdraw
            print(f"{NewPage}Please enter amount to withdraw... (Recomended:200)\nCurrent Cash:{Cash}")
            Amount = Cash + int(input("Amount:"))
            Cash, Action = Amount, LastAction
            PrintedHUD = 0
        
        LastAction = Action
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Quick tests