def conta_frases(text):
    """
    retorna o número de palavras em um texto
    str -> int
    """
    frasesSemP = str.split(text, '.')
    frasesSemPeSemEx = str.split(frasesSemP[-1], '!')
    frasesSemPExIn = str.split(frasesSemPeSemEx[-1], '?')
    frasesSemPExInret = str.split(frasesSemPExIn[-1], '...')
    return len(frasesSemPExInret)