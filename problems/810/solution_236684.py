def retira_pontuacao(frase):
    """função que retorna a frase dada sem nenhum sinal de pontuação, que são substituídos por espaço
    str -> str"""
    semtravessao = str.join(' ',str.split(frase,'-'))
    semvirgula = str.join('',str.split(semtravessao,','))
    semdoispontos = str.join('',str.split(semvirgula,':'))
    sempontoevirgula = str.join('',str.split(semdoispontos,';'))
    semponto = str.join('',str.split(sempontoevirgula,'.'))
    seminterrogacao = str.join('',str.split(semponto,'?'))
    semexclamacao = str.join('',str.split(seminterrogacao,'!'))
    novafrase = str.join(' ',str.split(semexclamacao,' '))
    return novafrase
def inverte(frase):
    """função que retorna a frase dada invertida, sem pontuação e sem letras maiúsculas
    str -> str"""
    nopont = retira_pontuacao(frase)
    minusculas = str.lower(nopont)
    lista = str.split(minusculas)
    listainvertida = lista[::-1]
    return str.join(' ',listainvertida)