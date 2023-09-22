Para contar a quantidade de palavras usei dua propriedades de str
Propriedade 1 O strip()método remove quaisquer caracteres iniciais (espaços no início) e finais (espaços no final) (espaço é o caractere inicial padrão a ser removido)
Propriedade 2 string count() retorna o número de ocorrências de uma substring na string fornecida. 
def quant_palavras(frase):
    """"""
    return str.count((frase), ' ') + 1