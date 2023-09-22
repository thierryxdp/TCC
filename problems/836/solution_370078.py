def busca(setor,matriz):
    i=0
    j=[]
    contatos=[]
    while i<len(matriz):
        if setor in matriz[i]:
            contatos=contatos+matriz[i]
            j=contatos+j        
        else:
            contatos=[[]
        i=i+1
    return j