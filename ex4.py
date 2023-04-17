import random

while True:
    numero_secreto = random.randint(1, 9)

    while True:
        tentativa = input("Adivinhe o número entre 1 e 9 (ou digite 'sair' para sair): ")
        if tentativa.lower() == "sair":
            break
        elif not tentativa.isdigit():
            print("Por favor, digite apenas números.")
        else:
            tentativa = int(tentativa)
            if tentativa < 1 or tentativa > 9:
                print("Por favor, digite um número válido entre 1 e 9.")
            else:
                if tentativa < numero_secreto:
                    print("Tentativa menor. Tente novamente.")
                elif tentativa > numero_secreto:
                    print("Tentativa maior. Tente novamente.")
                else:
                    print("Parabéns! Você acertou!")
                    break

    continuar = input("Deseja jogar novamente? (s/n): ")
    if continuar.lower() != "s":
        break
