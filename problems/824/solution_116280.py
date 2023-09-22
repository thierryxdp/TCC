def uppCons (frase: str) -> str:
   '''Retorna a frase com todas as suas consoantes em maiusculo'''
   cons = "BDCFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvxywz"
   #Inicializando contador e acumulador
   i = 0
   frase_retorno = frase[:]
   #Criando while para percorrer lista
   while i < len(frase):
      if frase[i] is in cons:
         frase_retorno = frase_retorno[:i] + str.upper(frase[i]) + frase_retorno[i+1:]
      i += 1

   return frase_retorno