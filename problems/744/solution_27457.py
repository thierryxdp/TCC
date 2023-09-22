def hashtag(s):
    """ Dada uma string, retorna a string inserindo o caractere '#' no inicio
        no meio e no final da propria string """
    meio = len(s) // 2
    stringNova = '#' + s[0:meio] + '#' + s[meio:len(s)] + '#'
    return stringNova