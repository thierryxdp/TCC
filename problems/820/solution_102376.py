def posLetra (frase: str, letra:str, o: int)-> int:
   '''Retorna a posição na frase da ocorrência o da letra dada'''
   #Deixando toda a frase em minusculo
   fraseA = str.lower(frase)
   
   #Inicializando contador e acumulador
   i = 0
   contador_ocorrencia = 0
   posicao = 0
   
   #Criando while para percorrer frase
   while i < len(fraseA) and contador_ocorrencia < o:
      if fraseA[i] == letra:
         contador_ocorrencia += 1
         posicao = i
      i += 1

   return posicao