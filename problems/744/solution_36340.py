def hashtag(s):
    '''Função que dado uma string, retorne a string com o
    caractere "#" no início, no meio e no final dela;
    str-> str'''
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s