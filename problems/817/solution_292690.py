def acimaDaMedia(notas):
’’’ retorne a m ́edia da turma e e uma lista com as notas que ficaram acima da m ́edia.
list -> tup’’’
media=sum(notas)/len(notas)
return media, maiores(notas,media)