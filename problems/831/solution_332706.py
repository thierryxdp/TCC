"""recebe uma frase em língua portuguesa e retorna essa mesma
palavra na língua do P.
Assinatura: string --> string
testes:
lingua_p('coração') == 'coporapaçãopo'
lingua_p('manuella') =='mapanupuepellapa'
"""

def lingua_p(palavra):
    trad_final=''
    for letra in palavra:
        if letra in 'AEIOUaeiouáéíóú':
        	trad_final+=letra+'p'+letra
        else:
            trad_final+=letra
    return trad_final