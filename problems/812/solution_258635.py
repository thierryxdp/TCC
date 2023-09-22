def retira_pontuacao(frase):
  argumentos=('-',',',':',';','.','?','!')
  texto=str.join(' ',str.split(frase, '!'))
  return texto