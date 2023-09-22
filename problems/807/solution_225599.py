def conta_frases(txt):
   """essa função serve para contar o número de frases em um texto
   str->int"""
   txt = txt.replace("...",".")
   txt = txt.replace("!",".")
   txt = txt.replace("?",".")
   num_pontos = txt.count(".")
   return num_pontos   

   #casos de teste
   #conta_frases("Oi, aqui é o Goku!") == 1
   #conta_frases("Dediquei minha vida a estudar a sabedoria, e também a loucura e a insensatez. Eu sabia que é tão inútil como escrever sobre a água. Ora, onde há sabedoria, também há tristeza. E o que aumenta o conhecimento aumenta a dor.") == 4
   #conta_frases("Na morte, somos iguais.") == 1