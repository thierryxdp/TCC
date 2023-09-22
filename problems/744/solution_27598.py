#Para retornar o que foi pedido utilisei o comando len que me da o numero d caracteres
#Criei uma variel s que assumiu a operação de strings
#e por fim retornei o que foi pedido, no caso, o uso da # no inicio meio e fim da frase
def hashtag(s):
    """
    parametro s: é uma string
    me retorna uma uma str que tem # no inicio, meio e fim"""
    s = "#" + s[ : len(s)//2] + "#" + s[len(s)//2 : ] + "#"
    return s