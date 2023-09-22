def hashtag(s):
    '''Função que receba uma string e onsira o caractere '#'
    no início, no meio e no final dela.
    str -> str'''
    quantidade = len(s)
    meio = int(quantidade/2)
    comeco = s[:meio]
    fim = s[meio:]
    return '#' + comeco + '#' + fim + '#'