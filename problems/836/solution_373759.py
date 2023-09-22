def busca(setor,matriz):
    ped=[]
    a = setor
    for i in matriz:
        for b in i:
            if b == a:
                ped.append(i)
    return (ped)