def qtd_divisores(n):
    '''it returns how many are the divisors of one given number
    int -> int'''
    divisors=0
    for number in list(range(1:n)):
        if n%number==0 and number>0:
            divisors+=1
    return divisors