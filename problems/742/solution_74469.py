def substitui(s,x,i):
    """Função que dados uma string s, um caractere x e
    um número inteiro i entre 0 e o comprimento da string,
    retorna uma string igual a s, com o elemento da posição i
    substituído pelo caractere x; string, string, int -> string"""
    
    stringS = str(s)
    posicao = stringS[i]
    substituicao= stringS[:i] + x + stringS[i+1:]
    return substituicao