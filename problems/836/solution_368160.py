def busca(setor, matriz): 
    '''str + list(list) -> list (list)'''
    funcionariosEncontrados = []
    for funcionario in matriz:
        if funcionario[2] == setor: #Terceira posição por conta da posição do setor no modelo matricial
            inf = []
            for dado in funcionario:
                if dado != funcionario[2]:
                    inf.append(dado)
            funcionariosEncontrados.append(inf)

    return funcionariosEncontrados