def filtraMultiplos(lista,numero):
    '''função que filtra os números que serã dados em uma 
    lista e verifica se tais números são múltiplos do parâmetro 
    numero
    list,int->list'''
    posicao=0
    lista=[]
    while posicao<len(lista):
        if lista[posicao]%numero==0:
            lista=lista+lista[posicao]
        posicao=posicao+1
    return list