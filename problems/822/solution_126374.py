def repetidos(lista_numeros):
    """Função que retorna o número de vezes que um elemento é igual ao anterior"""
    """Parâmetro de entrada:list"""
    """Parâmetro de saída:int"""
    contador=0
    acumulador=0
    while contador < len(lista_numeros):
        if lista_numeros[contador-1]==lista_numeros[contador]:
            acumulador+=1
        contador+=1
    return acumulador