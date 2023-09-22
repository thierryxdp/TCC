def repetidos(listadenumeros):
    """Função que recebe uma lista de números e retorna o número de vezes 
       que o elemento da lista é igual ao elemento anterior.
       list -> int
       
       Parâmetros:
       listadenumeros: Lista de números que será analisada pela função.
       
       returns: O número de vezes que o elemento da lista é igual ao 
                elemento anterior.
    """
    contador = 0
    ocorrencias = 0
    while contador < len(frase):
        if frase[contador - 1] == frase[contador]:
            ocorrencias = ocorrencias + 1
        contador = contador + 1
    return ocorrencias