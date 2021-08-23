class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return 2*self.width+2*self.height

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**0.5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'

    linhas = ['*'*self.width]*self.height

    return '\n'.join(linhas) + '\n'

  def get_amount_inside(self, outro):
    return int(self.get_area()/outro.get_area())

  def  __repr__(self):
    return "Rectangle(width="+str(self.width)+', height='+str(self.height)+')'

    
class Square(Rectangle):

  def __init__(self, side):
    Rectangle.__init__(self, side, side)
    self.side = side
    
  def set_side(self, side_1):
    self.side = side_1
    self.height = side_1
    self.width = side_1

  def set_height(self, side_1):
    self.set_side(side_1)
  #  self.side = side_1

  def set_width(self, side_1):
    self.set_side(side_1)
  #  self.side = side_1

  def  __repr__(self):
    return "Square(side="+str(self.side)+')'