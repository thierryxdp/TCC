def lingua_p(palavra):
    for n in palavra:
        if n in 'AEIOUaeiou':
            palavra=palavra[:palavra.index(n)]+'p'+n+palavra[palavra.index(n)+1:]
    return palavra