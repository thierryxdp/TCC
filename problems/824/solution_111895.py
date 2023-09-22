def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma porem com as consoantes
    maiusculas,str-->str"""
    n =''
    caractere=0
    while caractere<len(frase):
        if frase[caractere] in 'bcçdfghjklmnpqrstvxwyz':
            n += caractere.upper()
        else: 
            n += caractere
        n=n+1   
    return n