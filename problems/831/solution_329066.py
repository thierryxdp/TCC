def lingua_p(palavra):
    """Função que recebe como parâmetro uma palavra e retorna
       esta mesma palavra, em letras, traduzida para a língua 
       do P, ou seja, após cada vogal da palavra original, é
       inserida a sequência de letras 'p' mais a vogal original;
       string -> string"""
    palavra = str.lower(palavra)
    for letra in palavra:
        if letra in 'aeiouáéíóú' and letra == palavra[0]:
            indice = str.find(palavra,letra)
            palavra= palavra[:indice+1] + 'p' + letra + palavra[indice+1:]
        else:
            indice = str.find(palavra[indice+3],letra)
            palavra= palavra[:indice+1] + 'p' + letra + palavra[indice+1:]
    return palavra