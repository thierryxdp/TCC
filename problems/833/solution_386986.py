def conta_numero(numero:int,matriz:list)->int:
    'recebe um numero inteiro e umamatriz e retorna quantas vezes esse numero aparece na matriz'
    contador = 0
    for i in matriz:
        contador += i.count(n)
    return contador