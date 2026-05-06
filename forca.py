import random
from programacao import programacao
from animais import animais
from jogo import jogo

def jogo_forca():
    
    print("Bem-vindo ao jogo da forca!")
    print("================================================")
    print("Escolha uma categoria:")
    print("================================================")
    print("1. Jogos")
    print("2. Animais")
    print("3. Programação")
    print("================================================")

    opcao = input("Digite o número da categoria desejada: ")

    if opcao == "1":
        palavra = random.choice(jogo)
    elif opcao == "2":
        palavra = random.choice(animais)
    elif opcao == "3":
        palavra = random.choice(programacao)
    else:
        print("Opção inválida. Escolhendo Programação por padrão.")
        palavra = random.choice(programacao)

    letras_acertadas = []
    for letra in palavra:
        if letra == " ":
            letras_acertadas.append(" ")
        else:
            letras_acertadas.append("_")

    acertou = False
    enforcou = False
    limite_tentativas = len(palavra.replace(" ", "")) + 6
    tentativas_restantes = limite_tentativas
    letras_tentadas = []

    def mostrar_letras_acertadas():
        for letra in letras_acertadas:
            print(letra, end=" ")

    print("Tente adivinhar a palavra secreta: ")
    while not acertou and not enforcou:
        # mostrar as letras acertadas
        mostrar_letras_acertadas()
        print("")
        print(f"Tentativas restantes: {tentativas_restantes}")
        if letras_tentadas:
            print("Letras já tentadas:", ", ".join(letras_tentadas))

        chute = input("Digite uma letra: ").strip()
        if not chute:
            print("Digite pelo menos uma letra.")
            continue

        letra_chute = chute[0].upper()
        if letra_chute in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.append(letra_chute)

        acertou_letra = False
        for i in range(len(palavra)):
            if letra_chute == palavra[i].upper():
                letras_acertadas[i] = palavra[i]
                acertou_letra = True

        if not acertou_letra:
            tentativas_restantes -= 1
            print(f"Que pena! A letra '{letra_chute}' não está na palavra.")

        if tentativas_restantes <= 0:
            print("Você perdeu :(\nA palavra era:", palavra)
            enforcou = True
            break

        if "_" not in letras_acertadas:
            print("Parabéns, você acertou a palavra secreta!")
            mostrar_letras_acertadas()
            acertou = True

