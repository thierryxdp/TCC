def retira_pontuacao(frase):
  frase1 = frase.replace("...", "  ")
  frase2 = frase1.replace("!"," ")
  frase3 = frase2.replace("?"," ")
  frase4 = frase3.replace(";"," ")
  frase5 = frase4.replace("."," ")
  frase6 = frase4.replace("-"," ")
  frase7 = frase6.replace(":"," ")
  frase8 = frase7.replace(","," ")
  return frase8