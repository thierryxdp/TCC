def uppCons(frase):
   #Essa função irá receber uma frase como entrada e retorna-la com todas as suas consoantes em maíusculo
	#Entrada: String - Frase | Saída: String - Frase

	fraseConsoante =''
    for letra in frase:
        if not letra in 'aeiouAEIOU' and letra.isalpha() or letra =='ç':
            fraseConsoante += letra.upper()
        else:
            fraseConsoante += letra
    return fraseConsoante