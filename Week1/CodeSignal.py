def add(param1, param2):
    # just returns the sum of the two parameters    
    return param1 + param2
    
    
      
def centuryFromYear(year):
    # Returns the smallest integer greater than or equal to year / 100,
    return math.ceil(year / 100)
    
    
      
def checkPalindrome(inputString):
    # the 'inputString' reversed string (slice syntax)
    reversed = inputString[::-1]
    
    return inputString == reversed
