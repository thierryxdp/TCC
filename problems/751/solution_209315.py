def conta_frases(frase):
   """essa função serve para contar o número de palavras em um texto
   str->int"""
   if frase[0] == " ":
      frase = frase.lstrip(" ")
   if frase[-1] == " ":
      frase = frase.rstrip(" ")
   num_esp = frase.count(" ") + 1 
   return num_esp

   #casos de teste
   #conta_palavras("Oi, aqui é o Goku!") == 5
   #conta_palavras("Há uma diferença entre o que dizemos que é verdade, e o que vemos que é verdade.") == 17
   #conta_palavras("Seria o único propósito da folha, o de cair?") == 9