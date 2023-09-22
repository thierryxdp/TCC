def busca (setor: string, funcionarios: list) -> list:
    """Retorna todos funcionarios que trabalham no setor.
    	1. Parâmetros:
	        setor: setor que se pretende buscar os funcionarios.
    	    funcionarios: matriz cujas linhas correspondem a um funcionário 
            e as colunas são seus dados.
    """
    qtd_funcionarios = len(funcionarios)
    funcionarios_que_trabalham_no_setor = []
    for funcionario in funcionarios:
        if funcionario[2] == setor:
            funcionarios_que_trabalham_no_setor.append([funcionario[0],funcionario[1],funcionario[3]])
    return funcionarios_que_trabalham_no_setor