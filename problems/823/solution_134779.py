def faltante(lista):
    """Dado um quebra-cabeça com N peças, a função verifica qual 
    peça está faltando no quebra-cabeça. Deve ser dado como parâmetro
    uma lista com as N peças do quebra-cabeça, enumeradas do número incial até 
    o desejado.
    	Exemplo: [1,3,2,5]. A função vai descobrir que está faltando a peça de
    número 4;
    	list --> int"""
    i = 0
    numeroQueFalta = 0
    numeroQueFaltaComIncio1 = 0
    list.sort(lista)
    numeroFinal = lista[-1] + 1
    numeroInicio = lista[0]
    parametro = list(range(numeroInicio,numeroFinal))
    while i < len(lista):
        if lista[i] != parametro[(i)]:
            return numeroQueFalta + parametro[(i)]
        else:
            if lista[0] != 1:
                return lista[0] - 1
            if lista[0] == 1:
                numeroQueFaltaComIncio1 = lista[-1] + 1
        i = i + 1
    return numeroQueFaltaComIncio1