def lingua_p(palavra):
    for n in palavra:
        if n in 'AEIOUaeiou':
            palavra=palavra+'p'+n
    return palavra