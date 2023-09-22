def busca(setor, lista_funcionarios):
    funcionarios_registrados = []
    
    for funcionario in lista_funcionarios:
        if funcionario[2] == setor:
            for dado in funcionario:
                if dado == setor:
                    funcionario.remove(dado)
            funcionarios_registrados.append(funcionario)
        else:
            pass
        
    return funcionarios_registrados