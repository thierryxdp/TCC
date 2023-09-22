def lingua_p(palavra):
    palavra = palavra.lower()
    palavra_p = []
    for i in palavra:
        if i in "aeiou":
            palavra_p.append(i+"p"+i)
        else:
            palavra_p.append(i)
            
    palavra_p = ''.join(palavra_p[:-1])
    return palavra_p