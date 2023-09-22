def conta_numero(numero,matriz):
    """funcao que dado um numero inteiro e uma matriz de inteiros conta e retorna quantas vezes aquele número aparece na matriz"""
    lista=[]
    for i in range(len(matriz)):
        for j in range (len(matriz[i])):
            if numero == matriz[i][j]:
                list.append (lista,matriz[i][j])
               else:
                    lista = lista
   return len(lista)