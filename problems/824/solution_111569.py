def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma porem com as consoantes
    maiusculas,str-->str"""
    n = ''
    for caractere in frase:
        if caractere in 'bcçdfghjklmnpqrstvxwyz':
            n += caractere.upper()
        else: 
            n += caractere
    return n