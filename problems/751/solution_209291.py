def quant_palavras(frase):
    
   if frase[0] == " ":
      frase = frase.lstrip(" ")
   if frase[-1] == " ":
      frase = frase.rstrip(" ")
   num_esp = frase.count(" ") + 1 
   return num_esp