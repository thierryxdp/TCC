def lingua_p(palavra):
    """Função que recebe como parâmetro uma palavra e retorna
       esta mesma palavra, em letras, traduzida para a língua 
       do P, ou seja, após cada vogal da palavra original é
       o caractere 'p' é inserido;
       string -> string"""
    palavra = str.lower(palavra)
    for letra in palavra:
        if letra in 'aeiou':
            indice = str.find(palavra,letra)
            trecho_palavra = palavra[:indice+1]
            palavra = palavra[indice+1:]
            palavra_traduzida = trecho_palavra + 'p' + palavra
    return palavra_traduzida