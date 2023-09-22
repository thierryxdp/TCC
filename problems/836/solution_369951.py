def busca(nome,matriz):
    x=[]
    y=0
    for a in matriz:
        y+=1
        for b in a:
            if nome == b:
                x+=matriz[y-1]
            return x