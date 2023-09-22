def qtd_divisores(n):
    '''it returns how many are the divisors of one given number
    int -> int'''
    divisors=0
    nn=n+1
    possibles=list(range(n+1))
    for number in possibles:
        if number>0 and n%number==0:
            divisors+=1
    return divisors
qtd_divisores(15)