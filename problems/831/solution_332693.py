"""recebe uma frase em língua portuguesa e retorna essa mesma
palavra na língua do P.
Assinatura: string --> string
testes:
lingua_p('coração') == 'coporapaçãopo'
lingua_p('manuella') =='mapanupuepellapa'
"""

def lingua_p(palavra):
    string_saida=''
    for letra in palavra:
        if letra in 'AEIOUaeiouáéíóú':
        	string_saida+=letra+'p'+letra
        else:
            string_saida+=letra
    return string_saida