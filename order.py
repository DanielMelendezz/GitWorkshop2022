class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')
    def add_Salad(self):
        self.total_cost += 25
        self.items.append ("Salad")
        print("added Salad")

    # implement methods for menu items
