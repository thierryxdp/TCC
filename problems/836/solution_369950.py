def busca(nome,matriz):
    x=''
    y=0
    for a in matriz:
        y+=1
        for b in a:
            if nome == b:
                return matriz[y-1]