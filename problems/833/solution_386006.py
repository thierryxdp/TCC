def conta_numero(numero,matriz):
    '''retorna a quantidade de vezes que um numero aparece na matriz'''
    '''int, list -> int'''
    
    linhas= len(matriz)
    i=0
    lista=[]
    while i < linhas:
        linha=matriz[i]
        cont=list.count(linha, numero)
        list.extend(lista, [cont])
        
    soma=sum(lista)
    return soma