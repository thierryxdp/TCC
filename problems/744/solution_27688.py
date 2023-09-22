# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    import math
	quant = math.ceil(len(s))
        if len(s) % 2 == 0:
            c = "#" + str(s[0:quant]) + "#" + str(s[quant:len(s)]) + "#"
        else:
            quant = quant - 1
            c = "#" + str(s[0:quant]) + "#" + str(s[quant:len(s)]) + "#"
        return c