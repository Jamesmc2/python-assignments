import random
def randInt(min= 0  , max= 100  ):
    if max<0 or min>max:
        return false
    return round(random.random()*(max-min)+min)
print(randInt(max =6,min = 5))    
