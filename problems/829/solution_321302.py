def soma_h(n:int)->int:
    """ A função calcula o valor de H. Que é a soma do número 1 dividido pelo elemento de indice 0, do range de N+1, mais o número 1 dividido pelo elemento de índice 1 do range de N+1 e assim sucessivamente. Até o número 1 ser divido pelo próprio N"""
    soma = 0
    for numero in list(range(1,n+1)):
        soma += 1/numero
    return round(soma,2)