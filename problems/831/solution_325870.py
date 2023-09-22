def lingua_p(palavra):
    """dada uma palavra (em português), a função retorna esta mesma palavra traduzida para a língua do P, isto é, após
    cada vogal da palavra original, é inserida a sequência de letras 'p' mais a vogal original. A função ignora 
    diferenças entre maiúsculas e minúsculas, com retorno todo em minúsculas; str -> str"""
    str.lower(palavra)
    palavra_traduzida = ''
    for i in palavra:
        if i in 'aáâãeéêiíoóôuú':
            palavra_traduzida += i + 'p' + i
        else:
            palavra_traduzida += i
            
    return palavra_traduzida