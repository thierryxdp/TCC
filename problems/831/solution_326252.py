def lingua_p(palavra):
      """Recebe uma palavra e traduz para a língua do p/str->str"""
      if any(char.isdigit() for char in palavra)==True:
            print("A palavra deve conter apenas letras")
      else:
            palavra.lower()
            lista=list()
            for i in range(len(palavra)):
                  lista.append(palavra[i])
            i=0
            while i!=len(lista):
                  if lista[i]=="a" or lista[i]=="á" or lista[i]=="ã" or lista[i]=="â" or lista[i]=="e" or lista[i]=="é" or lista[i]=="ê" or lista[i]=="i" or lista[i]=="í" or lista[i]=="î"or lista[i]=="o" or lista[i]=="ó" or lista[i]=="ô" or lista[i]=="õ" or lista[i]=="u" or lista[i]=="ú" or lista[i]=="û":
                        lista.insert(i+1,"p")
                        lista.insert(i+2,lista[i])
                        i=i+3
                  else:
                        i+=1
            return "".join(lista)