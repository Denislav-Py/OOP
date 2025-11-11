# Create a function called start_playing which will receive an instance and will return its play() method.
def start_playing(obj):
    return obj.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


class Children:
    def play(self):
        return "Children are playing"


guitar = Guitar()
print(start_playing(guitar))
children = Children()
print(start_playing(children))
