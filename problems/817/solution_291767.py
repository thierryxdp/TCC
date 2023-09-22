def acima_da_media(l):
  media = round(float(sum(l))/len(l), 1) 
  notasAcimaMedia = questao7(l, media) 
  return media, notasAcimaMedia
    
print "Questao 9
l = [10, 9.5, 8.7, 2, 3.5, 0, 4.9, 6.7, 5.3, 9.4, 8.9]
print "Notas = ", l
x = questao9(l)
print "Media de notas:", x[0]
print "Notas acima da media: ", x[1]
print "\n"