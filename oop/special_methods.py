# DUNDER METHODS

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #  These special methods help us expose user defined objects clearly
    def __str__(self):
        return f"{self.title} by {self.author}"  # This is a special method

    def __len__(self):
        return self.pages  # This is a special method

    def __del__(self):
        print("A book object has been deleted")  # This is a destructor


b = Book("Python rocks", "Jose", 200)

# Before special methods
# print(b)  # <__main__.Book object at 0x7f8b1b3b3d30>
# str(b)  # '<__main__.Book object at 0x7f8b1b3b3d30>'

# After special methods
print(b)  # Python rocks by Jose
print(len(b))  # 200
del b  # Deletes the object from memory

