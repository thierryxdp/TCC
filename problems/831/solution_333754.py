def lingua_p(stri):
    vogais=('aeiou')
    LC_stri=stri.lower()
    
    stri_mod=''
    for l in LC_stri:
        stri_mod += l
        if l in vogais:
            stri_mod += 'p'
            stri_mod += l 
    return(stri_mod)