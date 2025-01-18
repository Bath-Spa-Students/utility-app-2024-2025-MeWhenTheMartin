#-----------------------------------------------------------------------------------------------------------#
###                              ### ----- VENDING  MACHINE ----- ###                                     ###
#-----------------------------------------------------------------------------------------------------------#

## Vending Machine for Code Lab (Y1 Group 2) Assesment 2
# Coded by Martin

print(f"Please wait...\nWe are preparing shortly...")

#-----------------------------------------------------------------------------------------------------------#
###                              ### ----- GLOBAL VARIABLES ----- ###                                     ###
#-----------------------------------------------------------------------------------------------------------#

'''
NOTES:
Variables with Capitals should be reserved for Global Variables.
--
Do NOT declare a "local variable" outside of the while true loop.
'''

# User Values #
Cash = 0
Money = Cash
Current = "Currently idle"
ListCurrent = "Currently idle", "Browsing the store", "Purchasing items", "At the bank"

## HUD ##

# Settings #
MXLenI, MXLenP = 15, 9
MaxLen = MXLenI
space = 0

# HUD Elements #
Blanks = " "
NewPage = "\n\n\n"
NewPage = NewPage*15 # 45 lines long
Divider = "-"
Divider = (f"""
{Divider*125}
""")

# Items #

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

ItemsList = []

Action = 0

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
        print(f"{NewPage}{Divider}Money:{Cash}\n{Current}...{Divider}Vending Machine{Divider}", end=''), printStoreMenu(inputs)
        if Action == 2:
            print(f"{Divider}99[Back]\nItems Dispensed:{ItemsList}")
        else:
            print(f"{Divider}8[Buy] 9[Withdraw]\nItems Dispensed:{ItemsList}")
    else:
        print("Function 'HUD' did not return 'type' from int 1-3, You may have entered out a value or a str.")

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


def Purchause(Input): # Old Function used for reference...
    if Input < len(PricesP1):

        Pge = 101
        if PageNumL == 1:
            if Input == PricesP1[Input]:
                print(f"Price:{PricesP1[Input]}")
            else:
                print(f"Could not get price. Item did not match list. Price:{PricesP1[Input]}")
                Cash + PricesP1[Input]
        elif PageNumL == 2:
            if Input == PricesP2[Input]:
                print(f"Price:{PricesP1[Input]}")
            else:
                print(f"Could not get price. Item did not match list. Price:{PricesP1[Input]}")
        else:
            print(f"This can't, purchause failed. (PageNum:{PageNumL}/Input:{Input}/Price:{Pge}/Len:{len(PricesP1)})")

    else:
        print("Halted, over the list's 'page' length...")
    
    #print(f"(PageNum:{PageNum}/Input:{Input}/Price:{Pge}/Len:{len(PricesP1)})")



#-----------------------------------------------------------------------------------------------------------#
###                              ### ----- END OF VARIABLES ----- ###                                     ###
#-----------------------------------------------------------------------------------------------------------#

# Quick Access Variables
DebugMode = 0
Input = 495
PageNum = 1
Cash = 2000 

# Boot/Menu - Run once only
def DasBoot():
    print(NewPage,Divider,end='')
    Current = ListCurrent[Action]
    print(f'''{Current}...{Divider}What would you like to do today?
1[Shop] 2[Withdraw/Deposit] 99[Leave]''')
DasBoot()

#-----------------------------------------------------------------------------------------------------------#

# Loop > State > Input > Output

while True: 
    try: 

        if not Action == 3:
            LastAction = Action
        PrintedHUD = 99

        if not Action == 2:
            if Input == 1 or 2:
                PageNumL = PageNum
        
        if PrintedHUD == 1 or 99:
            Input = int(input("Input:"))

        elif PrintedHUD == 0:
            Action = LastAction
            HUD(3,1)

        PrintedHUD = 1

        if DebugMode == 1:
            print(f"{Divider}\nDEBUG:")
            print(f"Var [Action]:{Action}")
            print(f"Var [LastAction]:{LastAction}")
            print(f"Var [Input]:{Input}")
            print(f"PrintedHUD{PrintedHUD}")
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
            print(f'''{Current}...{Divider}What would you like to do today?\n1[Shop] 2[Withdraw/Deposit] 99[Leave]''')

        if Action == 1:# Browser

            if Input == 8:
                if PageNum == 1 or 2:
                    Action = 2
                    PageNum = PageNumL
                HUD(3,PageNumL)
            if Input == 9:
                Action = 3
                PageNum = 1
                HUD(3,1)
            if Input == 1 or 2:
                PageNum = Input
                HUD(3,Input)

        if Action == 2:# Buying
            if Input < len(PricesP1):

                if PageNumL == 1: # Drinks
                    if Cash > PricesP1[Input] - 1:
                        print(f"Purchased: {ItemsP1[Input]} Price:{PricesP1[Input]}")
                        ItemsList.append(ItemsP1[Input])
                        Cash = (Cash - PricesP1[Input])
                    else:
                        print("Can't Purchause. Insufficient funds...")

                    print(f"Balance:{Cash}")
                    Action = 1
                elif PageNumL == 2: # Snacks
                    if Cash > PricesP2[Input] - 1:
                        print(f"Purchased: {ItemsP2[Input]} Price:{PricesP2[Input]}")
                        ItemsList.append(ItemsP2[Input])
                        Cash = (Cash - PricesP2[Input])
                    else:
                        print("Can't Purchause. Insufficient funds...")

                    print(f"Balance:{Cash}")
                    Action = 1
                    
                else:
                    print(f"This page can't, purchause failed. (PageNum:{PageNumL}/Input:{Input}/Price:{PricesP1[Input]}/Len:{len(PricesP1)})")
                    Action = 1
                    PageNum, PageNumL = 1,1 # Reset

            elif Input == 99:
                Action = 1

            else:
                print("Halted, over the list's 'page' length...")

            PageNum = PageNumL
            HUD(3,PageNumL)

        if Action == 3:# Deposit/Withdraw
            print(f"{NewPage}Please enter amount to withdraw... (Recomended:200)\nCurrent Cash:{Cash}")
            Amount = Cash + int(input("Amount:"))
            Cash = Amount
            PageNum = PageNumL
            Action = LastAction
            HUD(3,LastAction)

        if Input == 99:
            Action = LastAction
            HUD(3,1)
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Quick tests