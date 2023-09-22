def qtd_divisores(numero):
    "função que verifica quantos divisores um número tem."
    qtd = 0
    contagem = 0
    while contagem <= numero:
        if contagem > 0:
            if numero % contagem == 0:
                qtd += 1
        contagem +=1
    return qtd