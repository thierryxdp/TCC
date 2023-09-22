def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma porem com as consoantes
    maiusculas,str-->str"""
    n =''
    caractere=0
    while caractere<len(frase):
        if frase[caractere] in 'bcçdfghjklmnpqrstvxwyz':
            n += frase[caractere].upper()
        else: 
            n += frase[caractere]
    n=n+1   
    return n