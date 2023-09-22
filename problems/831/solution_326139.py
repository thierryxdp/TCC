def lingua_p(palavra):
    """recebe uma palavra e retorna a mesma na lingua do p a qual após cada vogal é inserida uma sequencia de letras 'p' mais a vogal original
    str->str"""
    for numero in len(palavra):
        if palavra[numero] in "aeiouAEIOUáéíóÁÉÍÓÊêãõÃÕàÀ":
            palavra=palavra[:numero]+p+palavra[numero]+palavra[numero+1:]
    return palavra