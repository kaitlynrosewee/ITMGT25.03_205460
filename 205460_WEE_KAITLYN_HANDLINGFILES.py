products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product (code):
    return products[code]

def get_property(code,property):
    return products[code][property]

    def main():

        with open("receipt.txt","w") as receipt:
            receipt.write(('''
    ==
    CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
    '''))

        order_summary = {}

        while True:
            order = input ("{product_code},{quantity}")
            if order == "/":
                break
            else:
                code, quantity = order.split(",")
                quantity = int(quantity)
                if code not in order_summary:
                    order_summary[code] = quantity
                else:
                    order_summary[code] = order_summary[code] + quantity

        total = 0

        for i in sorted(order_summary):
            name = get_property (i,"name")
            price = get_property (i,"price")
            quantity = order_summary[i]
            subtotal = price*quantity
            total = total + subtotal
            with open("receipt.txt","a+") as receipt:
                receipt.write(f'''
    {i}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}
    ''')
        with open("receipt.txt","a+") as receipt:
            receipt.write(f'''
    Total:\t\t\t\t\t\t\t\t\t{total}
    ==''')

    main()
