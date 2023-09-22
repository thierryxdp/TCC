def qtd_divisores(num):
    '''Funcao que recebe um numero e retorna quantos divisores esse numero tem'''
    contagem = 0
    for i in range(1,num+1):
        if num%i==0:
            contagem += 1
    return contagem