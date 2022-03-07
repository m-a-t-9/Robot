class Feeling:

  __name = ""
  __value = 0
  __range = ()

  def __init__(self, name, value, range=(0,100)):
    self.__name = name
    self.__value = value
    self.__range = range

  def __str__(self):
    return self.__name + " " + str(self.__value)

  def setValue(self, value):
    if value > self.__range[0] and value < self.__range[1]:
      self.__value = value
    else:
      print("Feeling's value out of range")

  def increaseFeeling(self):
    if self.__value + 1 > self.__range[0] and self.__value + 1 < self.__range[1]:
      self.__value += 1
    else:
      print("Feeling's value out of range")
