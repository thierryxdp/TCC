def lingua_p(palavra):
    """recebe uma palavra e retorna a mesma na lingua do p a qual após cada vogal é inserida uma sequencia de letras 'p' mais a vogal original
    str->str"""
    indice=0
    for numero in range(len(palavra)):
        if palavra[indice] in "aeiouAEIOUáéíóÁÉÍÓÊêãõÃÕàÀ":
            a=indice+1
            palavra=palavra[:a]+'p'+palavra[numero]+palavra[a:]
            indice+=2
        else:
            indice+=1
    return palavra