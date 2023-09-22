def posLetra(texto,letra,n):
    nt=str.join("*",texto)
    lt=str.split(nt,"*")
    return list.count(lt,letra)