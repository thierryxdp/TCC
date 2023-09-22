def retira_pontuaçao(frase):
    texto = str(frase)
    x = "-,:;!?."
    y = "       "
    table = texto.maketrans(x,y);
    	print (texto.translate(table))