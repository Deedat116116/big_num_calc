"""
Filename: big_Number_calculator.py
Author: Deedat
Author: <Deedat, Abdul-Nasir>
Created: <10/31/2025>
Instructor: Holtslander
"""
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        pass

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

    def set_data(self,data):
        self.data = data