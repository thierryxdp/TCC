def hashtag(s):
    """adiciona hashtag no inicio, no meio e no fim da string;
    str->str"""
    meio = len(s)//2
    return "#" + s[0: meio] + "#"+ s[meio: len (s)] + "#"

#teste:
#hashtag(lapis)== #la#pis#
#hashtag (menina) == #men#ina#
#hashtag (ana) == #a#na#