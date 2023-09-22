def conta_numero(numero,matriz):
    '''funcao que dado um numero e uma matriz, percorre por todos os elementos da matriz e conta quantas vezes esse numero esta nessa matriz;
       int,list(list)-> int'''
    soma= 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha]):
                            if coluna==numero:
                            soma=soma+1
    return soma