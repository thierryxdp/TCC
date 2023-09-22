def posLetra(frase,letra,ocorrencia):
    """Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra
    e retorna a posição em que aquela letra se encontra na string."""
    """string->int"""
    a = str.find(frase,letra)
    while a >= 0 and ocorrencia > 1:
        a = str.find(frase,letra, a + 1)
        ocorrencia -= 1
    return a