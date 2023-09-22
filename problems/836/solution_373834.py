def busca(setor,matriz):
    contato=[]
    for i in matriz:
        if setor in i:
            i=i[0],i[1],i[3]
            contato+= [i]
    return contato