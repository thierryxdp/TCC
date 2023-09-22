def lingua_p(palavra):
    """recebe uma palavra e retorna a mesma palavra traduzida para a lingúa do p, quando após cada vogal da palavra é colocada a sequência 'p' + vogal original
    str -> str"""
    separador_de_letras = list(palavra_minuscula)
    conta_letras = list.count(separador_de_letras, 'a') + list.count(separador_de_letras, 'e') + list.count(separador_de_letras, 'i') + list.count(separador_de_letras, 'o') + list.count(separador_de_letras, 'u') + list.count(separador_de_letras, 'é') + list.count(separador_de_letras, 'á') + list.count(separador_de_letras, 'ó') 
    contador = 0
    for numero in range(len(separador_de_letras) + conta_letras):
        if separador_de_letras[contador] in 'aeiouáéíóú':
            list.insert(separador_de_letras, contador + 1, 'p' + separador_de_letras[contador])   
        contador = contador + 1
    ppalavra = str.join('', separador_de_letras)
    return ppalavra