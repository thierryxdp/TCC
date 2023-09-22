def uppCons(frase):
    '''Função que recebe uma frase e retorna a mesma frase com todas as
    consoantes maiusculas.str->str
    obs:Usando o while funcionou no shell mas por aqui deu erro de limite
    de tempo'''
    refrase=''
    for caractere in frase:
        if caractere in 'bcçdfghjklmnpqrstvxwyz':
            refrase=refrase+caractere.upper()
        else:
            refrase=refrase+caractere
    return refrase