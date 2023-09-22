def retira_pontuacao(string:str)->str:
    travessao = str.join(" ", str.split(string,"-"))
    virgula = str.join(" ", str.split(travessao,","))
    dois_pontos = str.join(" ", str.split(virgula,":"))
    ponto_e_virgula = str.join(" ", str.split(dois_pontos,";"))
    ponto_final = str.join(" ", str.split(ponto_e_virgula,"."))
    exclamacao = str.join(" ", str.split(ponto_final,"!"))
    interrogacao=str.join(" ", str.split(exclamacao,"?"))

    final = interrogacao

    return final

def inverte(frase):

    """A Função inverte a frase dada sem letras maiúsculas e pontuações.
       str->str
       Parametro:
       frase: frase dada
    """

    sem_pontuacao = retira_pontuacao(frase)
    letras_minusculas = str.lower(sem_pontuacao)
    separa_palavras = str.split(letras_minusculas)
    inverter_ordem = separa_palavras[::-1]
    juncao_palavras = str.join(" ",inverter_ordem)
    final = juncao_palavras

    return final