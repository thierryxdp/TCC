def posLetra(texto, busca, n):
    """Função que recebe como entrada uma string, uma letra
    e um número que indica a ocorrência desejada da letra e 
    retorna em que posição da string aquela ocorrência da 
    letra está.
    str,str,int->int"""
    pos = texto.find(busca)
    while pos >= 0 and n > 1:
        pos = texto.find(busca, pos + 1)
        n -= 1
    return pos