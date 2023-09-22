empresa=[['AdalbertoFerreira', '566', 'Contabilidade', '(21)84564-5248'],
['JulianaVasconcelos', '465', 'RH', '(21)3555 − 4552'],
['FlaviaAmorim', '565', 'Contabilidade', '(21)2134-4845']]
def busca(setor,empresa):
    ''' funcao que retorna a lista com os dados do pessoal da empresa
list, str -> list'''
    ret =[]
    for i in empresa:
        if(i[2] == setor):
            cp = i.copy()
            cp.remove(setor)
            ret.append(cp)
    return ret