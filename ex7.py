# Abrir o arquivo de texto
with open('names.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

    contagem_nomes = {}

    for linha in linhas:
        nome = linha.strip()

        if nome in contagem_nomes:
            contagem_nomes[nome] += 1
        else:
            contagem_nomes[nome] = 1

    print("Contagem de nomes:")
    for nome, contagem in contagem_nomes.items():
        print(f"{nome}: {contagem} vezes")
