def conta_frases(texto):
    'dado um texto, retorna o numero de frases que tem nesse texto'
    frases_com_...=str.count(texto,'...')
    frases_com_!=str.count(texto,'!')
    frases_com_?=str.count(texto,'?')
    frases_com_.=str.count(texto,'.') - str.count(texto,'...')*3
    numero_de_frases=frases_com_...+frases_com_!+frases_com_?+frases_com_.
    return numero_de_frases