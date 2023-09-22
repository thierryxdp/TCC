#
def lingua_p(palavra):
      contador=0
      palavraP=''
      palavra=list(palavra.lower())
      vogais=['a','e','i','o','u']
      for i in range(len(palavra)):
            if palavra[i] in vogais:
                  contador+=1
      for i in range(len(palavra)+contador):
            if palavra[i] in vogais:
                  list.insert(palavra,i+1,'p'+palavra[i])
            palavraP+=palavra[i]
      return palavraP