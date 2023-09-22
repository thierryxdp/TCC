def busca(s,m):
    """função que recebe um setor (s) e uma matriz (m), onde cada linha
    representa uma informação de um funcionário de uma empresa, tal que
    exista quatro colunas de informações em string, sendo a ordem: 
    <nome>,<registro>,<setor>,<telefone>. E analisa quais são os
    funcionários que pertencem àquele setor, e deve retornar todos os
    seus dados;
    matriz->lista"""
    linhas = range(len(m))
    colunas = range(len(m[0]))
    funcionarios = []
    for i in linhas:
        for j in colunas:
            if s==m[i][j]:
                list.append(funcionarios,m[i])
        list.remove(m[i],m[i][j-1])
    return funcionarios