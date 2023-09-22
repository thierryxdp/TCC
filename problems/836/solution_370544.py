def busca(s,m):
    '''recebe uma matriz(m) como a do exemplo e o nome de um setor(s), e
    retorna os dados de todos os funcionários daquele setor
    Ex:[["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"],
    ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"],
    ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]]'''
    lista = []
    for i in m:
        if s in i[2] :
            del i[2]
            lista.append(i)
    return lista