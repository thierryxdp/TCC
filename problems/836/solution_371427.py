def busca(entrada,matriz):
    contato=[]
    if entrada=='Contabilidade':
        list.append(contato,matriz[0][0:2])
        list.append(contato[0],matriz[0][3])
        list.append(contato,matriz[-1][0:2])
        list.append(contato[-1],matriz[-1][3])
        
        return contato
    if entrada=='RH':
        list.append(contato,matriz[1][0:2])
        list.append(contato[0],matriz[1][3])
        return contato
    else:
        return contato