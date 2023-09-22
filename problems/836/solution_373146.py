def busca(setor,infos):
    '''Essa funcao recebe de entrada o nome de um setor de 
    uma empresa e uma matriz de informacoes a respeito de 
    todos os funcionarios da empresa (nome, registro, setor 
    e telefone) e realiza uma busca por setor.
    Ou seja, o retorno eh uma lista com os dados de todos os
    funcionarios pertencentes ao setor indicado na entrada.
    str, matriz (str) -> lista'''

    funcionarios = []

    for funcionario in infos:
        area = funcionario[2]
        if area == setor:
            copia_funci = list.copy(funcionario)
            del copia_funci[2]
            funcionarios += [copia_funci]
    return funcionarios

#casos de teste
# infos = [['marcia silva', '1234567', 'admnistracao', '(21)91234-5678'],
# ['adriana moreira', '8901234', 'recursos humanos', '(21)93333-4444'],
# ['carlos eduardo', '1367901', 'diretoria', '(21)92123-2425'],
# ['Ana Santos', '8765432', 'TI', '(21)96543-8765'],
# ['Silvia Maria', '9650234', 'recursos humanos', '(21)95476-9878']]

# busca('recursos humanos',infos) == 
# == [['adriana moreira', '8901234', 'recursos humanos', '(21)93333-4444'],
# ['Silvia Maria', '9650234', 'recursos humanos', '(21)95476-9878]]

# busca('diretoria',infos) == 
# == [['carlos eduardo', '1367901', 'diretoria', '(21)92123-2425']]

# busca('marketing',infos) == []