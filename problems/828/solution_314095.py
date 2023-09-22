def primo(n):
    """
    Função que dado um inteiro positivo retorna um valor
    booleano se for primo.(True se sim. False se não.)
    """
    qts_divisoes=0
    lista_primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                  31,37, 41, 43, 47, 53, 59, 61, 67, 71]
    list.append(lista_primos,n)
    list.sort(lista_primos)
    
    for i in lista_primos[:list.index(lista_primos,n)]:
        if n%i==0:
            qts_divisoes+=1
    if qts_divisoes==0:
        return True
    else:
        return False