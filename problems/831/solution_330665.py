#Exercício 6
def lingua_p(palavra):
   '''Retorna uma palavra traduzida para lingua p
      str -> str'''
   #Transformando palavra em uma lista de caracteres para poder mudar
   listaPalavra = list(palavra)
   retorno = ''
   #Criando que vai percorrer os indices da palavra
   for pos in range(len(palavra)):
      #Identificando a letra que está nessa posição
      letra = listaPalavra[pos]

      #Caso essa letra seja vogal...
      if letra in 'AEIOUaeiouÁÉÍÓÚáéíóú':
         #Adicione p + letra após a vogal
         retorno = retorno + listaPalavra[pos] + 'p'+letra
      else:
         #Acicione apenas a consoante sozinha
         retorno = retorno + listaPalavra[pos]
   
   return retorno