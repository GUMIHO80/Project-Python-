from datetime import time
from random import randint
class Clock:      
    def __init__(self,  hours = 0, minutes = 0, seconds = 0):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
       
    def convert( seconds ):
          seconds = seconds % (24 * 3600)
          hours = seconds // 3600
          seconds %= 3600
          minutes = seconds // 60
          seconds %= 60
          return Clock(hours , minutes ,seconds )

    def reconvert(self):
          seconds = self._seconds 
          hours = self._hours * 3600
          minutes = self._minutes * 60
          seconds = seconds + minutes + hours
          return (seconds )

    def __add__(self, other):
        x = Clock.reconvert(self)+ other

        return (Clock.convert(x))


        
    def __sub__(self, other):
        
        x = Clock.reconvert(self)  - Clock.reconvert(other)
       
        return x

    
    def st(self):
        return ("%02d:%02d:%02d" % (self._hours, self._minutes, self._seconds))
        
    def show(self):
        print (Clock.st(self))
        

l = []
for i in range(3):
    h = randint(0,24)
    m = randint(0,60)
    s = randint(0,60)
    l.append(Clock(h,m,s).st())
print(l)

for i in range(len(l)):
	
	min_idx = i
	for j in range(i+1, len(l)):
		if l[min_idx] > l[j]:
			min_idx = j
			
		
	l[i], l[min_idx] = l[min_idx], l[i]
print (l)    
        
p1 = Clock(15,34,1).reconvert()
p2 = Clock(10,12,9).reconvert()

result = p1-p2
print(result) 

clk = Clock.convert(12392)
clk.show()

c1 = Clock(15,34,1) + 120
c1.show()



