def lingua_p(palavra):
    ''' Função que recebe uma palavra em forma de string 
    (em português), e retorna tal palavra traduzida para
    a língua do pe: após cada vogal é acrescida a letra 
    "p" mais a vogal.
    Entrada: str
    Retorno: str '''
    
    palavra_traduzida = ''
    for letra in str.lower(palavra):
        if letra in "aeiouáéíóúâêôãà":
            palavra_traduzida = palavra_traduzida + letra + "p" 
        palavra_traduzida = palavra_traduzida + letra
    return palavra_traduzida