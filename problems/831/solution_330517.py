def lingua_p (palavra):
    vogal = ''
    for vogal in palavra:
        if (vogal in 'aeiouAEIOU'):
            x = palavra.replace ("e","epe").replace("a","apa").replace("i","ipi").replace("o","opo").replace("u","upu")
    return x