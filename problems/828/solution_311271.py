def primo(n):
    """Pede um número inteiro e verifica se ele é primo,
    retornando True ou False.
    int->bool"""
    #Eliminamos 0 e 1 como primos, pela definição.
    if n<3 and n!=2:
        return False
    #Para qualquer número n>=3,
    #não precisamos testar a divisão por nenhum número par
    #que seja >2, pois são eles mesmos múltiplos de 2.
    for x in range (3,n,2):
        if n%x == 0 or n%2 == 0:
            return False
    return True