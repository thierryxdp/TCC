def posLetra(frase, letra, numero):
      if frase.count(letra) < numero:
        return -1
      else:
            lista1 = []
            txt = list(frase)
            i = 0
            while i < len(txt) and len(lista1) < numero:
            	if letra == txt[i]:
                    list.append(lista1, txt[i])
                    i+= 1
            return i - 1