def validate(n, B):
    '''
    This validate number provided or not as per the base
    '''
    for digit in n :
        if digit not in B :
            raise Exception("Digit not provided in base system") 

def succ_alien(n, B):
    '''
    This method finds the successor for the number n
    for a given Base system - B
    '''
    base = len(B)
    rev_n = [digit for digit in n]
    rev_n.reverse()
    succ = []
    '''
    In real original carry is 0 and 1 is added to n. To avoid complexity, 
    1 is taken as a carry which will lead to same result
    '''
    carry = 1
    for digit in rev_n :
        pos = (B.index(digit)+carry)%base
        if pos == 0 : 
            carry = 1
        else : 
            carry = 0
        succ.append(B[pos])
    if carry == 1 :
        succ.append(B[carry])
    succ.reverse()
    return "".join(succ)

if __name__ == '__main__':    
    B = input('Enter Alien Base System : ')
    n = input('Enter Alien Number : ')
    validate(n,B)
    succ = succ_alien(n, B)
    print('successor of {} is {}'.format(n, succ))
    