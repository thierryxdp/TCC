def inverte(texto):
     texto = str.replace(texto,"."," ")
     texto = str.replace(texto,";"," ")
     texto = str.replace(texto,"-"," ")
     texto = str.replace(texto,","," ")
     texto = str.replace(texto,"!"," ")
     texto = str.replace(texto,"?"," ")
     texto = str.replace(texto,"-"," ")
     texto = str.lower(texto)
     return texto