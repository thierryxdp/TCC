def posLetra(text,letra,n):
    """Recebe como entrada uma string(text), uma letra e um numero(n), que indica a ocorrência da letra na frase, e retorna a posição da string em que aquela ocorrência da letra está
    str,str,int->int"""
    if str.count(text,letra)>=1:
        y=n-1
        str.replace(text,letra,'x',y)
        return str.find(text,letra)
    else:
        return -1