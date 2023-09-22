def lingua_p(palavra):
    word=''
    for vogal in palavra:
        if str.lower(vogal) in 'aeiouáéíóú':
            vogal=vogal+'p'+vogal
        word=word+vogal
    return word