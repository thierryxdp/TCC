matriz = [
    ['AdalbertoFerreira','566', 'Contabilidade', '(21)84564-5248'],
    ['JulianaVasconcelos','465', 'RH', '(21)3555-4552'],
    ['FlaviaAmorim','565', 'Contabilidade', '(21)2134-4845']
]

def busca(setor_busca)->list:
    '''...'''
    matriz = [
    ['AdalbertoFerreira','566', 'Contabilidade', '(21)84564-5248'],
    ['JulianaVasconcelos','465', 'RH', '(21)3555-4552'],
    ['FlaviaAmorim','565', 'Contabilidade', '(21)2134-4845']
]
    dados=[]
    
    for nome,registro,setor,telefone in matriz:
        if setor==setor_busca:
            dados.append([nome,registro,telefone])
    return dados
print(busca('contabilidade'))