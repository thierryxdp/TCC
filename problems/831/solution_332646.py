def lingua_p(palavra):
    nova_palavra = str.lower(palavra)
    ret = ""
    i = 0
    while i < len(nova_palavra):
        if nova_palavra[i] in 'aeiou':
            ret += nova_palavra[i]+"p"+nova_palavra[i]
        else:
            ret += nova_palavra[i]

        i = i + 1
    return ret