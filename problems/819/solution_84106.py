def filtraMultiplos(lista,n):
    """Função que dada uma lista de números inteiros e um númrto inteiro(n), ira retornar uma nova lista apenas com os números multiplos de n que estão contidos na lista original.
    casos de teste:
    entrada:([1,3,6,9],9) saida:[9]
    entrada:([2,4,6,8],2) saida:[2,4,6,8]
    entrada:([14,21,6,8,47,56,77],7) saida:[14,21,56,77]
    assinatura list, int -> list"""
    nova_lista = []
    for x in lista:
        if x % n == 0:
            list.append(nova_lista,x)
    return nova_lista