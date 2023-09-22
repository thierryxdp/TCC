def repetidos (numeros):
    "Função que recebe uma lista de numeros para que retorne, a quantidade de vezes que um elemento lista é igual ao elemento anterior; list ->int"
    indice = 0
    repetidos = 0 
    while indice < len(numeros):
        if numeros[indice] == numeros [indice - 1]:
            repetidos = repetidos + 1
        indice = indice + 1
        if len (numeros) == 2 and numeros [0] == numeros [1]: