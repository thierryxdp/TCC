def substitui(s,x,i):
    """Recebe uma string (frase, palavra, ...), um caractere x e um número
    i tal que i é menor ou igual o comprimento da string dada. Em seguida,
    retorna uma string igual a informada, mas o caractere na posição i é 
    substituído pelo caractere x.
    
    Parâmetros: s, x, i -> str, str, int
    Retorno: str"""
    
    ns=s[0:i]+x+s[i+1:-1]+s[-1]
    return ns