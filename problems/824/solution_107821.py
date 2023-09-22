def uppCons(frase):
      """Recebe uma frase e retorna a frase com as consoantes maiúsculas"""
      lista=list()
      for i in range(len(frase)):
            lista.append(frase[i])
      for i in range(len(lista)):
            if lista[i]!="a" and lista[i]!="A" and lista[i]!="e" and lista[i]!="E" and lista[i]!="i" and lista[i]!="I" and lista[i]!="o" and lista[i]!="O" and lista[i]!="u" and lista[i]!="U":
                  lista[i]=lista[i].upper()     
      return "".join(lista)