def uppCons(frase):
      """Recebe uma frase e retorna a frase com as consoantes maiúsculas"""
      lista=list()
      for i in range(len(frase)):
            lista.append(frase[i])
      for i in range(len(lista)):
            if lista[i]!="a" and lista[i]!="A" and lista[i]!="e" and lista[i]!="E" and lista[i]!="i" and lista[i]!="I" and lista[i]!="o" and lista[i]!="O" and lista[i]!="u" and lista[i]!="U" and lista[i]=="ã" and lista[i]=="Ã" and lista[i]=="â" and lista[i]=="Â" and lista[i]=="á" and lista[i]=="Á" and lista[i]=="é" and lista[i]=="É" and lista[i]=="ê" and lista[i]=="Ê"and lista[i]=="í" and lista[i]=="Í" and lista[i]=="î"and lista[i]=="Î" and lista[i]=="õ" and lista[i]=="õ"and lista[i]=="Õ"and lista[i]=="ô"and lista[i]=="Ô"and lista[i]=="ó" and lista[i]=="Ó" and lista[i]=="ú" and lista[i]=="Ú" and lista[i]=="û" and lista[i]=="Û":
                  lista[i]=lista[i].upper()
      return "".join(lista)