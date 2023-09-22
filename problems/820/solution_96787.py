def posLetra(frase,letra,ocorrencia):
    """Recebe como entrada uma string uma letra e um numero e
    retorna a posição da string que essa letra está na ocorrencia,
    caso exista menos ocorrencias da letra que a ocorrencia pedida,
    retorna -1; str, str, int-> int"""
    
    i=0
    o=0
    while i<len(frase) and o<ocorrencia:
        if frase[i]==letra:
            o=o+1
            pos=i
        i=i+1
    if (o!=ocorrencia):
        return -1
    else:
        return pos