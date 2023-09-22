def hashtag(s):
    """ recebe uma string e retorna a mesma com o caractere # no inicio meio e final:
    string->tupla """
    return "#" + s[:len(s)//2] + "#" + s[len(s)//2] + "#"