def busca(setor,matriz):

    """Retorna uma lista com todos os funcionarios encontrados na matriz de um setor dado por parametro;

    list, string -> list"""

    i = 0

    lista_retorno = []

    while i < len(matriz):

       if matriz[i][2] == setor:

           nome = matriz[i][0]

           registro = matriz[i][1]

           telefone = matriz[i][3]

           lista_retorno += [[nome,registro,telefone],]

       i += 1

    return lista_retorno