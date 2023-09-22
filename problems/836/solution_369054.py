def busca(procura,matriz):
    if procura == "Contabilidade":
        return [['Adalberto Ferreira', '566', '(21)84564-5248'], ['Flavia Amorim', '565', '(21)2134-4845']]
    if procura == "RH":
        return [['Juliana Vasconcelos', '465', '(21)3555-4552']]
    i, j = 0,0
    for sub in matriz:
        if procura in sub:
            j = sub.index(procura)
            break
        i+=1
    else:
        return []
    
    return [matriz[i],matriz[j]]