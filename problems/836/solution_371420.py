def busca(entrada,matriz):
    contato=[]
    if entrada=='contabilidade':
        contato= contato+matriz[0]+matriz[-1]
        return contato
    if entrada=='RH':
        contato= contato+matriz[1]
        return contato
    else:
        return contato