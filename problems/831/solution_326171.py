def lingua_p(palavra):
    """recebe uma palavra e retorna a mesma na lingua do p a qual após cada vogal é inserida uma sequencia de letras 'p' mais a vogal original
    str->str"""
    for numero in range(len(palavra)):
        if palavra[numero] in "aeiouAEIOUáéíóÁÉÍÓÊêãõÃÕàÀ":
            a=numero+1
            palavra=palavra[:a]+'p'+palavra[numero]+palavra[a:]
        numero+=3
    return palavra