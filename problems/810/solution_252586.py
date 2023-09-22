def inverte(frase):
    """"dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase
de entrada na ordem inversa, sem letras maiusculas, e sem a pontuacao."""
    nova_frase = str.lower(retira_pdada uma frase retorne uma outra frase que contenhaonto(frase))
    lista = str.split(nova_frase, ' ')
    list.reverse(lista)
    final = str.join(' ', lista)
   
    return final