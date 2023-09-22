def lingua_p(palavra):
    vogal="aeiou"
    l=" "
    for x in palavra:
        if x in vogal:
            l+=(x+"p"+x)
        else:
            l+=x
    return l