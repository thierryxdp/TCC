def posLetra(s,l,n):
    """Função que dado uma string,uma letra e um número
    retona em que posição da string aquela ocorrência da
    letra está, caso não esxista a quantidade de ocorrência
    pedida a função deverá retornar -1. str,str,int -> str
    """
    i = 0
    if l in s:
        while i < len(s) - 1:
            if l == s[i]:
                n = n-1
                i = i+1
            if l != s[i]:
                i = i+1
            if n == 0:
                return i - 2
            
    return -1