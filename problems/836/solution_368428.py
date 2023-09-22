def busca(setor: str, matriz: list) -> list:
    """Recebe uma matriz contendo as informações dos funcionários de uma
       empresa, no qual cada linha é a informação de um funcionário, e o nome de
       um setor da empresa e retorna os dados de todos os funcionários daquele
       setor

       Parameters:
       setor: String que representa o setor a ser analisado
       matriz: Matriz representada por uma lista de lista, no qual cada lista
       representa uma linha e cada lista de lista representa uma coluna. Cada
       linha da matriz representa um funcionário e cada coluna da matriz
       representa, respectivamente, o nome do funcionário, registro, setor e
       telefone desse funcionário

       Return:
       Dados os parâmetros "setor" e "matriz", retorna os dados de todos os
       funcionários que estão no parâmetro "matriz" do setor do parâmetro
       "setor"

       Examples:
       busca("Contabilidade", [["Adabelto Ferreira", "566", "Contabilidade",
       "(21)84564-5248"], ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"],
       ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]]) ==
       [['Adabelto Ferreira', '566', '(21)84564-5248'], ['Flavia Amorim', '565',
       '(21)2134-4845']]
    """

    dados = []
    lista = []

    for i in range(len(matriz)):
        lista = []
        if setor == matriz[i][2]:
            list.append(lista, matriz[i][0])
            list.append(lista, matriz[i][1])
            list.append(lista, matriz[i][3])
            list.append(dados, lista)

    return dados