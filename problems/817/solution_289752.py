import math
def acima_da_media(notas):
    '''coment'''   
    list.sort(notas)
    funcao= sum(notas)/len(notas)
    ident= list.index(notas,funcao)
    x=math.ceil(funcao)
        
    return notas[x+1:]