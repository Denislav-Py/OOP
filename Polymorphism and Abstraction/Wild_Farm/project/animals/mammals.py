from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Seed, Food


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def food_type(self):
        return [Vegetable, Fruit]

    def weight_gain(self):
        return 0.1

    def feed(self, food: Food):
        if type(food) not in self.food_type():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += (food.quantity * self.weight_gain())
        self.food_eaten += food.quantity


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def food_type(self):
        return [Meat]

    def weight_gain(self):
        return 0.4

    def feed(self, food: Food):
        if type(food) not in self.food_type():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += (food.quantity * self.weight_gain())
        self.food_eaten += food.quantity


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def food_type(self):
        return [Vegetable, Meat]

    def weight_gain(self):
        return 0.3

    def feed(self, food: Food):
        if type(food) not in self.food_type():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += (food.quantity * self.weight_gain())
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def food_type(self):
        return [Meat]

    def weight_gain(self):
        return 1

    def feed(self, food: Food):
        if type(food) not in self.food_type():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += (food.quantity * self.weight_gain())
        self.food_eaten += food.quantity


