def inverte(frase):
    """
    
    
    
    """
    retira = str.strip(frase, "-")
  
    retira1=str.replace(retira,   "!"," ")
    retira2=str.replace(retira1,  "?"," ")
    retira3=str.replace(retira2,  "."," ")
    retira4=str.replace(retira3,  "/"," ")
    retira5=str.replace(retira4,  ":"," ")
    retira6=str.replace(retira5,  ";"," ")
    retira7=str.replace(retira6,  "-"," ")
    retira8=str.replace(retira7,  ","," ")
    
    return str.join(" ",str.split(retira8))