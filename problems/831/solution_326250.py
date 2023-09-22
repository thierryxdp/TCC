def lingua_p(palavra):
    '''Função que recebe uma palavra (em português) e retorna esta mesma palavra
traduzida para a língua do P. Uma palavra foi traduzida para a lígua do P quando,
após cada vogal da palavra original, é inserida a sequência de letras p mais a
vogal original.
    str -> str
    '''
    lista_vogais=['a','e','i','o','u','ã','õ','é','ú','í','ó','á']
    palavra = str.lower(palavra)
    for vogal in lista_vogais:
        if vogal in palavra:
            palavra = str.replace(palavra,vogal,vogal+'p'+vogal)
    return palavra