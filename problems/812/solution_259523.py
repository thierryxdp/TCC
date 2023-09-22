def retira_pontuacao(frase):
	final = frase.replace('.', ' ')
    final1 = final.replace(',', ' ')
    final2 = final1.replace('?', ' ')
    final3 = final2.replace('-', ' ')
    final4 = final3.replace('!', ' ')
    final5 = final4.replace(':', ' ')
    return final5