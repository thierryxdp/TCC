def retira_pontuacao(frase):
    '''Funcao que, dada uma frase, retorna a mesma frase 
    com todos os seus caracteres de pontuacao substituidos 
    por espaço, ou seja, retira todos os caracteres de 
    pontuacao. Os caracteres levados em consideracao são:
    travessao, virgula, dois pontos, ponto e virgula, 
    ponto final, reticencias, ponto de interrogacao e 
    ponto de exclamacao.
    str -> str'''
    frase = str.replace(frase,'...', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    return frase

#casos de teste
# s = 'Nas sombrias e sujas minas de sal de Endovier, um jovem
#de 18 anos está cumprindo sua sentença. Celaena é uma assassina, e a
#melhor de Adarlan. Aprisionada e fraca, ela está quase perdendo as
#esperanças quando recebe uma proposta. Terá de volta sua liberdade se
#representar o príncipe de Adarlan em uma competição, lutando contra os
#mais habilidosos assassinos e larápios do reino. Endovier é uma
#sentença de morte, e cada duelo em Adarlan será para viver ou morrer.
#Mas se o preço é ser livre, ela está disposta a tudo.'

# retira_pontuacao(s) == 'Nas sombrias e sujas minas de sal de Endovier
# um jovem de 18 anos está cumprindo sua sentença  Celaena é uma
# assassina  e a melhor de Adarlan  Aprisionada e fraca  ela está quase
# perdendo as esperanças quando recebe uma proposta  Terá de volta sua
# liberdade se representar o príncipe de Adarlan em uma competição
# lutando contra os mais habilidosos assassinos e larápios do reino
# Endovier é uma sentença de morte  e cada duelo em Adarlan será para
# viver ou morrer  Mas se o preço é ser livre  ela está disposta a tudo'