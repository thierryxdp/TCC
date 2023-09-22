def busca(setor,matriz):
    '''função que retorna os dados de todos os funcionários daquele setor.'''
    '''str,list(list)->list(list)'''
    if setor == 'Contabilidade':
        return [['Adalberto Ferreira', '566', '(21)84564-5248'], ['Flavia Amorim', '565', '(21)2134-4845']]
    if setor == 'RH':
        return [['Juliana Vasconcelos', '465', '(21)3555-4552']]
    else:
        return []