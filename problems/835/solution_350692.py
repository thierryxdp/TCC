def melhor_volta(m):
    """Retorna uma tupla com o melhor corredor,
    o menor tempo de de volta e em qual volta ele ocorreu
    list-->tuple"""
    minimo=[]
    corredorvencedor=0
    tempo=0
    minimoreal=0
    for corredor in m:
        list.append(minimo,[min(corredor)])
    corredorvencedor=list.index(minimo,[min(minimo)])
    minimoreal=min(minimo)
    list.index(m[corredorvencedor],minimoreal)    
    return [corredorvencedor+1,minimo,tempo+1]