def lingua_p(palavra):
    for vogal in palavra:
        if vogal in 'AEIOUaeiou':
            vogal='p'
    return palavra