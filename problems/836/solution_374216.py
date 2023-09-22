def busca(setor,funcionarios_e_dados):
    """dada uma string setor de entrada, e uma matriz em forma de lista
    na qual as linhas recebem como entrada as strings na ordem: nome do funcionario,
    registro, setor, e telefone do funcionário, retorna uma nova lista com os dados
    de todos funcionarios que trabalham no setor de entrada
    str, list --> list"""
    funcionarios_setor=[]
    for funcionario in funcionarios_e_dados:
        if setor in funcionario:
            funcionarios_setor=funcionarios_setor+[funcionario]
    return funcionarios_setor