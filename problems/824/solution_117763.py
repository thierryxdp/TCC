def uppCons(frase:str):
    '''Função que recebe str e transforma suas consoantes em maiusculas.
    str->str'''
    minuscula = 'bcçdfghjklmnpqrstvwxyz'         
    maiuscula = 'BCÇDFGHJKLMNPQRSTVWXYZ'         
    tabela = str.maketrans(minuscula, maiuscula) 
    return frase.translate(tabela)