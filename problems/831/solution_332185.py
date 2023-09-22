def lingua_p(palavra):
    novo=palavra
    for x in palavra:
        if x in 'AEIOUaeiou':
            novo=str.replace(novo,x,x+'p'+x,str.count(palavra,x))
    return novo