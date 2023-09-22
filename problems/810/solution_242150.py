def retira_pontuacao(frase):
    """A função retira as pontuações da frase e substitui
	por espaço;
    str -> str"""
    sponto = str.replace(frase, ",","")
    svirgula = str.replace(sponto, ".","")
    stravessao = str.split(svirgula, ":","")
    sdoisponto = str.replace(stravessao, "-","")
    spontovirgula = str.replace(sdoisponto, ";","")
    sinterrogacao = str.replace(spontovirgula, "?","")
    sexclamacao = str.replace(sinterrogacao, "!", "")
    frasefinal = sexclamacao
    return frasefinal

def inverte(frase):
    """"A Função inverte uma frase sem a pontuação e 
	sem letras maiúsculas; 
	str -> str"""
    normal = str.split(retira_pontuacao(frase),' ')
    invertida = normal[::-1]
    invtxt = str.join(' ', invertida)
    return str.strip((invtxt.lower()))