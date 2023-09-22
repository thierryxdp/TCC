def busca(setor,ls):
    """Essa função serve para identificar quais funcionários trabalham
    no setor específico de interesse (setor), dada a matriz (ls).
    str,list->list"""
    nova_lista = []
    for listas in ls:
        if listas[2] == setor:
            del listas[2]
            nova_lista.append(listas)
    return nova_lista

#busca("RH",[["Pessoa 1","Número 1", "RH", "Telefone 1"],["Pessoa 2","Número 2", "Contabilidade", "Telefone 2"]]) == [['Pessoa 1', 'Número 1', 'Telefone 1']]
#busca("RH",[["Pessoa 1","Número 1", "RH", "Telefone 1"],["Pessoa 2","Número 2", "Contabilidade", "Telefone 2"],["Pessoa 3","Número 3", "RH", "Telefone 3"],["Pessoa 4","Número 4", "RH", "Telefone 4"]]) == [['Pessoa 1', 'Número 1', 'Telefone 1'], ['Pessoa 3', 'Número 3', 'Telefone 3'], ['Pessoa 4', 'Número 4', 'Telefone 4']]
#busca("Atendimento ao cliente",[["Pessoa 1","Número 1", "RH", "Telefone 1"],["Pessoa 2","Número 2", "Contabilidade", "Telefone 2"]]) == []