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

""""foi"""

def inverte(txt):
   """essa função serve para retirar as pontuações palavras em um texto, inverter e deixar em letra minuscula
   str->str"""
   lista = []
   txt = retira_pontuacao(txt)
   txt = txt.lower()
   lista = lista + str.split(txt)
   lista.reverse()
   x = " ".join(lista)
   return x
    
   #casos de teste
   #inverte("Enquanto outros homens seguem cegamente a verdade, lembre-se, nada é verdade.") == 'verdade é nada se lembre verdade a cegamente seguem homens outros enquanto'
   #inverte("Sacrificar-se pelos outros é o maior presente que você poderia dar a eles.") == 'eles a dar poderia você que presente maior o é outros pelos se sacrificar'
   #inverte("Na morte, somos iguais.") == 'iguais somos morte na'