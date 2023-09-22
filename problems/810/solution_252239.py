def remover(fraseremove):
    removido = str.replace(fraseremove,"!",'')
    removido1 = str.replace(removido,",",'')
    removido2 = str.replace(removido1,".",'')
    removido3 = str.replace(removido2,"-",' ')
    removido4 = str.replace(removido3,":",'')
    removido5 = str.replace(removido4,";",'')
    removido6 = str.replace(removido5,"...",'')
    removido7 = str.replace(removido6,"''",'')
    return remover
 
def inverte(frase):
    lista = str.split(str.lower(frase))
    frase = remover(lista)
    list.reverse(lista)
    final = str.join(' ', lista)
    return final