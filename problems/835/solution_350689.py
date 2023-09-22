def melhor_volta(m):
    """Retorna uma tupla com o melhor corredor,
    o menor tempo de de volta e em qual volta ele ocorreu
    list-->tuple"""
    minimo=0
    corredorvencedor=0
    tempo=0
    for corredor in m:
            if min(corredor)<minimo:
                minimo=min(corredor)
                corredorvencedor=list.index(m,corredor)
                tempo=list.index(corredor,minimo)
    return [corredorvencedor+1,minimo,tempo+1]