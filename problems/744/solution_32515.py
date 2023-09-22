'''
Função que adiciona hashtags no início, meio e no fim de determinada string
quebrando suas duas metades e concatenando com as hashtags.
:s -> str:
:return -> str:
'''
def hashtag(s):
    #antes = s[:len(s)//2]
    #depois = s[len(s)//2:]
    #s = "#" + antes + "#" + depois + "#"
    s = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return s