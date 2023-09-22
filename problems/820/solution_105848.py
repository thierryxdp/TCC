def posLetra(frase,letra,numero):
    '''função que recebe uma frase, uma letra, e um número
    que indica a ocorrência da letra e retorna
    a posição dela
    str str int --> int'''
    i=0
    resultado=[]
    j=0
    lista=list(frase)
    while i<len(frase):
        if lista[i]==letra:
            while j<=numero:
                if j==numero:
                    list.append(resultado,i)
                j=j+1
        i=i+1
    if numero>list.count(lista,letra):
        return -1
    return resultado[0]