####### Question 1 ########

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



####### Question 2 ########

class DotProduct:
    # Assumption - both have same number of elements. If not we can use itertools.zip_longest
    def __init__(self,integers1,integers2):
        self._integers1 = integers1
        self._integers2 = integers2


    def product(self):
        calculatedInteger = 0
        for i,j in zip(self._integers1, self._integers2):
            calculatedInteger+=(i*j)

        return (calculatedInteger)
    


###### Test cases

# Test 1
# A = 3i + 5j + 4k
# B = 2i + 7j + 5k
# DotProduct = 61

dotProd = DotProduct([3,5,4],[2,7,5])
print(dotProd.product())


# Test 2
# A = -4i -7j 
# B = 6i + 8j
# DotProduct = -80

dotProd = DotProduct([-4,-7],[6,8])
print(dotProd.product())