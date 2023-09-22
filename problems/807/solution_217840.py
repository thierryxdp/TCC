def conta_frases(a):
     '''funcao que recebe um texto e retorna quantas frases tem nele;str-->int'''
        x=str.split(a,'.')
        Y=str.split(a,'!')
        z=str.split(a,'?')
        v=str.split(a,'...')
    
    return len(x)+len(y)+len(v)+len(z)