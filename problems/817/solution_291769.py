def acima_da_media(l):
  media = round(float(sum(l))/len(l), 1) 
  notasAcimaMedia = acima_da_media(l, media) 
  return media, notasAcimaMedia