#!/usr/bin/env python

from user import User

import random


class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Initial Knowledge"]
        
    def teach(self):
        return self.knowledge[0]
