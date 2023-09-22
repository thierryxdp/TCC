def hashtag(s):
    '''Retorna a string com "#" no inicio, no meio e no final dela
    str-> str'''
    from math import floor
    meio=floor(len(s)/2)
    return "#"+s[0:meio]+"#"+[meio:]+"#"