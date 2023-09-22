def posLetra(frase,letra,ocorrencia):
    """Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra
    e retorna a posição em que aquela letra se encontra na string."""
    """string->int"""
    i=0
    a=0
    b=str.count(frase,letra)
    if b<ocorrencia:
        return -1
    else:
        while i<len(frase):
            if i<ocorrencia and letra in frase:
                a=str.index(frase,letra,ocorrencia)
                i=i+1
        return a