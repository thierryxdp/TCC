def posLetra(string,letra,n):
    """retorna em qual posiçao da string está a ocorrencia n da letra"""
    """caso a nao haja a ocorrencia pedida na string, retorna -1"""
    """str, str, int -> int"""
    i = 0
    if n <= string.count(letra):
        while i < len(string):
            x = string.find(n,i)
        i = i + 1  
        return x
    else:
        return -1