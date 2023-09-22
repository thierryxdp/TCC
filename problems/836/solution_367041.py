def busca(setor,matriz):
    """ A funcao busca, recebe uma matriz como a do exemplo e faz uma busca por setor, ou seja, dado um nome de um setor da empresa, a funcao retorna os dados de todos os funcionarios daquele setor.
        
        Parameters:
            setor = setor o qual serão retornado os dados das pesoas
            matriz = matriz contendo os dados, referentes a nome, registro, setor e telefone, em formato de strig dos funcionários da empresa. Exemplo: ["Adalberto Ferreira", "566","Contabilidade", "(21)84564-5248"]

        Testes:
            busca ("Contabilidade", [["Adalberto Ferreira", "566","Contabilidade", "(21)84564-5248"], ["Juliana Vasconcelos", "465","RH, "(21)3555-4552"], ["Flavia Amorim", "465","Contabilidade", "(21)2134-4845"]]) == [["Adalberto Ferreira", "566", "(21)84564-5248"],["Flavia Amorim", "465", "(21)2134-4845"]]
            busca ("RH", [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"], ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"], ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]]) == [["Juliana Vasconcelos", "465", "(21)3555-4552"]]

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