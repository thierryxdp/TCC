def conta_frases(texto):
      """Recebe um texto e retorna o número de frases/string->int"""
      if any(char.isdigit() for char in texto)==True:
            print("Palavras não contém números")
      else:
            texto=texto+"  "
            j=0
            k=0
            m=0
            ret=0
            for i in range(len(texto)):
                  if texto[0]=="." or  texto[0]=="!" or  texto[0]=="?":
                        print("Textos não começam por ponto")
                  elif texto[i]==".":
                        j+=1
                        if i+2<len(texto):
                              if texto[i+1]==".":
                                    j-=1
                                    if texto[i+2]==".":
                                          ret+=1
                                    elif texto[i+1]=="!" or texto[i+1]=="?":
                                          print("Não pode haver dois pontos seguidos salvo reticências")
                  elif texto[i]=="!" :
                        k+=1
                        if i+1<len(texto):
                              if texto[i+1]=="!" or texto[i+1]=="?" or texto[i+1]==".":
                                    print("Não pode haver dois pontos seguidos salvo reticências")
                  elif texto[i]=="?":
                        m+=1
                        if i+1<len(texto):
                              if texto[i+1]=="!" or texto[i+1]=="?" or texto[i+1]==".":
                                    print("Não pode haver dois pontos seguidos salvo reticências")
            return j+k+m