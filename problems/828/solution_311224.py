def primo(n):
    """Pede um número inteiro e verifica se ele é primo,
    retornando True ou False.
    int->bool"""
    import math
    from math import sqrt, ceil
    #Não precisamos testar para nenhum número par
    #que seja >2, pois são eles mesmos múltiplos de 2.
    #Também não precisamos testar para nenhum número >sqrt(n),
    #pois estaríamos repetindo múltiplos.
    #Por exemplo, 4<sqrt(24)<5. Não precisamos testar
    #para divisores maiores que 4, pois 4*6 = 24 e 6*4=24.
    for x in range (3,ceil(sqrt(n))+1,2):
        if n%x == 0 or n%2 == 0:
            return False
    return True