retira_pontuacao (frase):
"tira pontuação e substitui por espaço"
frase=frase.replace('-',' ')
frase=frase.replace(',',' ')
frase=frase.replace(':',' ')
frase=frase.replace(';',' ')
frase=frase.replace('.',' ')
frase=frase.replace('!',' ')
frase=frase.replace('?',' ')
return frase