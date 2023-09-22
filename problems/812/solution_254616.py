def retira_pontuacao(frase):
  frase=str.replace(frase,"!"," ").replace(frase,","," ").replace(frase,":"," ").replace(frase,";"," ").replace(frase,"."," ").replace(frase,"?"," ").replace(frase,"!"," ")
	return frase