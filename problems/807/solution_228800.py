def conta_frases(texto):
    '''Funcao que conta o numero de frases que aparece em um texto
ent->str
saida->int'''
    valor=0
    for i in range(0,len(texto)):
        c=texto[i]
        if '.' ==c and texto[i-1]!='.':
            valor+=1
        if '!'==c or '?'==c:
            valor+=1  
    return valor