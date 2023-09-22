def posLetra(frase,letra,numero):
    '''funcao que recebe uma str, uma letra e um numero e retorna em que posição da str a ocorrencia
    da letra esta'''
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