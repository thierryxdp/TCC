def posLetra(texto,letra,ocorrencia):
    """recebe como entrada uma string, uma letra e um numero que
    indica a ocorrencia desejada da letra(1 para primeira ocorrencia,
    2 paea segunda, etc), e retorna em que posicao da string aquela 
    ocorrencia da letra está. Caso exista menos ocorrencia da letra do que
    a ocorrencia pedida, a função deve retornar -1"""
    i=0
    n=0
    while i<len(texto) and n<ocorrencia:
        if texto[i]==letra:
            n=n+1
            i=i+1
            if n<ocorrencia:
                return -1
            else:
                return i-1