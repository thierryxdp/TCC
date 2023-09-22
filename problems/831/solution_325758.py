def lingua_p(palavra):
    proxima=0
    for letra in palavra:
        if palavra[proxima] in ['a','e','i','o','u']:
            ppalavra=str.replace (palavra,palavra[proxima],(palavra[proxima]+'p'+palavra[proxima]))
            proxima=proxima+1
            return ppalavra
        else:
            return palavra