from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed, Food


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def food_type(self):
        return [Meat]

    def weight_gain(self):
        return 0.25

    def feed(self, food: Food):
        if type(food) not in self.food_type():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += (food.quantity * self.weight_gain())
        self.food_eaten += food.quantity


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def food_type(self):
        return [Vegetable, Fruit, Meat, Seed]

    def weight_gain(self):
        return 0.35

    def feed(self, food: Food):
        if type(food) not in self.food_type():
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += (food.quantity * self.weight_gain())
        self.food_eaten += food.quantity
