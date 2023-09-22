def lingua_p(palavra):
    '''Programa que retorna a palavra completamente minuscula e na lingua do P
    str -> str'''
    p = palavra.lower()
    i = 0
    l = []
    for i in range(len(palavra)):
        if p[i] != "a" and p[i] != "á" and p[i] != "e" and p[i] != "é" and p[i] != "i" and p[i] != "o" and p[i] != "u" and p[i] != "ú":
            list.append(l, p[i])
        else:
            list.append(l, p[i]+"p"+p[i])
    return "".join(l)