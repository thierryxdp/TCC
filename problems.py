def getProblems():
    data_array = []
    
    # 02 - Funcoes e Tipos de dados
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    
    # 03 - Tipos de dados, Strings, Estrutura Condicional
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    
    # 04 - Variáveis e atribuição, strings e tuplas
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    
    # 05 - Manipulação de strings, tuplas e listas
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    
    # 06 - Fatiamento e manipulação de listas
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    
    # 07 - Estrutura de repetição com teste de parada: While
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    
    # 08 - Estrutura de repetição iteradora: for
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    
    # 09 - Laços aninhados e matrizes
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    data_array.append(["method", "context", "theme"])
    
    # 05 - Listas e Dicionários
    # data_array.append(["def intercala(lista1: List[int],lista2: List[int]) -> List[int]:\n    lista3 = 6*[0]\n    lista3[::2] = lista1\n    lista3[1::2] = lista2\n    return lista3\n", "Faça uma função chamada definida por **\\`intercala(lista1, lista2)\\`** que dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que é formada intercalando os elementos de L1 e L2. \n\n\n\nExemplo:\n\nL1 = [1, 3, 5] e L2 = [2, 4, 6] gera L3 = [1, 2, 3, 4, 5, 6].", "Listas e Dicionários"])
    # data_array.append(["def pontos_por_time(jogos: list[list[str, str, list[int, int]]]) -> dict[str, int]:\n    pontuacao = {}\n    \n    for jogo in jogos:\n        time1 = jogo[0]\n        time2 = jogo[1]\n        if time1 not in pontuacao:\n            pontuacao[time1] = 0\n        if time2 not in pontuacao:\n            pontuacao[time2] = 0\n            \n        resultado = jogo[2]\n        if resultado[0] > resultado[1]:\n            pontuacao[time1] += 3\n        elif resultado[0] < resultado[1]:\n            pontuacao[time2] += 3\n        else:\n            pontuacao[time1] += 1\n            pontuacao[time2] += 1\n            \n    return pontuacao\n", "Faça uma função chamada pontos_por_time  que receba uma lista de dois elementos, onde cada elemento é também uma lista. A lista completa tem informações do número de gols em dois jogos de futebol entre dois times (jogo da ida e jogo da volta), no seguinte formato: [['Cormengo', 'Flamínthians', [1, 0]], ['Flamínthians', 'Cormengo', [2, 2]]].Nesta lista de exemplo, no primeiro jogo entre Cormengo e Flamínthians, o Cormengo fez 1 gol e o Flamínthians não fez gol. Sua função deve retornar um dicionário cujos mapeamentos são: <nome do time>  -> <numero total de pontos na fase>. Os pontos de um time na fase são calculados da seguinte forma: em cada jogo, os times recebem três pontos por vitória e um ponto por empate. Não são atribuídos pontos para derrotas. O total de pontos de uma fase é a soma de pontos dos dois jogos da fase. Na lista de exemplo, o total de pontos do Cormengo é 4 e do Flamínthians é 1.", "Listas e Dicionários"])
    # data_array.append(["def colchao(lista: list[int],H: int,L: int) -> bool:\n    maior = max(L,H)\n    menor = min(L,H)\n    if lista[1] > maior:\n        return False\n    else:\n        if lista[0] > menor:\n            return False\n        else:\n            return True\n", "Questão OBI (Olimpíada Brasileira de Informática - OBI2012, Fase 1, Nível 2) - (Colchão)\n\nJoão está comprando móveis novos para sua casa. Agora é a vez de comprar um colchão novo, de molas, para substituir o colchão velho. As portas de sua casa têm altura H e largura L e existe um colchão que está em promoção com dimensões A × B × C. O colchão tem a forma de um paralelepípedo reto retângulo e João só consegue arrastá-lo através de uma porta com uma de suas faces paralelas ao chão, mas consegue virar e rotacionar o colchão antes de passar pela porta. Entretanto, de nada adianta ele comprar o colchão se ele não passar através das portas de sua casa. Portanto ele quer saber se consegue passar o colchão pelas portas e para isso precisa de sua ajuda. Faça uma função definida por colchao(medidas,H,L) para resolver esse problema, onde medidas é uma lista com os tamanhos inteiros A, B e C, e H e L são os tamanhos inteiros da altura e largura da porta, respectivamente.\nEntrada: Os parâmetros de entrada são uma lista com as dimensões do colchão em centímetros, ordenadas da menor para a maior, e dois inteiros H e L, correspondentes respectivamente a altura e a largura das portas em centímetros.\nSaída: A sua função deve retornar True se o colchão passa pelas portas e False caso contrário.\nExemplos:\nEntrada: [25,120,220], 200, 100 ; Saída: True\nEntrada: [25,205,220], 200, 100 ; Saída: False\nEntrada: [25,200,220], 200, 100 ; Saída: True", "Listas e Dicionários"])
    
    # (DES) 08 - Estrutura de Repetição - for
    # data_array.append(["def soma_h(n: int) -> float:\n    soma = 0\n    for denominador in range(1,n+1):\n        soma += 1.0/denominador\n    return round(soma,2)", "Faça uma função chamada soma_h para calcular e retornar o valor H com N termos onde N é inteiro e dado com entrada. Retorne seu resultado somente com 2 casas decimais, utilizando a função round(número, 2)", "Estrutura de repetição iteradora: for"])
    # data_array.append(["def divisores(n: int) -> int:\n    total = 0\n    for contador in range(1,n+1):\n        if n%contador == 0:\n            total += 1\n    return total", "Faça uma função chamada divisores que conte quantos divisores um número tem. Este número será passado como argumento de entrada. Exemplo: Se o número for 10, os divisores são: 1, 2, 5 e 10; total de 4 divisores.", "Estrutura de repetição iteradora: for"])
    data_array.append(["def freq_palavras(frase: str) -> dict:\n    if not re.fullmatch(\"((another)|(value)|(test)| )*\", frase):\n        return None\n    dic = {}\n    lista = frase.split()\n    for palavra in lista:\n        if palavra in dic:\n            dic[palavra] += 1\n        else:\n            dic[palavra] = 1\n    return dic\n", "Construa uma função chamada **freq_palavras(frases)** que receba uma string e retorne um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece. Por exemplo: \n\n- freq_palavras(\"dinheiro é dinheiro e vice versa\") \n\nRetorna o dicionário: { \"dinheiro\":2, \"é\": 1, \"e\": 1, \"vice\": 1, \"versa\":1}", "Estrutura de repetição iteradora: for"])
    # data_array.append(["def lingua_p(palavra: str) -> str:\n    palavra = str.lower(palavra)\n    traduzida = ''\n    for c in palavra:\n        traduzida = traduzida + c\n        if c in 'aeiouáàãâéêíóòõú':\n            traduzida = traduzida + 'p' + c\n    return traduzida\n", "Faça uma função chamada lingua_p que receba como parâmetro uma palavra e retorne esta mesma palavra traduzida para a lingua do P. Uma palavra é traduzida para a lingua do P quando, após cada vogal da palavra original, é inserida a sequencia de letras p mais a vogal original.\n\nPor exemplo:\n\nexemplo → epexepemplopo\n\nentao → epentapaopo\n\ncaderno → capadepernopo", "Estrutura de repetição iteradora: for"])
    # data_array.append(["def count(frase: str, letra: str) -> int:\n    contador = 0\n    for l in frase.lower():\n        if letra == l:\n            contador += 1\n    return contador", "Faça uma função chamada count  que dada uma frase e uma letra, conte quantas vezes aquela letra aparece na frase, só que sem usar a função count()\nAtenção!Maiúsculas e minúsculas também contam! Mas o computador não sabe que elas são iguais, você precisa antes transformá-las!", "Estrutura de repetição iteradora: for"])
    
    # data_array.append(["def fatorial(n: int) -> int:\n    fat = 1\n    while n>0:\n        fat = fat*n\n        n = n-1\n    return fat\n", "Faça uma função chamada **fatorial** que dado um número, calcule o fatorial deste número. (Não usar a função factorial do módulo math)", "Estrutura de repetição com teste de parada: While"])
    # data_array.append(["def posLetra(frase: str, letra: str, ocorrencia: int) -> int:\n    pos = 0\n    contador = 0\n    while pos < len(frase):\n        if frase[pos] == letra:\n            contador = contador + 1\n            if contador == ocorrencia:\n                return pos\n        pos = pos + 1\n    return 'Ocorrência não encontrada'\n", "Faça uma função chamada **posLetra** que recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra (1 para primeira ocorrência, 2 para segunda, etc). Sua função deve retornar em que posição da string aquela ocorrência da letra está. Caso exista menos ocorrências da letra do que a ocorrência pedida, a função deve mostrar a mensagem \"Ocorrência não encontrada\".\n\nExemplo:\n\n>>> posLetra(\"mariana come banana\", \'a\', 3)\n\n6\n\n(posição da terceira ocorrência da letra \'a\' na string dada)", "Estrutura de repetição com teste de parada: While"])
    # data_array.append(["def faltante(pecas: List[int]) -> int:\n    lp = pecas[:]\n    lp.sort()\n    contador = 0\n    peca = -1\n    while (contador < len(lp)):\n        if (lp[contador] == (contador + 1)):\n            contador = contador + 1\n        else:\n            peca = contador + 1\n            contador = len(lp)\n    if (peca == -1):\n        peca = len(lp) + 1\n    return peca\n", "*Questão OBI (Olimpíada Brasileira de Informática - OBI2007, Fase 1, Nível 1) - (Peça Perdida)*\n\nJoãozinho adora quebra-cabeças, essa é sua brincadeira favorita. O grande problema, porém, é que às vezes o jogo vem com uma peça faltando. Isso irrita bastante o pobre menino, que tem de descobrir qual peça está faltando e solicitar uma peça de reposição ao fabricante do jogo. Sabendo que o quebra-cabeças tem N peças, numeradas de 1 a N e que exatamente uma está faltando, ajude Joãozinho a saber qual peça ele tem de pedir.\n\nEscreva uma função chamada **faltante** que, dada uma lista com N − 1 inteiros numerados de 1 a N, descubra qual número inteiro deste intervalo está faltando.\n\n- **Entrada:** O parâmetro de entrada é uma lista L de tamanho N − 1 contendo números inteiros (não repetidos) de 1 a N.\n- **Saída:** A sua função deve retornar o número inteiro x que pertence ao intervalo [1, N] mas que não pertence a lista de entrada L.\n\nExemplos:\n\n- Entrada: [3,1];\nSaída: 2\n- Entrada: [1,2,3,5] ;\nSaída: 4\n- Entrada: [2,4,3] ;\nSaída: 1", "Estrutura de repetição com teste de parada: While"])
    # data_array.append(["def bolo(a: int,b: int,c: int) -> int:\n    return min(a//2,b//3,c//5)\n", "*Questão OBI (Olimpíada Brasileira de Informática - OBI2012, Fase 2, Nível Júnior) - (Receita de Bolo)*\n\nJoão deseja fazer bolos para seus amigos, usando uma receita que indica que devem ser usadas 2 xícaras de farinha de trigo, 3 ovos e 5 colheres de sopa de leite.\nEm casa ele tem **A** xícaras de farinha de trigo, **B** ovos e **C** colheres de sopa de leite. João não tem muita prática com a cozinha, e portanto ele só se arriscará a\nfazer medidas exatas da receita de bolo (por exemplo, se ele tiver material suficiente para fazer mais do que 2 e menos do que 3 bolos, ele fará somente 2 bolos). \nSabendo disto, ajude João escrevendo uma função chamada **bolos** que determine qual a quantidade máxima de bolos que ele consegue fazer.\n\n- **Entrada:** Os parâmetros de entrada da função são três números inteiros A, B e C, indicando respectivamente o número de xícaras de farinha de trigo, o número de ovos e o número de colheres de sopa de leite que João tem em casa.\n\n- **Saída:** Sua função deve retornar a quantidade máxima de bolos que João consegue fazer.\n\nExemplos:\n\n- Entrada: 4, 6, 10;\nSaída: 2\n- Entrada: 4, 6, 9 ;\nSaída: 1'", "Funcoes e Tipos de dados"])
    
    # data_array.append(["def total(compras: List[int], produtos: Dict[str, float]) -> float:\n    soma = 0\n    for produto in compras:\n        if produto in produtos:\n            soma += produtos[produto]\n    return round(soma,2)", "Escreva uma função chamada total que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja. Por exemplo, para os dados:\nlista de compras = [’biscoito’, ’chocolate’, ’farinha’]\nprodutos = { ’amaciante’:4.99, ’arroz’:10.90, ’biscoito’:1.69, ’cafe’:6.98, ’chocolate’:3.79, ’farinha’:2.99 } \nO valor retornado pela função será 8.47. Retorne seu resultado somente com 2 casas decimais, utilizando a função round(número, 2).", "Dicionário"])
    # data_array.append(["def insere(lista: List[int], n: int) -> List[int]:\n    lista=lista+[n]\n    return sorted(lista)", "Faça uma função definida por insere(lista_numero, n) que dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta. Retorne a lista atualizada.", "Listas"])
    # data_array.append(["def maiores(lista: List[int], n: int):\n    lista = lista+[n]\n    list.sort(lista)\n    list.reverse(lista)\n    indice=list.index(lista,n)\n    sublista=lista[:indice]\n    list.sort(sublista)\n    list.reverse(sublista)\n    return str(sublista)", "Faça uma função chamada maiores que dada uma lista ordenada L (decrescente) de números inteiros e um número inteiro n, retorne a sublista formada por todos os elementos maiores que n em ordem decrescente.", "Listas"])
    
    
    # data_array.append(["method", "context", "theme"])
    # data_array.append(["method", "context", "theme"])
    # data_array.append(["method", "context", "theme"])
    # data_array.append(["method", "context", "theme"])
    # data_array.append(["method", "context", "theme"])
    # data_array.append(["method", "context", "theme"])
    # data_array.append(["method", "context", "theme"])
    # data_array.append(["method", "context", "theme"])
    # data_array.append(["method", "context", "theme"])
    return data_array