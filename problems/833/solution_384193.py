#Entrada: Um número
#1)Precisamos procurar na matriz qual elemento é igual ao número da entrada
#2)Ao encontrar, precisamos contar, a cada elemento encontrado
#2.2) adicionamos um a nossa contagem
#3)Ao final, retornamos o resultado dessa contagem
def conta_numero(numero:int,matriz:list)->int:
    contador=0
    for termo in matriz:
        for elemento in termo:
            if elemento == numero:
                contador += 1
    return contador