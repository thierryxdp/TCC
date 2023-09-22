def lingua_p(palavra):
    '''função que recebe uma palavra em português e traduz para a lingua do p.
    str -> str
    Explicação: a lingua do p consiste em adicionar o p sempre que houver uma vogal e duplicá-la, dessa forma usamos o for para verificar se a letra está na palvra e o if para veridficar se é vogal ou não, depois acrescentamos o p se for vogal e montamos a nova estrutura, colocando tudo em minúsculo depois.''' 
    letras=''
    for letra in palavra:
        if letra in 'AEIOUaeiouáéóúí':
            letra=letra+'p'+letra
        letras=letras+letra
    return str.lower(letras)