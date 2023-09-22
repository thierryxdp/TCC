def hastag(palavra):
    """Função que recebe uma string e insere o caractere # no inicio,
    meio e no final dela.
    str -> str"""
    
    return '#' + palavra[:len(palavra)] + '#' + palavra[len(palavra):] + '#'