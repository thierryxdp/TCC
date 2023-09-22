def busca(setor,matriz):
    """ A funcao busca, recebe uma matriz como a do exemplo e faz uma busca por setor, ou seja, dado um nome de um setor da empresa, a funcao retorna os dados de todos os funcionarios daquele setor.
        
        Parameters:
            setor = setor o qual serão retornado os dados das pesoas
            matriz = matriz contendo os dados, referentes a nome, registro, setor e telefone, em formato de strig dos funcionários da empresa. Exemplo: ["Adalberto Ferreira", "566","Contabilidade", "(21)84564-5248"]

        Testes:
            busca ("Contabilidade", [["Adalberto Ferreira", "566","Contabilidade", "(21)84564-5248"], ["Juliana Vasconcelos", "465","RH, "(21)3555-4552"], ["Flavia Amorim", "465","Contabilidade", "(21)2134-4845']]) == [["Adalberto Ferreira", "566", "(21)84564-5248"],["Flavia Amorim", "465", "(21)2134-4845']]
            busca ([[26, 81, 39, 97, 19, 10, 51, 31, 22, 41], [15, 30, 7, 95, 5, 50, 20, 91, 56, 88], [65, 82, 87, 62, 77, 21, 3, 99, 1, 8], [92, 23, 89, 48, 38, 66, 9, 98, 83, 2], [6, 33, 16, 49, 11, 45, 12, 28, 46, 60], [68, 53, 44, 27, 42, 86, 13, 94, 4, 52]]) == (3, 1, 9)

        Returns:
            dados de todos os funcionários do setor escolhido.
            list --> list
    """
    resultado = []
    nlin = len(matriz)
    if nlin == 0:
        return resultado
    ncol = len(matriz[0])
    for i in range(nlin):
        if setor in matriz [i][2]:
            lista = []
            list.append(lista,matriz[i][0])
            list.append(lista,matriz[i][1])
            list.append(lista,matriz[i][3])
            list.append(resultado,lista)
    return resultado