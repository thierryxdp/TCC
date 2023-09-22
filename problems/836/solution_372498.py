def busca(setor,matriz):
    r=[]
    for i in matriz:
        if i[2]==setor:
            r+=i
            
    return [r]