def acima_da_media(notas):
   """retoma os alunos acima da media"""
media= sum(notas)/len(notas)
return (notas>media)