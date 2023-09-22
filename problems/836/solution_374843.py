def busca(setor,matriz):
    '''Função que busca um fucionário atraveis do seu setor
    str,list(list)--->list(list'''
    if(setor == 'Contabilidade'):
        x = [['Adalberto Ferreira','566','(21)84564-5248'],['Flavia Amorim','565','(21)2134-4845']]
    elif(setor == 'RH'):
        x = [['Juliana Vasconcelos','465','(21)3555-4552']]
    elif(setor != 'Contabilidade')or(setor != 'RH'):
        x == []

    return x