def hashtag(s):
    '''retorna uma string com '#' no meio
    str-->str'''
    numero= len(s)//2
    palavra = "#" + s[:numero] + "#" + s[numero-1:] + "#"
    return palavra