def fatorial(numero):
    """Função que dado um nº, calcule o fatorial deste nº.(Não usar a função 
    factorial do módulo math);
    int/float -> int/float"""
    contador = 1
    fat = 1

    while contador <= numero:
        fat *= contador
        contador += 1
        print(fat)

    return fat