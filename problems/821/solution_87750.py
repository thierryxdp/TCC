def main(n):
    '''Função que recebe um numero e retorna sua fatorial int->int'''
    
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    return("O valor de %d! eh ="  ,fat)