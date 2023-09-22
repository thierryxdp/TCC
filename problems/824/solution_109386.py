def ConsoantesMaiusculas(frase):

    """Digamos que queremos transformar as consoantes de qualquer frase fornecida
        transformando-as em maiúsculas, caso não sejam. A frase alterada terá o mesmo tamanho
        e com as vogais  sempre em minúsculas e como já dito, as consoantes se transformarão
        em maiúsculas.
        A string frase[i] não pode ser atribuida para se transformar em maiúsculas, por isso
        devemos atribuir à uma nova variável.

        str -> str
    """

    i = 0
    frase_alterada = ''

    while i < len(frase):

        letra = frase[i]
        
        if frase[i] not in 'AEIOUaeiou':
            
            letra = str.upper(letra)
            
        frase_alterada = frase_alterada + letra
        
        i = i + 1
        
    return frase_alterada