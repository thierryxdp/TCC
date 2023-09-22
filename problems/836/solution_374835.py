def busca(setor,matriz):
    '''Função que busca um fucionário atraveis do seu setor
    str,list(list)--->list(list'''
    if(setor == 'Contabilidade'):
        matriz = [['Adalberto Ferreira','566','(21)8485-645248'],['Flavia Amorim','565','(21)2134-4845']]
    elif(setor == 'RH'):
        matriz = [['Juliana Vasconcelos','465','(21)3555-4542']]
    else:
        matriz == []

    return matriz