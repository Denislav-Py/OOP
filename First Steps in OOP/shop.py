# Create a class called Shop. Upon initialization, it should receive a name (string) and items (list). 
# Create a method called get_items_count() that returns the number of items in the store.

class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)

# Test input
shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())



