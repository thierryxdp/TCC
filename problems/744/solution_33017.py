from math import floor
def hashtag(s):
    """Função que recebe uma string e insere o caractere
    "#" no início, no meio e no final dela. Por exemplo,
    se a entrada for "abcd" a saída deve ser "#ab#cd#".
    Outro exemplo: se receber "abcde", a função deve
    retornar "#ab#cde#".
    str -> str"""
    return '#' + s[:(floor(len(s)/2))] + '#' + s[(floor(len(s)/2)):] + '#'