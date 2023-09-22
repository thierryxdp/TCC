def maiores(listaNumeros, n):
    """função que dada uma lista e um número inteiro 'n', retorne uma outa lista com os valores na lista original maiores que 'n'; list,int -->list"""
    if n not in listaNumeros:
        listaNumeros.append(n)
        listaNumeros.sort()
        x = listaNumeros.index(n)
        sublista = listaNumeros[x+1:]
        rep = sublista.count(n)
        return sublista[rep:]
    def aci