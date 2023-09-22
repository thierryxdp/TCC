uppCons(string):

  txt = list(string)

  i = 0

  while i < len(txt):

    if txt[i] in "xgixgigixgixfizrufahslsisihxhochocigcgicgixgixigxgixigx":

         txt[i] = txt[i].upper()          

   

  txt = "".join(txt)

  return txt