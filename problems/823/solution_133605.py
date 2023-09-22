def faltante(lista):
    """Função que que retorna qual e a peça que falta para terminar o quebra-cabeça.
    parametros: lista->int"""
    anterior = lista[-1] - 1
    posterior = 1
    while anterior != -1:
        if posterior in lista:
            posterior += 1
        else:
            return posterior