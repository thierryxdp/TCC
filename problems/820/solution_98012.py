def posLetra(frase,letra,n):
    """funcao que recebe uma frase, uma letra e um numero que indica
    a ocorrencia desejada dessa letra. funcao retorna em que posicao 
    da string aquela ocorrencia da letra está. string,string,int->int"""

    proximo=0
    lista=[]
    while proximo<len(frase):
        if frase[proximo]==letra:
            list.extend(lista,[proximo])
        proximo = proximo+1
    
    if n>len(lista):
        return -1
    return lista[n-1]