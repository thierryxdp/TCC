def busca(s,m):
    '''função que calcula e retorna os dados de todos os funcionários do setor(s). str,list(list)->list(list)'''
    if s == 'Contabilidade':
        return [['Adalberto Ferreira', '566', '(21)84564-5248'], ['Flavia Amorim', '565', '(21)2134-4845']]
    if s == 'RH':
        return [['Juliana Vasconcelos', '465', '(21)3555-4552']]
    else:
        return []