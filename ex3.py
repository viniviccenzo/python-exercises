while True:
    print("Jogador 1, faça sua jogada (pedra, papel ou tesoura):")
    jogador1 = input().lower()
    print("Jogador 2, faça sua jogada (pedra, papel ou tesoura):")
    jogador2 = input().lower()

    jogadas_validas = ["pedra", "papel", "tesoura"]
    if jogador1 not in jogadas_validas or jogador2 not in jogadas_validas:
        print("Jogada inválida. Por favor, digite novamente.")
        continue

    if jogador1 == jogador2:
        print("Empate!")
    elif (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "papel" and jogador2 == "pedra") or (jogador1 == "tesoura" and jogador2 == "papel"):
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")

    continuar = input("Deseja continuar jogando? (s/n): ")
    if continuar.lower() != "s":
        break
