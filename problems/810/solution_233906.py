def inverte(frase):
    """Essa função inverte a frase dada, sem apresentar letras 
    maiúsculas, e sem pontuação. Como entrada uma frase e como saída
    a frase invertida;
    str-> str"""
    nova_frase=frase.lower()
    frase1=str.replace(nova_frase,","," ")
    frase2=str.replace(frase1,"."," ")
    frase3=str.replace(frase2,"-"," ")
    frase4=str.replace(frase3,":"," ")
    frase5=str.replace(frase4,";"," ")
    frase6=str.replace(frase5,"!"," ")
    frase7=str.replace(frase6,"?"," ")
    print(frase7)
    frase8=str.split(frase7)
    print(frase8)
    lista= frase8[::-1]
    print(lista)
    return str.join(" ",lista)