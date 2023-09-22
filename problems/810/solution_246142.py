def inverte(txt):
   """essa função serve para retirar as pontuações palavras em um texto, inverter e deixar em letra minuscula
   str->str"""
   lista = []
   txt = frases_sem_pontuacao(txt)
   txt = txt.lower()
   lista = lista + str.split(txt)
   lista.reverse()
   x = " ".join(lista)
   return x
    
   #casos de teste
   #inverte("Enquanto outros homens seguem cegamente a verdade, lembre-se, nada é verdade.") == 'verdade é nada se lembre verdade a cegamente seguem homens outros enquanto'
   #inverte("Sacrificar-se pelos outros é o maior presente que você poderia dar a eles.") == 'eles a dar poderia você que presente maior o é outros pelos se sacrificar'
   #inverte("Na morte, somos iguais.") == 'iguais somos morte na'