def busca(setor,funcionarios):
    """ funcao que recebe como entrada um setor da empresa e
    uma matriz com os dados dos funcionarios, e retorna uma
    lista com as informações de todos os funcionarios que 
    trabalham naquele setor;
    str; list(list) -> list(list)"""
    
    lista = []
    for i in range(len(funcionarios)):
        if funcionarios[i][2] == setor:
            info = funcionarios[i]
            del info[2]
            lista += [info]
    return lista