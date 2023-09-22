def busca(string,matriz):
    '''Recebe uma matriz com os dados de funcionários em forma de lista e uma string;
Retorna os dados de todos os funcionários que tenham tal string no registro;
list => list'''
    retorno = []
    for funcionario in matriz:
        if string in funcionario:
            retorno = retorno + [funcionario[0],funcionario[1],funcionario[3]]
    return retorno