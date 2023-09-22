def lingua_p(palavra):
    palavra = str.lower(palavra)
    bruh = ""
    x = 0
    while x<len(palavra):
        if palavra[x] in "aeiou":
            bruh = bruh + palavra[x] + "p" + palavra[x]
        else:
            bruh = bruh + palavra[x]
        x = x+1
    return bruh