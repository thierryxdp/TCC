def lingua_p(stri):
#Dada uma palavra, a funcao retorna esta palavra traduzida para a lingua do P str -> str
    vogais = ('aeiou')
    l_stri = stri.lower()
    st = ''
    for n in l_stri:
        st += n
        if n in vogais:
            st += 'p'
            st += n
    return (st)