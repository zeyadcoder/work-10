class work:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
      if (self.x<other.x):
        return "ob1 is less than ob2" 
      else:
        return "ob2 is less than ob1"
    def __eq__ (self,other): 
     if (self.x==other.x):
        return("equal")
     else:
        return("not equal")
obj1 = work(2)
obj2 = work(7)
print (obj1 < obj2)
obj3 = work(5)
obj4 = work(9)
print (obj4 == obj3)

    


