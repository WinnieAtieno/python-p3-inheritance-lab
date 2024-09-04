#!/usr/bin/env python

from user import User

class Student(User):
   def __init__(self, firstname, lastname):
      super().__init__(firstname, lastname)
      self.knowledge = []
      
   def learn(self,info):
      self.knowledge.append(info)