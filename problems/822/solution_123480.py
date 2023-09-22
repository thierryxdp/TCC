def repetidos(lista_de_numeros):
    numero_anterior = 0
    uma_vez_sim_outra_nao = 0
    ocorrencias_repetidas = 0
    for numero in lista_de_numeros:
        if uma_vez_sim_outra_nao % 2 == 0 and uma_vez_sim_outra_nao != 0 and uma_vez_sim_outra_nao != 2:
            numero_anterior = numero
        if numero_anterior == numero:
            ocorrencias_repetidas += 1
        uma_vez_sim_outra_nao += 1
    return ocorrencias_repetidas