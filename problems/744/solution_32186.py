def hashtag(palavra):
    """Função que recebe uma string e insere o caractere # no inicio,
    meio e no final dela.
    str -> str"""
    
    return "#" + palavra[:len(palavra)//2] + "#" + palavra[len(palavra)//2:] + "#"