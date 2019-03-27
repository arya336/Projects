import math

class calculator:
    def __init__(self,num1,num2):
        self.first = num1
        self.second = num2
        
    def add(self):
        result1 = self.first + self.second
        return result1
    def sub(self):
        result2 = self.first - self.second
        return result2
    def mul(self):
        result3 = self.first * self.second
        return result3
    def div(self):
        result4 = self.first / self.second
        return result4
    def sin1(self):
        result5 = math.sin(self.first)
        return result5
    def cos1(self):
        result6 = math.cos(self.first)
        return result6
    def tan1(self):
        result7 = math.tan(self.first)
        return result7
    
    
a = int(input("Enter a number "))
b = int(input("Enter another number "))
c = input("Enter operation: '+','-','*','/','sin','cos','tan',: ")  

obj=calculator(a,b)

if c == "+":
    print(obj.add())
elif c == "-":
    print(obj.sub())
elif c == "*":
    print(obj.mul())
elif c == "/":
    print(obj.div())
elif c == "sin":
    print(obj.sin1())
elif c == "cos":
    print(obj.cos1())
elif c == "tan":
    print(obj.tan1())
    