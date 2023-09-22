def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma porem com as consoantes
    maiusculas,str-->str"""
    n =''
    caractere=0
    while n<len(frase):
        if frase[caractere] in 'bcçdfghjklmnpqrstvxwyz':
            x += caractere.upper()
        else: 
            x += caractere
        n=n+1   
    return x