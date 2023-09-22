def freq_palavras(frases):
    """essa função recebe uma frase e retorna um
    dicionário com cada palavra da frase e o 
    número de vezes que ela aparece;
    str->dict"""
    lista = str.split(frases)
    dic = {}
    for c in lista:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    return dic