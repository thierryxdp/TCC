def posLetra(frase, letra, numero_ocorrencia):
    '''Função que recebe uma frase, uma letra e um número que 
    indica a ocorrência da letra na frase e retorna a posição
    que aquela ocorrência daquela letra se encontra dentro da frase.
    Caso tal ocorrência não exista, será retornado o valor -1.
    str, str, int -> int'''
    if str.count(frase, letra) < numero_ocorrencia:
            return -1
    i = 0
    contador_ocorrencias = 0
    while i < len(frase):
        if frase[i] == letra:
            contador_ocorrencias = contador_ocorrencias + 1
        if contador_ocorrencias == numero_ocorrencia:
            return i
        i = i + 1