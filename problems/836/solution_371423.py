def busca(entrada,matriz):
    contato=[]
    if entrada=='Contabilidade':
        list.append(contato,matriz[0][0:2][3])
        list.append(contato,matriz[-1][0:2][3])
        
        return contato
    if entrada=='RH':
        contato= contato+matriz[1]
        return contato
    else:
        return contato