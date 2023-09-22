def posLetra(texto, letra, numero):
    if(texto.count(letra) < numero):
        return -1
    helper = 0
    
    for i, l in enumerate(texto):
      if(letra == l):
        helper = helper + 1
        if (helper == numero):
          return i        print(letra, i)