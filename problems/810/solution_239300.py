def inverte(f):
    "str-->str"
    "A função pega uma string, converte todas as letras maiusculas, tira todos os pontos e retorna ela invertida"
    #Primeiro são feitas as tarefas de converter letras maiusculas pra minusculas, depois tirados os pontos, então a string é separada em termos de uma lista, essa lista então é invertida e por fim unida pelo " " para formar a frase inversa
    f1= str.replace((str.lower(f)),"-"," ")
    f2= str.replace(f1,","," ")
    f3= str.replace(f2,":"," ")
    f4= str.replace(f3,";"," ")
    f5= str.replace(f4,"?"," ")
    f6= str.replace(f5,"!"," ")
    f7= str.replace(f6,"."," ")
    L1= str.split(f7)
    s=str.join(" ",L1[::-1])
    return s