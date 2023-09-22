def retira_pontuacao (frase):
   '''funcao que retorna frase sem pontuacao'''
   '''str=>str'''
frase=frase.replace("."," ")
frase=frase.replace("/"," ")
frase=frase.replace(";"," ")
frase=frase.replace(","," ")
frase=frase.replace(":"," ")
frase=frase.replace("-"," ")
frase=frase.replace("?"," ")
frase=frase.replace("!"," ")
 return frase