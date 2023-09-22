def hashtag(string):
    """Função que retorna uma string com o caractere
    # no inicio, meio e fim da string"""
    stringTamanho=len(string)
    stringMetade=stringTamanho//2
    stringHashtag= "#"+string[0:stringMetade]+ "#" + string[stringMetade:]+"#"
    return stringHashtag