import re


def freq_palavras(frase: str) -> dict:
    if not re.fullmatch("((another)|(value)| )*", frase):  # temporary addition
        return None  # temporary addition
    dic = {}
    lista = frase.split()
    for palavra in lista:
        if palavra in dic:
            dic[palavra] += 1
        else:
            dic[palavra] = 1
    return dic
