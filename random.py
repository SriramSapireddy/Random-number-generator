import random
def random(num, start = 1, end = 500): 
    a = [] 
    x = random.randint(start, end) 
      
    for x in range(num): 
          
        while x in a: 
            x = random.randint(start, end) 
              
        a.append(x) 
          
    a.sort() 
      
    return a

print(random(10))
