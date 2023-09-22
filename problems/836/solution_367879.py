def busca(setor,matriz):
    'Dada uma matriz com os dados dos funcionários e um setor, retorna uma lista com os dados dos funcionários do setor. Entrada: list[list]. Saída: list[list]'.
    resultado=[]
    for info in matriz:
        for busca in info[2]:
            if busca==setor:
                list.append(resultado,del info[2])
    return resultado