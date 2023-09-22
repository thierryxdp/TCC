def hashtag(s):'''retorna uma string com '#' no meio
    str-->str'''
     palavra = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return palavra