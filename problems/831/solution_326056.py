def lingua_p(palavra):
    num=''
    for vogal in palavra:
        if vogal in 'aeiouAEIOUáéíõú':
            num=num+vogal+'p'+vogal
        else:
            num=num+vogal
    return num