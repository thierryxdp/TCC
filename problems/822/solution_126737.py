def repetidos(lista):
    """Função que recebe como entrada uma lista de números
    e retorna o numero de vezes que um elemento da lista é 
    igual ao elemento anterior"""
    repeticao = 0
    i = 0
    while i<len(lista)-1:
    	if lista[i]==lista[i=1]:
            repeticao=repeticao+1
        i=i+1
    return repeticao