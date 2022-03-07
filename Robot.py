from Feeling import * 

class Robot:

  __feelings = []

  def __init__(self, name):
    self.__name = name
    self.__createFeelings()
    print("Hello, I'm Lucy")

  def __createFeelings(self):
    self.__feelings.append(Feeling("Happy", 0))
    self.__feelings.append(Feeling("Sad", 0))
    self.__feelings.append(Feeling("Surprised", 0))
    self.__feelings.append(Feeling("Afraid", 0))
    self.__feelings.append(Feeling("Angry", 0))
    self.__feelings.append(Feeling("Anxious", 0))

  def __str__(self):
    serial = self.__name + "/n"
    for feeling in self.__feelings:
      serial += str(feeling) + "/n"
    return self.__name + "/n" + str(self.__feelings)