def hashtag(str1):
    ''' Funcao que recebe uma string e insira o caractere #
    no inicio, no meio e no final dela.
    : return "#ab#cde#"
    : str -> str '''
    str1 = "#" + pre + "#" + pos + "#"
    str1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1)//2:] + "#"
    return str1