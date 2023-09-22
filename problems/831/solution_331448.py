def lingua_p(palavra):
    '''
    Função que recebe uma palavra em português e retorna
    essa mesma palavra traduzida para a língua do P. A língua do P
    é quando após cada vogal da palavra original, é inserida a sequência
    de letras 'p' mais a vogal original.
    Retorna a resposta com todas as letras em minúsculas
    '''
    
    letras = list(palavra)
    for letra in letras:
        if letra in "aeiouáéíóúâêôûîAEIOUÁÉÍÓÚÂÊÎÔÛ":
            letras = letras.replace(letra,(letra+"p"+letra))
        final = ''.join(letras)       
    return final