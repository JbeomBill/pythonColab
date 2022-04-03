class Calc():
    totalSum = 0
    def __init__(self) -> None:
        self.totalSum = 0
    def sum(self,a,b):
        self.totalSum = a+b
        print("여기의합산은?===>"+str(self.totalSum))
        return a+b
    
if __name__ == "__main__" :
    temCalc = Calc()
    returnVal = temCalc.sum(5,7)
    print("returnVal===>"+str(returnVal))
<<<<<<< HEAD
    print("returnVal===>"+str(returnVal))
    print("returnVal===>"+str(returnVal))
    
=======
>>>>>>> 46d1cff63fbab78d08ad57a80e5baa0d766a7ade
