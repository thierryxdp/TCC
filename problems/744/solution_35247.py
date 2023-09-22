def hashtag(s):
    """Função que recebe uma string e insere o caractere '#', no inicio
    meio e final dela"""
    return "#"+ s[0:(len(s)//2)]+"#"+ s[(len(s)//2):]+"#"