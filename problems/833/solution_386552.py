def conta_numero(num,matriz):
    conta= 0
    for linha in matriz:
        conta=conta+list.count(linha,num)
        return conta