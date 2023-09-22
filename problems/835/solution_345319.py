def melhor_volta(matriz):
    """dada uma matriz 6X10 (referente a resultados de corrida de kart),
    a função retorna uma tupla contendo quem fez a melhor volta, qual foi
    tempo e em que volta esse menor tempo ocorreu.
    list-->tuple
    
    Parâmetros
    indice1: índice referente ao primeiro while
    índice2: índice referente ao segundo while
    nlinhas: número de linhas da matriz
    ncolunas: número de colunas da matriz
    lista: lista com todas as voltas de todos os pilotos, em ordem
    quem: piloto que fez a melhor volta
    quando: em qual volta desse piloto ocorreu o menor tempo"""
     
     
    indice1=0
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    lista=[]
    while indice1<nlinhas:
        indice2=0
        while indice2<ncolunas:
            list.append(lista,matriz[indice1][indice2])
            indice2=indice2+1
        indice1=indice1+1
    
    quem=int(list.index(lista,min(lista))/10)+1
    quando=(list.index(lista,min(lista))+1)-(quem-1)*10
    return (quem, min(lista), quando)