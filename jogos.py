import adivinhacao
import forca

while True:
    print("\n" + "================================================")
    print("         MENU DE JOGOS")
    print("================================================")
    print("1. Jogo de Adivinhação")
    print("2. Jogo da Forca")
    print("3. Sair")
    print("================================================")
    
    opcao = input("Escolha uma opção (1-3): ").strip()
    
    if opcao == "1":
        adivinhacao.jogo_adivinhacao()
    elif opcao == "2":
        forca.jogo_forca()
    elif opcao == "3":
        print("Obrigado por jogar! Até a próxima!")
        break
    else:
        print("Opção inválida. Tente novamente.")