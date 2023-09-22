def repetidos(lista_num):
    """Recebe uma lista de números e retorna a quantidade de vezes que um
       elemento foi igual ao elemento anterior.
       list->int
       
       Parameters:
       lista_num: A lista de números que sera usada como base para a função."""
    i=1
    repeticoes=0
    while i<len(lista_num):
        if lista_num[i]==lista_num[i-1]:
            repeticoes=repeticoes+1
        i=i+1
    return repeticoes