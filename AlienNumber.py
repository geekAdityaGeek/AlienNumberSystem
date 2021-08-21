def compute_digit(n, B, digit_pos, carry):
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
    if digit_pos<0:
        if carry == 1 :
            return B[carry]
        else : 
            return ''
    new_digit, new_carry = compute_digit(n, B, digit_pos, carry)
    return compute_succ(n, B, digit_pos-1, new_carry)+new_digit

def succ_alien(n, B):
    succ = compute_succ(n,B, len(n)-1, 1)
    return succ

if __name__ == '__main__':    
    B = input('Enter Alien Base System : ')
    n = input('Enter Alien Number : ')
    succ = succ_alien(n, B)
    print('successor of {} is {}'.format(n, succ))
    