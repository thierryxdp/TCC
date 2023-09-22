def busca(setor,matriz):
    ped=[]
    red=[]
    a = setor
    for i in matriz:
        for b in i:
            if b == a:
                ped.append(i)
                
    if len(ped)>0:
        for c in ped:
            for d in c:
                if d == a:
                    c.remove(d)
    
    return (ped)