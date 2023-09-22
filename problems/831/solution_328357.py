def lingua_p(palavra):
    """Retorna uma palavra para a língua do P, ou 
    seja após cada vogal da palavra original, é 
    inserida a sequência de letras 'p' mais a 
    vogal original;str->str"""
    nova=''
    palavra=str.lower(palavra)
    for i in range(len(palavra)):
        if ('A'in palavra[i] or 'a'in palavra[i] or 'E'in palavra[i] or 'e'in 
        palavra[i] or 'I'in palavra[i] or 'i'in palavra[i] or 'O'in 
        palavra[i] or 'o'in palavra[i] or 'U'in palavra[i] or 'u'in 
        palavra[i] or 'Á'in palavra[i] or 'á'in palavra[i] or 'Ã'in
        palavra[i] or 'ã'in palavra[i]or 'É'in palavra[i] or 'é'in palavra[i] or 'Í'in
        palavra[i] or 'í'in palavra[i] or 'Ú'in palavra[i] or 'ú'in
        palavra[i] or 'Ó'in palavra[i] or 'ó'in palavra[i] or 'Õ'in
        palavra[i] or 'õ'in palavra[i]):
            nova=nova+'p'+palavra[i]
        else:
            nova=nova+palavra[i]
    return nova