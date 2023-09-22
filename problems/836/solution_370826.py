def busca(setores)->list:
    '''...'''
    matriz = [
        ['AdalbertoFerreira','566', 'Contabilidade', '(21)84564-5248'],
        ['JulianaVasconcelos','465', 'RH', '(21)3555-4552'],
        ['FlaviaAmorim','565', 'Contabilidade', '(21)2134-4845']]
    dados=[]
    
    for nome,registro,setor,telefone in matriz:
        if setor==setores:
            dados.append([nome,registro,setro,telefone])
    return dados