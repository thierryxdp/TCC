def melhor_volta(matriz):
    '''Função que dada uma matriz 6x10 com os tempos em segundos
    dos corredores em cada volta, sendo 6 corredores e 10 voltas para cada;
    retorna uma tupla com a informação de quem teve a melhor volta
    da prova, com qual tempo e em que volta; list -> tuple'''
    
    lista = [ ]
    A = 0
    B= 0
    listaA = 0
    listaB = 0
    for i in matriz:
        
        for j in i:
            lista = lista + [j]
    menor = min(lista)
    
    for i in matriz:
        B = 0
        A = A + 1
        for j in i:
           if menor == j:
              listaB = listaB + B
              listaA = listaA + A
           B = B + 1
    return listaA,menor,listaB+1