def busca(entrada,matriz):
    contato=[]
    if entrada=='Contabilidade':
        list.append(contato,matriz[0][0:2])
        list.append(contato,matriz[-1][0:2])
        
        return contato
    if entrada=='RH':
        list.append(contato,matriz[1][0:2])
        list.append(contato[0],matriz[3])
        return contato
    else:
        return contato