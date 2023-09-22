def busca(x,matriz):
    nomes = []
    registros = []
    telefones = []
    for a in matriz:
        for b in a:
            if b == x:
                nomes = nomes + [matriz[matriz.index(a)][0]]
                registros = registros + [matriz[matriz.index(a)][1]]
                telefones = telefones + [matriz[matriz.index(a)][3]]
    dados1 = [nomes[0],registros[0],telefones[0]]
    dados2 = [nomes[1],registros[1],telefones[1]]                    
    
    return [dados1,dados2]