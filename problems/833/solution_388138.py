def conta_numero(numero,matriz):
    '''
    Funcao que retorna a qtd de vezes que um numero inteiro
    aparece numa matriz de entrada com inteiros, de qualquer tamanho
    int,list->int
    '''
    contador=0
    for vetor_confere in range(len(matriz)):
        
        ultimo_elem_lista=matriz[vetor_confere]
        for num_contar in range(len(ultimo_elem_lista)):
            if ultimo_elem_lista[num_contar]==numero:
                contador=contador+1
            else:
                contador
    return contador