class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, new_area):
        self.width = new_area / self.height

    def __str__(self):
        return f"To‘g‘ri to‘rtburchak: width={self.width:.2f}, height={self.height:.2f}, area={self.area:.2f}"


rect1 = Rectangle(10, 5)
print(rect1)

rect1.area = 150
print("\nMaydon o‘zgartirilgandan so‘ng:")
print(rect1)

rect2 = Rectangle(8, 4)
print("\nYangi to‘g‘ri to‘rtburchak:")
print(rect2)

rect2.area = 200
print("\nMaydon yangilangandan so‘ng:")
print(rect2)
