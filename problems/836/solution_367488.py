def busca(cargo, matriz):
    """Essa funcao recebe como argumento um cargo a ser
       procurado numa matriz, tambem recebida como argumento.
       str, list -> list"""
    dados_funcionarios = []
    for funcionario in matriz:
        if cargo.lower() == funcionario[2].lower():
            dados_funcionarios.append(funcionario)
    return dados_funcionarios