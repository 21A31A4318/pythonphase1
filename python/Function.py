class Function:
    def __init__(self):
        print("Basic Function")
    def addition(self,a,b):
        return a+b
    def subtraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b

A=int(input())
B=int(input())
obj=Function()
print(obj.addition(A,B))
print(obj.subtraction(A,B))
print(obj.multiplication(A,B))
print(obj.division(A,B))

        
