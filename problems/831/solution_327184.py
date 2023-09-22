def lingua_p(palavra: str) -> str:
    """Recebe uma palavra em português e retorna essa mesma palavra traduzida
       para a língua do P

       Parameters:
       palavra: Palavra, na forma de string, escrita em português a ser
       traduzida para a língua do P

       Return:
       Dado o parâmetro "palavra", retorna a mesma string do parâmetro "palavra"
       traduzida para a língua do P, no qual, após cada vogal da string do
       parâmetro "palavra", é inserida a sequência de letras "p" mais a vogal
       original, e, a língua P ignora todas as letras maiúsculas

       Examples:
       lingua_p("exemplo") == 'epexepemplopo'
       lingua_p("entao") == 'epentapaopo'
       lingua_p("caderno") == 'capadepernopo'
    """
    
    nova = str.lower(palavra)
    resposta = ""

    for x in nova:
        if x in "aeiouáéíóúâêîôûãõ":
            resposta = resposta + (x + "p" + x)
        else:
            resposta = resposta + x

    return resposta