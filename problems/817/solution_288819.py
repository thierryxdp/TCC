def acima_da_media(lista):
    """Dada uma lista com notas dos alunos da turma, retorne uma lista ordenada com notas acima da média"""
    medi
    "media = soma / len(list)\n",
    "\n",
    "maisProximo = list[0]\n",
    "diferenca = media - list[0]\n",
    "menorDiferenca = diferenca\n",
    "for num in list:\n",
    "    #valor mais próximo da média\n",
    "    diferenca = media - num\n",
    "    if diferenca < 0:\n",
    "        diferenca = diferenca * -1\n",
    "    if diferenca < menorDiferenca:\n",
    "        menorDiferenca = diferenca\n",
    "        maisProximo = num\n",