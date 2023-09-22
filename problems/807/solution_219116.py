def conta_frases(texto):
    'dado um texto, retorna o numero de frases que tem nesse texto'
    frases_com_ret=str.count(texto,'...')
    frases_com_excla=str.count(texto,'!')
    frases_com_inter=str.count(texto,'?')
    frases_com_ponto=str.count(texto,'.') - str.count(texto,'...')*3
    numero_de_frases=frases_com_...+frases_com_!+frases_com_?+frases_com_.
    return numero_de_frases