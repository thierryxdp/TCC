def busca(nome,matriz):
    resultado = []
    
    for contato in matriz:
        for inf in contato:
            if nome in inf:
                resultato = resultado + contato
    return resultato