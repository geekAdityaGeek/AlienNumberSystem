def compute_digit(n, B, digit_pos, carry):
    '''
    This method computes the digit for successor and 
    carry, which is generated as result of addition of 1
    '''
    #check whether digit belongs to base system or not
    if n[digit_pos] not in B :
        raise Exception("Digit not provided in base system") 
    base = len(B)
    base_pos = (B.index(n[digit_pos])+carry)%base
    digit = B[base_pos]
    new_carry = carry
    if base_pos!=0 : 
        new_carry = 0        
    return digit, new_carry

def compute_succ(n, B, digit_pos, carry):
    '''
    This traverses the digit from right to left and computes
    the successor. It gets the digit and carry to proceed further 
    to next digit on the left
    '''
    succ_n = ''
    curr_carry = carry
    while digit_pos >= 0 :
        new_digit, new_carry = compute_digit(n, B, digit_pos, curr_carry)
        succ_n = new_digit+succ_n
        curr_carry = new_carry
        digit_pos = digit_pos - 1
    if curr_carry == 1 :
        return B[curr_carry]+succ_n
    return succ_n

def succ_alien(n, B):
    '''
    This method computes the successor. For successor, 1 needs to 
    be added to the number. 
    For rightmost digit 1 has to be added and carry is 0.
    Hence instead of keeping another operand, carry is set to 1.
    '''
    succ = compute_succ(n,B, len(n)-1, 1)
    return succ

if __name__ == '__main__':    
    B = input('Enter Alien Base System : ')
    n = input('Enter Alien Number : ')
    succ = succ_alien(n, B)
    print('successor of {} is {}'.format(n, succ))
    