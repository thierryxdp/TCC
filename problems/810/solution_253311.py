#Função utilizada no exercicio anterior
def retira_pontuacao(fraseInicial):
    travessao = str.replace(fraseInicial,'-',' ')
    virgula = str.replace(travessao,',',' ')
    doisPontos = str.replace(virgula,':',' ')
    pontoVirgula = str.replace(doisPontos,';',' ')
    pontoFinal = str.replace(pontoVirgula,'.',' ')
    pontoInterrogacao = str.replace(pontoFinal,'?',' ')
    pontoExclacamacao = str.replace(pontoInterrogacao,'!',' ')

    return pontoExclacamacao
#Função que dada uma frase como entrada, retorna uma outra frase que contem as mesmas palavras da frase de entrada,porém na ordem inversa,sem letras maiúsculas e sem a pontuação,str = str
def inverte(FraseFinal):
    listaA = str.lower(retira_pontuacao(FraseFinal))
    listaB = str.split(listaA)
    listaC= listaB[::-1]
    listaD = str.join(" ",(listaC))
   
    return listaD