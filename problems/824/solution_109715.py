def uppCons(frase):
    """Recebe uma frase e retorna a frase com todas as suas consoantes em
       maiúsculas(os demais caracteres permanecem como estavam na frase original).
       str->str
       
       Parameters:
       frase: A frase que sera usada como base para a função."""
    i=0
    frase2=[]
    while i<len(frase):
        if str.lower(frase[i]) in "qwrtypsdfghjklçzxcvbnm":
            list.append(frase2,str.upper(frase[i]))
        else:
            list.append(frase2,frase[i])
        i=i+1
    return str.join("",frase2)