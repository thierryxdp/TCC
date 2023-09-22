def lingua_p(palavra):
    """
    Função que recebe como parâmetro uma palavra(em português) e retorna a mesma palavra traduzida na língua do p
    Uma palavra foi traduzida para a língua do P quando, após cada vogal da palavra original, é inserida a sequência de letras 'p' mais a vogal original 
    """
    
    palavra = str.lower(palavra)
    
    for vogal in ['a','e','i','o','u','á','é','ú']:
            palavra = str.replace(palavra, vogal, vogal+'p'+vogal)
    return palavra