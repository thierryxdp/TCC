def lingua_p(palavra):
    """essa função recebe uma palavra em português e muda ela para a língua do P;
    str->str"""
    numpalavra=''
    for vogal in palavra:
        if vogal in 'aeiouAEIOUáéíõú':
            numpalavra= numpalavra+ vogal + 'p'+vogal 
        else:
            numpalavra= numpalavra+ vogal 
    return numpalavra