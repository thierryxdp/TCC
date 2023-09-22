def posLetra (frase,letra,n):
    '''Dado uma frase, uma letra contida na frase a um numero
    que indica a ocorrencia desejada da letra, retorna a posição
    na frase em que a ocorrencia da letra se encontra;
    str,str,int->int'''
    proximo=0
    lista=[]
    while proximo < len(frase):
        if frase[proximo]==letra:
            list.extend (lista,[proximo])
        proximo+=1
    if n> len(lista):
        return -1
    
    return lista [n-1]