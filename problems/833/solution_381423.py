def conta_numero(numero, matriz):
    '''Função que dado um número inteiro e uma matriz de inteiros, conta e retorna quantas vezes aquele número aparece na matriz
       parâmetro de entrada:int,list
       valor de retorno:int'''
    lista=[]
    for i in matriz:
        for j in i:
            if j == numero:
                list.append(lista,[j])
    return len(lista)