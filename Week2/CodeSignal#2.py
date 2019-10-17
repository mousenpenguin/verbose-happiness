def adjacentElementsProduct(inputArray):
    # list of products defined by each product of two adjacent items in inputArray
    products = [inputArray[i] * inputArray[i + 1] for i in range(0, len(inputArray) - 1)]
    
    # returns the largest product in products list
    return max(products)
    
      
def shapeArea(n):
    # equation based on quadratic sequences math topic (2n² - 2n + 1)
    return 2 * n ** 2 - 2 * n + 1
    
    
 def makeArrayConsecutive2(statues):
    # returns the difference between the expected items (1 + max(statues) - min(statues)) 
    # and the total items (len(statues))
    return 1 + max(statues) - min(statues) - len(statues)
    
    
  def almostIncreasingSequence(sequence):
    # the errors count
    errors = 0
    
    for i in range(1, len(sequence)):
        value = sequence[i]
        
        # if value > previous one, then it goes well so far (no need to do anything else).
        if (value > sequence[i - 1]):
            continue
        
        # otherwise there is an error, and the errors count increments by 1
        errors += 1

        # if there are two errors then there is no solution.
        if (errors > 1):
            return False
        
        # but if there is only one error, then we check that the index is in the sequence array range
        if (i - 2 >= 0 and i + 1 < len(sequence)):
            # and check whether we can make the sequence consecutive
            # if we can't, then there is no solution due there is an unsolvable error.
            if (value <= sequence[i - 2] and sequence[i + 1] <= sequence[i - 1]):
                return False
        
    return True
