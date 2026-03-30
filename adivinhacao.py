import random

def jogo_adivinhacao():
    print("Escolha o nível de dificuldade:")
    print("1. Fácil (1-10)")
    print("2. Médio (1-50)")
    print("3. Difícil (1-100)")
    
    while True:
        nivel = input("Digite o número do nível (1-3): ").strip()
        if nivel == "1":
            max_num = 10
            break
        elif nivel == "2":
            max_num = 50
            break
        elif nivel == "3":
            max_num = 100
            break
        else:
            print("Opção inválida. Tente novamente.")
    
    numero_secreto = random.randint(1, max_num)
    tentativas = 0
    print(f"Bem-vindo ao jogo de Adivinhação!")
    print(f"Tente adivinhar o número secreto entre 1 e {max_num}.")
    
    while True:
        try:
            chute = int(input("Digite seu palpite: "))
            tentativas += 1
            if chute < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif chute > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, digite um número válido.")

