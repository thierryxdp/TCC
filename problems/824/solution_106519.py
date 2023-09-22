def uppCons(frase):
    '''retorna uma nova frase com todas as consoantes da original em
    maiúsculo, sem alterar os demais caracteres
    str -> str'''
    
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    elemento = 0
    FRaSe = ''
    
    while elemento < len(frase):
        if frase[elemento] in consoantes:
            FRaSe += str.upper(frase[elemento])
        else:
            FRaSe += frase[elemento]
        elemento += 1
        
    return FRaSe