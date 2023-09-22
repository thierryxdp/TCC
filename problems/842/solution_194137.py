def ida(g1,g2):
    '''Determina o ponto que cada time recebe após o jogo de ida
    int,int->[int,int]'''
    if g1>g2:
        return [3,0]
    elif g1==g2:
        return [1,1]
    else:
        if g1<g2:
            return [0,3]
def volta(g3,g4):
    '''Determina o ponto que cada time recebe após o jogo de volta
    int,int->[int,int]'''
    if g3>g4:
        return [0,3]
    elif g3==g4:
        return [1,1]
    else:
        if g3<g4:
            return [3,0]
def pontos_por_time(lista):
    '''Retorna um dicionário com o nome do time e o número de pontos dele'''
    '''[[str,str,[int,int],[str,str,[int,int]]]->{str,int,str,int}'''
    lista1=lista[0]
    lista2=lista[1]
    gol_ida=lista1[2]
    gol_volta=lista2[2]
    g1=gol_ida[0]
    g2=gol_ida[1]
    g3=gol_volta[0]
    g4=gol_volta[1]
    timeA=ida(g1,g2)[0]+volta(g3,g4)[0]
    timeB=ida(g1,g2)[1]+volta(g3,g4)[1]
    if timeA>=timeB:
        return {lista1[0]:timeA,lista2[0]:timeB}
    else:
        if timeB>timeA:
            return {lista2[0]:timeB,lista1[0]:timeA}