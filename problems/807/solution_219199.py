def conta_frases(texto):
    
    frases_com_excla=str.count(texto,'!')
    frases_com_inter=str.count(texto,'?')
    frases_com_rt=str.count(texto,'...')
    frases_com_pf=str.count(texto,'.') - 3*str.count(texto,'...')
    
    return frases_com_excla + frases_com_inter + frases_com_rt + frases_com_pf