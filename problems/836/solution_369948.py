def busca(nome,matriz):
    x=''
    for a in matriz:
        for b in a:
            if nome == b:
                return matriz[a]