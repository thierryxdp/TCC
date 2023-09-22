#Questão 2
def qtd_divisores(num):
    """Função que determina a quantidade de divisores de um número;
    int -> int"""
    listaDivisores = []
    indice = 0
    listaNum = list(range(1, num +1))
    for i in listaNum:
        if num % listaNum[indice] == 0:
            listaDivisores = listaDivisores + [num]
        indice += 1
    return len(listaDivisores)