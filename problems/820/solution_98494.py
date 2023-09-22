def posLetra (frase,letra,ocorrencia):
    '''Dado uma frase, uma letra contida na frase a um numero
    que indica a ocorrencia desejada da letra, retorna a posição
    na frase em que a ocorrencia da letra se encontra;
    str,str,int->int'''
    indice=0
    lista=[]
    while indice < len(frase):
        if frase[indice]==letra:
            list.extend (lista,[indice])
        indice+=1
    if ocorrencia> len(lista):
        return -1
    
    return lista [ocorrencia-1]