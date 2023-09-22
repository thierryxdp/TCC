def repetidos(ls):
    '''Função que recebe uma lista de números como entrada, e retorna o número de vezes 
que um elemento da lista é igual ao elemento anterior.
Assinatura: ls -> int
Casos de teste:
repetidos([24, 14, 9, 29, 5, 13, 27, 22, 8, 18, 18, 15, 12, 12]) == 2
repetidos([20, 20, 1, 29, 26, 26, 7, 7]) == 3
repetidos([4, 26, 11, 11, 23, 19, 28, 5, 20, 10]) == 1
'''
    c = 0                                      ## new_ls = []
    fat = ls[1:]                               ## repetidos = []
    for i in range(len(fat)):                   ## for n in ls:
        if ls[i] == fat[i]:                    ##     if n in new_ls:
            c += 1                             ##         repetidos.append(n)
    return c                                   ##     else:
                                               ##         new_ls.append(n)
                                               ## return len(set(repetidos))