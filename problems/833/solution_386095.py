def conta_numero(numero, matriz):
    """Dado um número inteiro e uma matriz de inteiros, a função retorna quantas vezes
       n aparece em m.
       int, list -> int"""
    n_list = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == n:
                list.append(n_list, n)
    return len(n_list)
#Testes:
#m = [[1, 2, 3], [2, 3, 4]]
#conta_numero(2, m)--> 2
#conta_numero(4, m)--> 1
#conta_numero(0, m)--> 0