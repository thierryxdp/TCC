def busca(string, matriz):
    '''dada uma matriz com os dados dos funcionarios de uma empresa e uma str, retorna os funcionarios que atuam no setor informado
    str, list -> list'''
    funcionarios = []
    for func in matriz:
        if func[2] == string:
            novo = []
            for dado in func:
                if dado != string:
                    list.append(novo, dado)
            list.append(funcionarios, novo)
    return funcionarios