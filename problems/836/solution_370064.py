def busca(setor,matriz):
    i=0
    j=0
    contatos=[]
    while i<len(matriz):
        if setor in matriz[i]:
            contatos=contatos+matriz[i]+contatos
        else:
            contatos=[]
        i=i+1
    return contatos