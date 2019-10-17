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
        
        if (value > sequence[i - 1]):
            continue
        

