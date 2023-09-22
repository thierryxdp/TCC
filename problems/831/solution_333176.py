lingua_p(palavra):
    """funcao que recebe uma palavra como entrada e retorna 
    a palavra traduzida para a lingua do P. Uma palavra e traduzida
    para essa lingua quando, apos cada vogal da palavra, insere-se
    a sequencia de letras p mais a vogal original
    str -> str"""
    for j in range(0,len(palavra)+1):
        if palavra[j] in 'aeiouAEIOU':
            palavra[j] = palavra[j] + 'p'
    return str.lower(palavra)