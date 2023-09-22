def busca(setor,matriz):
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
            j=j+1
        else:
            contatos=[]
        i=i+1
    return j