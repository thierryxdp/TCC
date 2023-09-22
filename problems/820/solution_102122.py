def find_nth(texto, busca, n):
    pos = texto.find(busca)
    while pos >= 0 and n > 1:
        pos = texto.find(busca, pos + 1)
        n -= 1
    return pos