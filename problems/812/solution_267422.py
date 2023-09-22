def retira_pontuacao(frase):
    'Retorna a frase sem qualquer sinal de pontuacao..string--string'
    sinais=(',','.',';',':','"','!','?')
    frase.replace(sinais)
    return frase