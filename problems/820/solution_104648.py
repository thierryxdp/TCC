def posLetra(frase,letra,n):
    """Retornar uma função que receba uma string,letra e um n° e indica a ocorrência desejada da letra, sendo a posição retornada; str,str,int=>list"""
    lista = []
    i = 0
    while i<len(frase):
        if frase[i]==letra:
            lista=lista+[i]
        if (len(lista)+1)<=n:
            x = -1
        if (len(lista)+1)>n:
            x= lista[n-1]
        i=i+1
    return x