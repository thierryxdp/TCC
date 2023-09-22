def retira_pontuacao(frase):
    'retira caracteres especiais de uma string e a retorna os substituindo por espaço"
    lista = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","'","\""]
    return frase.translate({ord(p): " " for p in lista})