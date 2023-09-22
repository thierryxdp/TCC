def lingua_p(palavra):
    palavra=palavra.lower()
    final=''
    for i in palavra:
        if i in 'aeiou':
            final=final+i+palavra.join('p')+i
        else:
            final=final+i
    return final