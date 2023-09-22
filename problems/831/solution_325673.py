def lingua_p(palavra):
    i=0
    while i<len(palavra):
        if palavra in 'AEIOUaeiou':
            return palavra+'p'