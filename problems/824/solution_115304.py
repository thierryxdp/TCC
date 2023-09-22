def uppCons(frase):
    ''' recebe frase e retorna ela com consoante em maiusculo,entrada/saida:str'''
    fras=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyç':
            fras=fras+ str.upper(frase[i])
        else:
            fras=fras+frase[i]
        i=i+1
    return fras