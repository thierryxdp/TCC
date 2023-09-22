def lingua_p(palavra):
    """essa função recebe uma palavra e retorna essa mesma 
    palavra, porém com uma letra p adicionada após cada vogal dessa palavra;
    str->str"""
    num_palavra=''
    for vogal in palavra:
        if vogal in 'aeiouAEIOUáéíõú':
            numpalavra= numpalavra+ vogal + 'p'+vogal 
        else:
            numpalavra= numpalavra+ vogal 
    return numpalavra