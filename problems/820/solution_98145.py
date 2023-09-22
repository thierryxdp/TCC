def posLetra(frase,letra,num):
    """Dado uma frase, uma letra e a ocorrência desejada, retorna a posição da ocorrência. string,string,int>int"""
    lista = list(frase)
    pos = lista.count(letra)
    if pos >= num:
        sub = str.replace(frase,letra,'*', num-1)
        return str.find(sub,letra,0,-1)
    else:
        return -1