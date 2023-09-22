def freq_palavras(frases):
     freq = dict()
     frases_sep = frases.split("")
     for i in frases:
             if i not in freq:
                     freq[i] = 1
             else:
                     freq[i] += 1
     return freq