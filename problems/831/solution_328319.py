def lingua_p(palavra):
    '''Retorna uma nova palavra na qual logo apos cada vogal da palavra original é inserida uma sequencia de 'p' mais a vogal;
       Entrada: str;
       Saida: str;
    '''
    palavra = palavra.lower()
    vogal = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
    lista = []
    for letra in palavra:
        if letra in vogal:
            list.append(lista, letra)
            list.append(lista, 'p')
            list.append(lista, letra)
        else:
            list.append(lista, letra)
    palavra = ''.join(lista)
    return palavra