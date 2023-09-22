#Essa função serve para colocar # no início, meio e fim de strings
# str-> str
def hashtag(s):
    x = len(s)/2
    x = int(x)
    "divide o valor do comprimento da string, e coloca na váriavel x, em forma de int"
    return "#" + s[0:x] + "#" + s[x:] + "#"
	"retorna partes do texto divididas somadas às # em pontos específicos, como início, meio e fim"

#casos de teste:
"""
hashtag ("toretto") == '#tor#etto#'
hashtag ("paralelepipedo") == '#paralel#epipedo#'
"""