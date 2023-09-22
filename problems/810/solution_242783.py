def retira_pontuacao(frase):
    """ Dado como entrada uma frase, retorna essa frase
    sem as pontuações, str -> str 
    Vai trocando pontuação por caracter especial e no final muda,
    todos para espaço"""
   
    ponto = str.replace(frase,".","¬")
    ponto_virgula = str.replace(ponto,";","¬")
    ponto_dois = str.replace(ponto_virgula,":","¬")
    virgula = str.replace(ponto_dois,",","¬")
    travessao = str.replace(virgula,"-","¬")
    exclamacao = str.replace(travessao,"!","¬")
    interrogacao = str.replace(exclamacao,"?","¬")
    espaco = str.replace(interrogacao,'¬',' ')
    return espaco

def inverte(frase):
    """ Inverte a frase, remova a pontuação e deixa tudo 
    minúscula  str -> str"""
    " retira a pontuação "
    sem = retira_pontuacao(frase)
    " deixa minúscula "
    minuscula = str.lower(sem)
    " retira o espaço final"
    espaco_final = str.rstrip(minuscula)
    " Transforma em lista "
    quebra = str.split(espaco_final)
    " Inverte a lista "
    inverte = quebra[::-1]
    " Junta a lista com "¬" "
    transforma = str.join("¬",inverte)
    " Transforma o "¬" em espaço "
    espaco2 = str.replace(transforma,"¬",' ')
    " Retorna a frase desejada "
    return espaco2