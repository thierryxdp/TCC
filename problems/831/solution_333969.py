def lingua_p(palavra):
    vogais=('aeiouAEIOU')
    palavra_p=''
    for l in palavra:
        palavra+=1
        if l in vogais:
            palavra_p+='p'
            palavra_p+= 1
    return (palavra_p)