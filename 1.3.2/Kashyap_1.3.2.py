def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip
    
def hyp(leg1, leg2):
    '''Uses the pythagoran theorem to calc
    Parameters: leg1 -> Integer, leg2 -> Integer
    Returns hypotonuse length -> Integer 
    ''' 
    return (leg1**2 + leg2**2)**0.5

def mean(a, b, c):
    '''Uses mean formula to calc
    Parameters: a -> Integer, b -> Integer, c -> Integer
    Returns mean -> Integer
    ''' 
    return (a+b+c)/3.0

def perimeter(base, height):
    '''Uses the perimeter formula
    Parameters: base -> Integer, height -> Integer
    Returns parameter -> Integer
    ''' 
    return (base+base+height+height)

print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)