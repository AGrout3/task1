cart: dict = {}

cart_summary_cost: int = 0

# ITEM STORAGE
item1: dict = {
    "product_name": "Xiaomi Redmi Note",
    "product_year": "2019",
    "product_quantity": 100,
    "product_description": "XIAOMI description",
    "product_price": 200}

item2: dict = {
    "product_name": "Apple Iphone X",
    "product_year": "2022",
    "product_quantity": 50,
    "product_description": "IPHONE description",
    "product_price": 800}

item3: dict = {
    "product_name": "Samsung Galaxy",
    "product_year": "2020",
    "product_quantity": 200,
    "product_description": "SAMSUNG description",
    "product_price": 500}
# END OF STORAGE

def main_page():
    """
    Main page navigation function. Takes user's input and leads to referring page. Available input: number (1) or
    name (main/main page)
    """
    print("Welcome to Main page!")
    print("1/Main page\n2/Store page\n3/Cart page")
    go_to = input("So, where to? Type number or name ").upper()
    if go_to in ["1", "MAIN", "MAIN PAGE"]:
        draw_line()
        print("Loading Main page...")
        draw_line()
        main_page()
    elif go_to in ["2", "STORE", "STORE PAGE"]:
        draw_line()
        print("Loading Store page...")
        draw_line()
        store_page()
    elif go_to in ["3", "CART", "CART PAGE"]:
        draw_line()
        print("Loading Cart page...")
        draw_line()
        cart_page()
    else:
        draw_line()
        print("Incorrect input")
        draw_line()
        main_page()


def cart_page():
    """
    Cart page function. It shows items in cart (if they are), their quantity and summary price (+VAT).
    Also user can change quantity of some products or clean whole cart (not implemented yet) or go back to Main.
    While doing some functions here I realized that I REALLY should go through classes, but whatever
    """
    print("This is your Cart\n")
    if cart == {}:
        print("Your cart is empty\nYou will be redirected to Main page")
        draw_line()

    elif cart != {}:
        for key, value in cart.items():
            print(key, ' : ', value)
        print("Total cost of all products is: " + str(cart_summary_cost) + " (" + str(
            int(cart_summary_cost * 1.08)) + " including 8% VAT)")
        draw_line()

        cart_action = input("""Type 1 if you want to change quantity of some
Type 0 if you want to delete all
Type 'Back' for Main menu """).upper()

        if cart_action in ["1", "0", "BACK"]:
            if cart_action == "1":
                draw_line()

                temp = list(cart.keys())
                for i in range(len(temp)):
                    print(i, end=" ")
                    print(temp[i])
                draw_line()

                to_change = int(input("What products quantity you want to change? Type its number "))
                print("You're going to change ", temp[to_change], "quantity in your cart")
                print("There's " + str(cart[(temp[to_change])]) + " of " + temp[to_change] + "in your cart.")
                print("Not implemented yet")
                draw_line()
                cart_page()
                # CONSTRUCTION SITE AHEAD, WEAR SAFETY HELMET
                # x = 1
                # while temp[to_change] not in (eval("item" + str(x))).values:
                #     if temp[to_change] not in (eval("item" + str(x))).values:
                #         x += 1
                #     else:
                #         print(eval("item" + str(x)))
                # draw_line()
            elif cart_action == "0":
                draw_line()
                print("Not implemented yet")
                cart_page()
            elif cart_action == "BACK":
                draw_line()
                main_page()
        else:
            print("Something went wrong")

    else:
        print("Something went wrong")
    main_page()


def store_page():
    """
    Store page contain function, which transfer item quantity from stored item dictionaries to cart as key/value
     (name/quantity) pairs. Also counts summary price based on prices, stored in item dictionaries.
    """

    print(f'''Welcome to our store! There are our latest devices:
1/{item1["product_name"]}
2/{item2["product_name"]}
3/{item3["product_name"]}''')

    action = input("What device you are interested in? Type it's number\nor 'Back' for Main page ")
    if action.upper() in ["1", "2", "3", "0", "BACK"]:
        if action in ["1", "2", "3"]:
            chosen_device = None
            chosen_device = eval("item" + str(action))
            draw_line()
            print(chosen_device["product_name"] + " (" + chosen_device["product_year"] + ")" + "\n" + "Avaiability: " +
                  str(chosen_device["product_quantity"]) + "\n" + "Description: " + chosen_device[
                      "product_description"] + "\n" + "Price: " + str(chosen_device["product_price"]))
            draw_line()
            action = input('''Still interested? Type
1 or Add to add device to your cart
0 or Back to return to Store page ''').upper()
            if action in ["1", "ADD"]:
                draw_line()
                quantity = None
                quantity = int(
                    input((str(chosen_device["product_quantity"])) + ' avaiable!\nHow much do you want? '))
                summary_cost = (chosen_device["product_price"] * quantity)
                global cart_summary_cost
                cart_summary_cost += (summary_cost)
                added: list = [(chosen_device["product_name"], quantity)]
                chosen_device["product_quantity"] = (chosen_device["product_quantity"] - quantity)
                if chosen_device["product_name"] not in cart.keys():
                    cart.update(dict(added))
                elif chosen_device["product_name"] in cart.keys():
                    cart[(chosen_device["product_name"])] = cart[(chosen_device["product_name"])] + quantity
                for item in cart:
                    draw_line()
                    print(str(quantity) + " " + chosen_device['product_name'] + " was added to cart")
                    print("Total price is " + str(summary_cost))
                    print("Now only " + str(chosen_device["product_quantity"]) + " left!")
                    draw_line()
                    store_page()
                else:
                    print("Something went wrong")
                    draw_line()
                    store_page()
            elif action in ["0", "BACK"]:
                    draw_line()
                    store_page()
            else:
                    print("Something went wrong")
                    draw_line()
        elif action.upper() in ["0", "BACK"]:
            draw_line()
            main_page()
        else:
            print("Incorrect input. Please, try again.")
            draw_line()
            store_page()


def draw_line():
    """
    Visual separator
    """
    print("=*" * 20)


main_page()
