def busca(entrada,matriz):
    contato=[]
    if entrada=='contabilidade':
        list.append(contato,matriz[0][0:2])
        list.append(contato,matriz[0][3])
        list.append(contato,matriz[-1][0:2])
        list.append(contato,matriz[-1][3:])
        return contato
    if entrada=='RH':
        contato= contato+matriz[1]
        return contato
    else:
        return contato