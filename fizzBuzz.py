class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        numbers= []
        for i in range(1, n+1):
        
            three = (i % 3 == 0)
            five = (i % 5 == 0)
        
            string = ""
            
            if three:
                string += "Fizz"
            
            if five:
                string += "Buzz"
            
            if not string: 
                string = str(i)
            
            numbers.append(string)
        
        return numbers
