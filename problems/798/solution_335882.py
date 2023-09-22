def freq_palavras(frases):
    '''Função que receba uma string e retorna a quantidade de letras das palavras da string
    str--> dict'''
    l_p = frases.split()
    d1 = {}
    contador = 0

    for p in l_p:
        d1[l_p[contador]] = l_p.count(l_p[contador])
        contador += 1
    return d1