def qtd_divisores(num):
    """Função que determina a quantidade de divisores de um número;
    int -> int"""
    listaDivisores = []
    listaNum = list(range(1, num +1))
    for i in listaNum:
        if num % i == 0:
            listaDivisores = listaDivisores + [num]
    return len(listaDivisores)