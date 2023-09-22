def qtd_divisores(n):
    """ Funçao que retorna quantos divisores tem um numero"""
    if n==0 or n<0:
        return 0
    count=0
    for num in list(range(n[0],n+1)):
        if num%n == 0:
            qtd = count +=1
            return count