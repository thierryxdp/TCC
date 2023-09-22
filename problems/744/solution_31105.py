# Função que insera uma # no início, no meio e no final da string
# s é uma tring qualquer
# str-> str
def hashtag(s):
    media=len(s)/2
    return #+s[0:media]+#+[(media-1):]#