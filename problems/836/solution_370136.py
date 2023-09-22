def busca(setor,matriz):
    '''Dado uma matriz e um setor, retorna as informações das pessoas do certor informado.str,list(list).->list(list)'''
    i=0
    l=0
    j=[]
    contatos=[]
    k=[]
    while i<len(matriz):
        if setor in matriz[i]:
            contatos=contatos+[matriz[i]]
            j=j+contatos
            k=j[l].remove(setor)
            l=l+1
        else:
            contatos=[]
        i=i+1
    return j