def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma porem com as consoantes
    maiusculas,str-->str"""
    n = ''
    caractere=['bcçdfghjklmnpqrstvxwyz']
    while True:
        if caractere:
            n += caractere.upper()
        else: 
            n += caractere
    return n