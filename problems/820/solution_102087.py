def posLetra(string,letra,ocr):
    """Recebe uma string, uma letra e um número que indica a ocorrência desejada da letra;
    str, str, int -> int"""
    x = 0
    tamanho = len(string)
    y = 0
    while x < tamanho:
        if string[x] == letra:
            if y == ocr:
                return x
            else:
                y = y+1
        else:
            x = x+1
    return -1