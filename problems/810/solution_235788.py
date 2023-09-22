def inverte(frase):
    """função que dada uma frase retorna a mesma frase na ordem inversa sem pontuação e letras maiúsculas;
    str->str"""
    var1=str.replace(frase,'...','')
    var2=str.replace(var1,'?','')
    var3=str.replace(var2,'.','')
    var4=str.replace(var3,'!','')
    var5=str.replace(var4,',','')
    var6=str.replace(var5,'-',' ')
    var7=str.replace(var6,';','')
    var8=str.replace(var7,':','')
    var9=str.split(var8," ")
    var10=var9[::-1]
    var11=str.join(" ",(var10))
    return str.lower(var11)