class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def area(self):
        print(f"The area of Rectangle is {self.width * self.height}")

  @classmethod
  def square(cls, size):
    return cls(size, size)
    
rec = Rectangle(2, 3)
rec.area()

re = Rectangle.square(10)
re.area()