def posLetra(frase,letra,ocorrencia):
    '''Função que  retorna a posição da ocorrencia da letra
    pedido na entrada e se ela não estiver na frase retorna -1
    entrada=string,string,int
    saida=int'''
    i=0
    lista=[]
    if ocorrencia<=frase.count(letra):
        while i< len(frase):
            if frase[i] in letra:
                list.append(lista,i)
            i+=1
        return lista[ocorrencia-1]
    else:
        return -1