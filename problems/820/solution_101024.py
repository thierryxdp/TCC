def posLetra(frase,letra,ocorrencia):
    """Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra
    e retorna a posição em que aquela letra se encontra na string."""
    """string->int"""
    pos = texto.find(busca)
    while pos >= 0 and ocorrencia > 1:
        pos = str.find(frase,busca, pos + 1)
        ocorrencia -= 1
    return pos