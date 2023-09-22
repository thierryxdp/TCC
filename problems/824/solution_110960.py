def uppCons(s):
    '''Funcao que retorna todas as consoantes em maiuscula
    entra:str
    saida:str'''
    newStr=''
    n=0
    while n<len(s):
        if s[n] in 'bcdfghjklmnpqrstvwxyzç':
            newStr=newStr+s[n].upper()
        else:
            newStr=newStr+s[n]
        n+=1
    return newStr