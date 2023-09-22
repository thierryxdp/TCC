def pos(frase, letra, n):
    qtd_letras = str.count(frase, letra) # 3

    if qtd_letras < n:
        return -1
    else:
        i = 0
        p = 0
        while i < len(frase):
            p = str.index(frase, letra, i)
            i = p + 1