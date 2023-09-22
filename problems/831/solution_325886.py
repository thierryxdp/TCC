def lingua_p(palavra):
    """Para retornar uma frase com a língua do p,
    quando o p é inserido após uma vogal, digite;
    str->str"""
    npalavra=''
    for v in palavra:
        if v in 'aeiouAEIOUáéíõú':
            npalavra= npalavra+ v + 'p'+v
        else:
            npalavra= npalavra+ v
    return npalavra