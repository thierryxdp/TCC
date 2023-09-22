def busca(nome,matriz):
    resultado = []
    for palavra in matriz:
        
        for c in palavra:
            if c == nome:
                del palavra[2]
                list.append(resultado, palavra)
    return resultado