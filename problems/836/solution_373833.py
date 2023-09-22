def busca(setor,matriz):
    contato=[]
    for i in matriz:
        if setor in i:
            contato+= [i]
    return contato