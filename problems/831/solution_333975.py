def lingua_p(palavra):
    vogais=('aeiou')
    palavra=palavra.lower()
    palavra_p=''
    for l in palavra:
        palavra_p += 'p'
        if l in vogais:
            palavra_p+='p'+1
    return (palavra_p)