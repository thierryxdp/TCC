def uppCons(frase):
    '''Função que recebe uma frase e retorna as consoantes da frase em maiusculo
    sem alterar os demais caracteres. Entrada: str. Saída:str'''
    c = 0
    CONS = ''
    
    while c < len(frase):
        if frase[c] in 'bcçdfghjklmnpqrstvwxyz':
            CONS=CONS+str.upper(frase[c])
        else:
            CONS=CONS + frase[c]
        c=c+1
         
    return CONS