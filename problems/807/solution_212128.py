def conta_frases(texto):
     """Recebe um texto e retorna a quantidade de frases baseado nos pontos/string->int"""
     if(any(char.isdigit() for char in texto))==True:
          print("Palavra não contém números")
     else:
          w=0
          z=0
          p=0
          q=0
          for i in range(len(texto)):
               if texto[0]=="." or texto[0]=="?"or texto[0]=="!":
                    print("Textos não podem começar por ponto")
               elif(texto[i]=="."):
                           if i+2<len(texto):  
                                 if(texto[i+1]=="." and texto[i+2]=="."):
                                       w+=1
                                 else:
                                       z+=1
                           else texto=texto +"   ":
                                 z+=1
               elif texto[i]=="!":
                          if(i+1<len(texto)) :
                                if(texto[i+1]!="." or texto[i+1]!="!" or texto[i+1]!="?"):
                                      p+=1
                          else texto=texto +"   ":
                                 z+=1            
               elif texto[i]=="?":
                          if(i+1<len(texto)) :
                                if(texto[i+1]!="." or texto[i+1]!="!" or texto[i+1]!="?"):
                                      q+=1
                          else texto=texto +"   ":
                                 z+=1            
          return w+z+p+q