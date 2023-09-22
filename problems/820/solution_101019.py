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
        while i<ocorrencia:
            a = str.find(frase,letra, a+1)
            i=i+1
        return a