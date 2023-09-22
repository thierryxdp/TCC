def filtraMultiplos(list,numero):
    '''função que filtra os números que serã dados em uma 
    lista e verifica se tais números são múltiplos do parâmetro 
    numero
    list,int->list'''
    posicao=0
    list=[]
    while posicao<len(list):
        if list[posicao]%numero==0:
            list=list+list[posicao]
        posicao=posicao+1
    return list