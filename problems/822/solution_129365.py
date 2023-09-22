def repetidos(lista):
    'retorna o numero de vezes que dois num consecutivos sao iguais na lista'
    'lista--int'
    primeironum=lista[0]
    x=1
    vezes=0
    while x<len(lista):
        if lista[x]==primeironum:
            vezes+=1
        primeironum=lista[x]
        x+=1
    return vezes