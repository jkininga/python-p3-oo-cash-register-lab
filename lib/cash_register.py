#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0): #discount is optional on instantiation
        self.discount = discount #instance attribute: user manually apply a discount
        self.total = 0 #no user intervention
        self.items = [] # no user intevention, keeps track of added items
        self.item_details = []
    
    #Function that adds new items with optional quantity
    def add_item(self, title, price, quantity=1):
        self.total += price * quantity #total value
        for _ in range(quantity):
            self.items.append(title)
            self.item_details.append({"title": title,"price": price, "quantity": quantity})
        # print(f"Value so far is excluding discount is {self.total}")

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount/100)
            self.total = round(self.total - discount_amount, 2)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    # def add_item_optional_quantity(self, title, price, quantity =1):
    #     self.total += price * quantity
    #     self.items.append({"title": title, "price": price, "quantity": quantity})
   
    def void_last_transaction(self):
        if self.items and self.item_details:
            self.items.pop()
            last_item = self.item_details.pop()
            self.total -= last_item["price"] * last_item["quantity"]

        


cashregister1 = CashRegister(10)

# cashregister2 = CashRegister(10)
cashregister1.add_item("iphone 12 promax", 50000, 1)
cashregister1.add_item("techno 19", 10000, 1)
# cashregister1.add_item("oppo x", 10000, 2)
# cashregister2.add_item("iphone 13 promax", 60000, 2)
cashregister1.apply_discount()
cashregister1.void_last_transaction()


# print(f"value after discount is {cashregister1.total}")
print(cashregister1.items)
print(cashregister1.total)
cashregister1.apply_discount()







# cahsregister1 = CashRegister(10)