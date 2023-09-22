empresa=[['Adalberto Ferreira', '1091982', 'Contabilidade', '(21)99281 − 2983'],
['Juliana Vasconcelos', '1111722', 'RecursosHumanos', '(21)99848 − 1902'],
['Flavia Amorim', '1128938', 'Contabilidade', '(22)99273 − 9404']]

def buscarSetor(empresa, setor):
    ''' funcao que retorna a lista com os dados do pessoal da empresa
list, str -> list'''
    ret =[]
    for i in empresa:
        if(i[2] == setor):
            cp = i.copy()
            cp.remove(setor)
            cp.append(cp)
    return ret