import random

def jogo_forca():
    jogos = [
        "minecraft", "roblox", "valorant", "fortnite", "csgo",
        "league of legends", "free fire", "call of duty", "fifa 23", "pes 2021",
        "gta v", "red dead redemption 2", "among us", "fall guys", "apex legends",
        "overwatch", "rainbow six siege", "the witcher 3", "cyberpunk 2077", "elden ring",
        "dark souls", "bloodborne", "resident evil 4", "resident evil village", "silent hill",
        "god of war", "horizon zero dawn", "the last of us", "uncharted 4", "spider-man",
        "batman arkham knight", "assassin's creed valhalla", "assassin's creed odyssey", "watch dogs 2", "far cry 5",
        "far cry 6", "borderlands 3", "destiny 2", "halo infinite", "forza horizon 5",
        "need for speed heat", "gran turismo 7", "rocket league", "brawl stars", "clash royale",
        "clash of clans", "subway surfers", "temple run", "plants vs zombies", "angry birds"
    ]
    animais = [
        "Leão", "Elefante", "Sapo", "Arara", "Tubarão",
        "Cachorro", "Gato", "Cavalo", "Vaca", "Porco",
        "Galinha", "Pato", "Peru", "Coelho", "Ovelha",
        "Cabra", "Leopardo", "Tigre", "Urso", "Lobo",
        "Raposa", "Hiena", "Girafa", "Zebra", "Rinoceronte",
        "Hipopótamo", "Canguru", "Coala", "Panda", "Macaco",
        "Chimpanzé", "Gorila", "Crocodilo", "Jacaré", "Águia",
        "Falcão", "Coruja", "Pinguim", "Golfinho", "Baleia",
        "Polvo", "Lula", "Caranguejo", "Lagosta", "Formiga",
        "Abelha", "Borboleta", "Mosquito", "Cobra", "Lagarto"
    ]
    programacao = [
        "ALGORITMO", "PROGRAMA", "CODIGO", "VARIAVEL", "FUNCAO",
        "CLASSE", "OBJETO", "HERANCA", "LOOP", "CONDICAO",
        "PYTHON", "JAVA", "JAVASCRIPT", "HTML", "CSS",
        "REACT", "NODE", "SQL", "BANCO", "DADOS",
        "SERVIDOR", "CLIENTE", "API", "JSON", "DEBUG",
        "COMPILADOR", "INTERPRETADOR", "FRAMEWORK", "BIBLIOTECA", "GIT",
        "GITHUB", "VERSIONAMENTO", "DEPLOY", "CLOUD", "HOSPEDAGEM",
        "DOMINIO", "BACKEND", "FRONTEND", "FULLSTACK", "SCRIPT",
        "TERMINAL", "LINUX", "WINDOWS", "MACOS", "INTELIGENCIA",
        "ARTIFICIAL", "MACHINE", "LEARNING", "DADOS", "SEGURANCA"
    ]
    
    palavra = random.choice(programacao)

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
        palavra = random.choice(jogos)
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

