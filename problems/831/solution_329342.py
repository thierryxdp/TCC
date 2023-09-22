def lingua_p(palavra):
    '''função que recebe como entrada a string 'palavra' e retorna uma nova
string onde, após cada vogal da string original, é adicionada a letra p mais a
vogal anterior, estando a string toda em letras minúsculas; string->string'''

    baixo=str.lower(palavra)
    final=''

    for x in baixo:
        final=final + x
        if x in 'aeiouáéíóúâêîôûãõà':
            final=final+'p'+x
    return final