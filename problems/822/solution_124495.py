def repetidos(lista):
    """Função que recebe uma lista com varios numeros e retorna a quantas vezes a sequencia aparece.
    parametros:lista->int"""
    i = 0
    iguais = 0
    while i < len(lista):
        if lista[i] == lista[i + 1]:
            iguais +=1
    	indice += 1
    return iguais