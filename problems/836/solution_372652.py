def busca(x,matriz):
    nome = ''
    registro = ''
    telefone = ''
    for a in matriz:
        for b in a:
            if b == x:
                nome = matriz[matriz.index(a)][0]
                registro = matriz[matriz.index(a)][1]
                telefone = matriz[matriz.index(a)][3]
    
    return [nome,registro,telefone]