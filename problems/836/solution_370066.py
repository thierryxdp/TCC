def busca(setor,matriz):
    i=0
    j=[]
    contatos=[]
    while i<len(matriz):
        if setor in matriz[i]:
            j=contatos+matriz[i]
            contatos=j+contatos        
        else:
            contatos=[]
        i=i+1
    return contatos