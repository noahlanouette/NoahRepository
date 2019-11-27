import unittest
class ListManipulator:
    def __init__(self, list):
        self.list = list

    def min(self): #checks if there are any numbers
        if len(self.list) == 0:
            return None

        min = self.list[0] #finds the min
        for item in self.list:
            if item < min:
                min = item
        return min

    def max(self): #checks if there are any numbers
        if len(self.list) == 0:
            return None

        max = self.list[0] #finds the max
        for item in self.list:
            if item > max:
                max = item
        return max

    def remove(self, value): #removes a value from the original list
        to_remove = []
        for i, item in enumerate(self.list):
            if item == value:
                to_remove.append(i)

        removed_count = 0 #gives the amount of removed values
        for index in to_remove:
            self.list.pop(index - removed_count)
            removed_count += 1

class TestListManipulator(unittest.TestCase): #tests go in order of when each piece of each function has been typed out
    def testmin(self):
        amount = ListManipulator(0)
        self.assertIsNone(amount)

    def test_min(self):
        numbersmall = ListManipulator(0)
        self.assertEqual(numbersmall, 0)

    def testmax(self):
        amount = ListManipulator(0)
        self.assertIsNone(amount)

    def test_max(self):
        numberbig = ListManipulator(100)
        self.assertEqual(numberbig, 100)

    def testremove(self):
        removed = ListManipulator(0) #couldn't figure this out
        self.assertIn(removed, to_remove)

    def test_remove(self):
        removedcount = ListManipulator(1)
        self.assertEqual(removedcount, 1)
        
unittest.main()
    
