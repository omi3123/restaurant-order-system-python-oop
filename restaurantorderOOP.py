class MenuItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Order:
    def __init__(self):
        self.items=[]
        self.quantities=[]
    def add_item(self,item,quantity):
        self.items.append(item)
        self.quantities.append(quantity)
    def calculate_total(self):
        total=0
        for i in range(len(self.items)):
            total+=self.items[i].price*self.quantities[i]
        return total
class Restaurant:
    def __init__(self):
        self.menu= [
            MenuItem("Pizza",10),
            MenuItem("BUrger",9),
            MenuItem("Pasta",8),
            MenuItem("Salad",7)
        ]
    def show_menu(self):
        print("\nMenu: ")
        for index,item in enumerate(self.menu):
            print(f"{index+1}. {item.name} ${item.price}")
    def take_order(self):
        order=Order()
        while True:
            self.show_menu()
            choice=int(input("Enter menu item number(or 0 to finish): "))-1
            if choice==-1:
                break
            quantity=int(input("Enter quantity: "))
            order.add_item(self.menu[choice],quantity)
        return order
    def print_receipt(self,order):
        print("\nReceipt: ")
        for i in range(len(order.items)):
            item=order.items[i]
            quantity=order.quantities[i]
            print(f"{item.name} x {quantity}=${item.price*quantity}")
        print(f"Total: ${order.calculate_total()}")
restaurant=Restaurant()   
customer_order=restaurant.take_order()
restaurant.print_receipt(customer_order)