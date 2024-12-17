### Vending Machine

'''
NOTES:
Variables with Capitals should be reserved for Global Variables
'''
print("Please wait...")

## Global Variables

# User Values
Cash = 0
Money = Cash

## HUD

# Settings
MXLenI = 15
MXLenP = 9
MaxLen = MXLenI
space = 0

# HUD Elements
Blanks = " "
NewPage = "\n\n\n"
NewPage = NewPage*15
Divider = "-"
Divider = (f"""
{Divider*125}
""")

# Items
Type = ["Drink", "Snack"]
# Maximum Characters for Items is [15]
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

MenuNo = 0
Active = 1

Action = 0
# 0 = Initiate Console
# 1 = Browsing Shop
# 2 = Buying Items
# 3 = Deposit/Withdraw Cash

## Functions

# Menu/HUD

def HUD(type, inputs): # For Displaying Global Variables
    # 1 = CURRENT ACTIONS
    # 2 = INTERACTIONS
    # 3 = INFORMATION
    if type == 1:
        print(type)
    if type == 2:
        print(type)
    if type == 3:
        print(f"{Divider}Money:{Cash}\nBrowsing the shop...{Divider}Vending Machine{Divider}", end=''), printStoreMenu(inputs)
        print(f"{Divider}8[BUY] 9[DEPOSIT] 99[Back]\nItems Dispensed:")
    else:
        print("Function 'HUD' did not return from int 1-3, You may have entered out of value or a str.")

default_stock = 10

def printItemMenu(no,item,price,stock,price_,stock_):
    if Action == 2:
        print(f"{no}[{item}{price_}]   {price}{stock_}{stock}")
    else:
        print(f" [{item}{price_}]   {price}{stock_}{stock}")

def printStoreMenu(Num):
    print(f" Item{Blanks*16}Value    Stock")
    num, go = 0, 0
    # Page Number
    if   Num == 1:
        ItemsNum, PricesNum, go = ItemsP1, PricesP1, 1
    elif Num == 2:
        ItemsNum, PricesNum, go = ItemsP2, PricesP2, 1
    else:
        print('Menu does not exist...'), go == 0
    # Print Menu
    if go == 1:
        for item, price in zip(ItemsNum, PricesNum):
            I = MXLenI - len(item)
            P = MXLenP - len(str(price))
            I = Blanks * I
            P = Blanks * P
            printItemMenu(num,item,PricesNum[num],default_stock,I,P)
            num += 1
        
    print(f"\n6[Back] Page {Num}/2 7[Next]{Divider}")

def Interact():
    print("Interact")

# --- END OF VARIABLES ---

# Boot/Menu
print(NewPage,Divider,end='')
print(f'''Browsing the store...{Divider}What would you like to do today?
1[Shop] 2[Withdraw/Deposit] 99[Leave]''')

## CYCLE

while True: 
    try: 
        Input = int(input("Input:"))
        print(NewPage)
        HUD(3,Input)
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")