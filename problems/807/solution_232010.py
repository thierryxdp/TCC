def remove_pontuacao(frase):
"""funcao que indicada uma frase retorna a frase sem pontuação;
str->str"""
f1=str.replace(frase,','," ")
f2=str.replace(f1,'-'," ")
f3=str.replace(f2,':'," ")
f4=str.replace(f3,';'," ")
f5=str.replace(f4,'.'," ")
f6=str.replace(f5,'?'," ")
f7=str.replace(f6,'!'," ")
return f7