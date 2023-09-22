def inverte(frase):
      """Recebe uma frase e a retorna com as palavras invertidas/str->str"""
      frase=frase.lower()
      if any(char.isdigit() for char in frase)==True:
            print("Frases não podem conter números")
      elif frase[-1]!="." and frase[-1]!="!" and frase[-1]!="?":
            print("Frases devem terminar com ponto")
      else:
            for i in range(len(frase)):
                  if frase[0]=="." or frase[0]=="?" or frase[0]=="!" or frase[0]=="-" or frase[0]=="," or frase[0]==";" or frase[0]==":":
                        print("Frases não podem começar com sinais de ponutação")
                  elif frase[i]==".":
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
            return str(lista1)