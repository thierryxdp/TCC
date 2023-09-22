def lingua_p(palavra):
    palavra=str.lower(palavra)
    novo=palavra
    for x in palavra:
        if x in 'AEIOUaeiou':
            str.replace(novo,x,x+'p'+x)
    return novo