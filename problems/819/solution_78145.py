def filtraMultiplos(lista,numero):
    " Lista onde ficara amarazenados os múltiplos "
    divisiveis = []
    " Contador para o while "
    contador = 0
    " Enquanto o contador for menor que o tamanho da lista o while irar continuar "
    while contador < len(lista):
        " Verifica cada número da lista se e multiplo do numero "
        if lista[contador]%numero == 0:
            " Adiciona na lista divisiveis pelo numero de entrada "
            list.append(divisiveis,lista[contador])
            " Soma 1 numero ao contador a cada verificação "
        contador += 1
        " Retornar os multiplos do numero de entrada "
    return divisiveis