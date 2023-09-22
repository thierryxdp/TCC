def pos_letra(texto, busca, n):
    "retorna a occorencia da letra"
    pos = texto.find(busca)
    while pos >= 0 and n > 1:
        pos = texto.find(busca, pos + 1)
        n -= 1
    return pos