def busca(setor, matriz):
    '''funçao dado uma matriz com dados de funcionarios faz uma busca pelo setor e retorna os dados dos funcionario desse setor
    str, list -> list'''
    resultado = []
    for funcionario in matriz:
        if setor in funcionario:
            pessoa = [i[0], i[1], i[3]]
            resultado += [pessoa]
    return resultado