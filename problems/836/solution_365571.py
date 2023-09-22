def busca(string, matriz):
    '''dada uma matriz com dados dos funcionarios de uma empresa e uma string, retorna a ficha dos funcionarios que atuam no setor informado
    str, list -> list'''
    funcionarios = []
    for func in matriz:
        if func[2] == string:
            list.append(funcionarios, func)
    return funcionarios