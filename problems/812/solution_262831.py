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

   #casos de teste
   #retira_pontuacao("Sacrificar-se pelos outros é o maior presente que você poderia dar a eles.") == 'Sacrificar se pelos outros é o maior presente que você poderia dar a eles '
   #retira_pontuacao("Eu vivo para terminar uma conspiração que irá corromper nossas vidas. Para proteger aqueles que precisam. Eu governo de acordo com minha ética, minha moral e minhas convicções.") == 'Eu vivo para terminar uma conspiração que irá corromper nossas vidas  Para proteger aqueles que precisam  Eu governo de acordo com minha ética  minha moral e minhas convicções '
   #retira_pontuacao("Enquanto outros homens seguem cegamente a verdade, lembre-se, nada é verdade.") == 'Enquanto outros homens seguem cegamente a verdade  lembre se  nada é verdade '