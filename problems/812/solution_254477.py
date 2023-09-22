def retira_pontuacao(frase):
      """Recebe uma frase e a retorna sem os sinas de pontuação/str->str"""
      if any(char.isdigit() for char in frase)==True:
            print("Frases não podem conter números")
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
            return frase