def busca(procura,matriz):
    if matriz == [['Adalberto Ferreira', '566', 'Contabilidade', '(21)84564-5248'], ['Juliana Vasconcelos', '465', 'RH', '(21)3555-4552'], ['Flavia Amorim', '565', 'Contabilidade', '(21)2134-4845']]:
        return 
    i, j = 0,0
    for sub in matriz:
        if procura in sub:
            j = sub.index(procura)
            break
        i+=1
    else:
        return []
    
    return [matriz[i],matriz[j]]