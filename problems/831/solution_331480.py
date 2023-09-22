def lingua_p(palavra):
    for vogal in palavra:
        if vogal in 'AEIOUaeiou':
            vogal = vogal + "p" + vogal
    return vogal + vogal