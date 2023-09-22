def inverte(frase):
      """Recebe uma frase e a retorna com as palavras invertidas/str->str"""
      frase=frase.lower()
      if True:
            for i in range(len(frase)):
                  if frase[i]==".":
                        frase=frase.replace("."," ")
                  elif frase[i]=="?":
                        frase=frase.replace("?"," ")
                  elif frase[i]=="!":
                        frase=frase.replace("!"," ")
                  elif frase[i]==",":
                        frase=frase.replace(","," ")
                  elif frase[i]=="-":
                        frase=frase.replace("-"," ")
                  elif frase[i]==":":
                        frase=frase.replace(":"," ")
                  elif frase[i]==";":
                        frase=frase.replace(";"," ")
            lista=[]
            x=str("")
            for i in range(len(frase)):
                  if frase[i]!=" ":
                        x+=frase[i]
                  else:
                        lista.append(x)
                        x=str("")
            lista1=[]
            for i in reversed(range(len(lista))):
                  for j in range(len(lista)):
                       lista1.append(lista[i])
                       i-=1
                  break
            return " ".join(lista1)