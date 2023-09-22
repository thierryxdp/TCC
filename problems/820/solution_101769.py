def posLetra(frase, letra, numero):
      if frase.count(letra) < numero:
        return -1
      else:
            lista1 = []
            txt = list(frase)
            i = 0
            while len(lista1) < numero and i < len(txt):
            if letra == txt[i]:
                  list.append(lista1, txt[i])
                  i+= 1
            return i - 1