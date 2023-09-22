def posLetra(string,letra,n):
    """função que recebe como entrada uma string, uma letra e um número
    que indica a ocorrência desejada da letra e retorna em que posição da string
    aquela ocorrência está. Retorna -1 caso existam menos ocorrências do que a pedida

    str,str,int -> int

    exemplos:
    posLetra("mariana come banana","a",3)==6
    posLetra("gabriel gabriel","g",3)==-1
    posLetra("mariana come banana","n",3)==17
    """
    i=0
    lista=[]
    while i!=len(string):
        if string[i]==letra:
            lista.append(i)
        i=i+1
    if n-1<=len(lista):
        return lista[n-1]
    if n-1>=len(lista):
        return -1