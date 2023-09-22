def remove_pontuacao(frase):
"""funcao que indicada uma frase retorna a frase sem pontuação;
str->str"""
fa=str.replace(frase,',',",")
fb=str.replace(fa,'-'," ")
fc=str.replace(fb,':'," ")
fd=str.replace(fc,';'," ")
fe=str.replace(fd,'.'," ")
fr=str.replace(fe,'?'," ")
fg=str.replace(fr,'!'," ")
return fg