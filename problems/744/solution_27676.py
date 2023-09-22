def hashtag(string):
      """Recebe uam string e insere # no início, meio e final da string/str->list"""
      lista=list()
      for i in range(len(string)):
            lista.append(string[i])
      if len(lista)%2==0:
            lista.insert(0,"#")
            lista.insert(len(lista)//2 +1,"#")
            lista.append("#")
      else:
            lista.insert(0,"#")
            lista.insert(len(lista)//2,"#")
            lista.append("#")  
      return "".join(lista)