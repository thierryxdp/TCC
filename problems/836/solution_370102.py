def busca(setor,matriz):
    i=0
    j=[]
    contatos=[]
    k=[]
    while i<len(matriz):
        if setor in matriz[i]:
            contatos=contatos+[matriz[i]]
            j=j+contatos
            k=j[1].remove(setor)
        else:
            contatos=[]
        i=i+1
    return j