def pontos(x):
    d ={'cor':0,'fla':0}
    d['cor']=d['cor']
    d['fla']=d['fla']
    lista1=x[0]
    lista2=x[1]
    lista12=lista1[2]
    'placar 1 lista'
    lista22=lista2[2]
    'placar 2 lista'
    lista13=lista12[0]
    'primeiro numero do placar 1'
    lista14=lista12[1]
    'segundo numero do placar 1'
    lista23=lista22[0]
    'primeiro numero do segundo placar'
    lista24=lista22[1]
    'segundo numero do segundo placar'
    lista01=lista1[0]
    'primeiro time lista 1'
    lista02=lista1[1]
    'segundo time lista 1'
    lista03=lista2[0]
    'primeiro time lista 2'
    lista04=lista2[1]
    'segundo time lista 2'
    d1={lista01:0,lista02:0}
    if lista13>lista14:
        d1[lista01]=d1[lista01]+3
    if lista13<lista14:
        d1[lista02]=d1[lista02]+3
    if lista13==lista14:
        d1[lista02]=+1 
    if lista13==lista14:
        d1[lista01]=+1
    

    d2={lista03:0,lista04:0}
    if lista23>lista24:
        d2[lista03]+=3
    if lista23<lista24:
        d2[lista04]+=3
    if lista23==lista24:
        d2[lista03]=+1
    if lista23==lista24:
        d2[lista04]+=1
    d3=d1[lista01]+d2[lista04]
    d4=d1[lista02]+d2[lista03]
    return {lista01:d3,lista02:d4}