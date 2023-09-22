''' Funcao que recebe uma string e insira o caractere #
    no inicio, no meio e no final dela.
    : return "#ab#cde#"
    : str -> str
'''
    def hashtag(str1):
    srt1 = "#" + str1[:len(str1)//2] + "#" + str1[len(str1//2:] + "#"
    return str1