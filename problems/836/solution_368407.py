def busca(setor,tabela_info):
    """Recebe o nome de um setor e uma tabela com as informações dos funcionarios
       (as linhas da tabela contem nome, registro, setor e telefone de um funcionario,
       todas as entradas da matriz devem estar em formato string)e retorna os dados
       de todos os funcionários daquele setor.
       str,list->list

       Parameters:
       setor: O nome do setor em formato string.
       tabela_info: Uma tabela com as informações dos funcionarios(as linhas da tabela
       contem nome, registro, setor e telefone de um funcionario, todas as entradas da
       matriz devem estar em formato string)"""
    funcionarios=[]
    for funcionario in tabela_info:
        if setor in funcionario:
            list.append(funcionarios,funcionario)
    for i in funcionarios:
        list.remove(i, setor)
    return funcionarios