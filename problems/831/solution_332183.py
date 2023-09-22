def lingua_p(palavra):
    palavra=str.lower(palavra)
    novo=palavra
    for x in palavra:
        if x in 'AEIOUaeiou':
            novo=replace(novo,x,x+'p'+x)
    return novo