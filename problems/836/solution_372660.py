def busca(x,matriz):
    nome = ''
    registro = ''
    telefone = ''
    M = []
    for a in matriz:
        for b in a:
            if b == x:
                nome = matriz[matriz.index(a)][0]
                registro = matriz[matriz.index(a)][1]
                telefone = matriz[matriz.index(a)][3]
                M = M + [nome,registro,telefone]
    return M