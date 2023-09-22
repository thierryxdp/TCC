def retira_pontuacao(frase)
'''Dada uma frase, a função  retorna a frase sem ponto
str -> str'''
palavra = str.replace(frase,'?','')
palavra = str.replace(palavra'.',' ')
palavra= str.replace(palavra,',',' ')
palavra= str.replace(palavra,'!',' ')
palavra= str.replace(palavra,'-',' ')
return palavra