def lingua_p(palavra):
    vogais=('aeiouáéíóúàèìòùâêôã')
    LC_palavra=palavra.lower()
    palavra_p=''
    for l in LC_palavra:
        palavra_p += l
        if l in vogais:
            palavra_p+='p'
            palavra_p+= l
    return (palavra_p)