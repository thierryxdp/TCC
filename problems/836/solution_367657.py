def busca(setor, matriz):
    """Função que recebe um setor como string e uma matriz e retorna os funcionários que atuam no parâmetro 'setor'.
    str, list -> list"""
    funcionarios = []
    for lista_funcionario in matriz:
        if setor.title() in str(lista_funcionario[2]).title():
            funcionario_copia = lista_funcionario.copy()
            del funcionario_copia[2]
            funcionarios.append(funcionario_copia)
    if len(funcionarios) == 0:
        return 'Nenhum registro encontrado'
    else:
        return funcionarios