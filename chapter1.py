from itertools import combinations

class OddProduct:

    def __init__(self, integers):
        self._integers = integers


    def findPairs(self):
        for i,j in combinations(self._integers,2):
            if i*j % 2 != 0:
                return (i,j) 
            


###### Test cases  #######

# Test 1
productOdd = OddProduct([1,2,3,4,5,6,8])
print(productOdd.findPairs())


# Test 2
productOdd = OddProduct([2,2,2,2,2,2,2])
print(productOdd.findPairs())

# Test 3
productOdd = OddProduct([1,2,-3,-4])
print(productOdd.findPairs())

