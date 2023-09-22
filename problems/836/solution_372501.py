def busca(setor,matriz):
    r=[]
    for i in matriz:
        a=[]
        if i[2]==setor:
            a+=i
        r+=[a]
    return [r]