def uppCons(frase):
    """ Transforma todas as consoantes da frase em maiúsculas.
    	str -> str
        
        Parameter:
        frase: Frase
        
        Returns:
        A frase com todas as consoantes maiúsculas.
    """
    i = 0
    lista = list(frase)
    lista1 = []
    while i < len(lista):
        if lista[i] in 'aáàãâeéêiíoóôuAÁÀÃEÉÊIÍOÓÔU;:-?,.!QWRTYPSDFGHJKLÇZXCVBNM ':
            lista1.append(lista[i])
        elif lista[i] in 'qwrtypsdfghjklçzxcvbnm':
            lista1.append(str.upper(frase[i]))
        i = i + 1
    return str.join('', lista1)