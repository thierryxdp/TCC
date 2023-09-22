def conta_frases(frases):
    frases=str.split(frases,'.')
    num_ponto=len(frases)-1
    frases=frases.split('!')
    num_excl=len(frases.split('!'))-1
    frases=frases.split('?')
    num_int=len((frases.split('?'))-1
    frases=frases.split('..')            
    num_doisp=len(frases.split('..'))-1
    return num_ponto+num_excl+num_int+num_doip