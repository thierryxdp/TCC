lista_funcionarios = [
    ['AdalbertoFerreira','566', 'Contabilidade', '(21)84564-5248'],
    ['JulianaVasconcelos','465', 'RH', '(21)3555-4552'],
    ['FlaviaAmorim','565', 'Contabilidade', '(21)2134-4845']
]

def busca(lista_funcionarios:list, setor: str)->list:
    '''...'''
    
    for i in lista_funcionarios:
        if (setor) in (lista_funcionarios[0]):
            return lista_funcionarios[0]
        if (setor) in (lista_funcionarios[1]):
            return lista_funcionarios[1]
        if (setor) in (lista_funcionarios[2]):
            return lista_funcionarios[2]