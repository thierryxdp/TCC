def acima_da_media(l):
  media = round(float(sum(l))/len(l), 1) 
  notasAcimaMedia = questao7(l, media)
  return media, notasAcimaMedia