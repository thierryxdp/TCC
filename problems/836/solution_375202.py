def busca(setor,ls):
    '''função que identifica quais funcionários trabalham em um certo setor,
    dada uma matriz e um setor
    str,list->list'''
    
    nova_lista=[]
    for listas in ls:
        if listas[2]==setor:
            del listas[2]
            nova_lista.append(listas)
            
    return nova_lista