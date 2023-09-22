def retira_pontuacao(txt):
   """essa função serve para retirar as pontuações palavras em um texto
   str->str"""
   txt = txt.replace("..."," ")
   txt = txt.replace("."," ")
   txt = txt.replace(";"," ")
   txt = txt.replace("!"," ")
   txt = txt.replace("?"," ")
   txt = txt.replace(":"," ")
   txt = txt.replace("-"," ")
   txt = txt.replace(")"," ")
   txt = txt.replace("("," ")
   txt = txt.replace("["," ")
   txt = txt.replace("]"," ")
   txt = txt.replace(","," ")
   return txt