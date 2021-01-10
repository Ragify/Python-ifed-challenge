import math

def nearest_square(n):
    if n<1:
        return 0
    else:
        return(math.floor(n**0.5)**2)