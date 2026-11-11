while True:
    # 1. Menu Interativo (Estrutura Condicional)
    print("\n=== MENU DE JOGADORES ===")
    print("1 - Ver Jogadores Cadastrados")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Lista de Jogadores ---")
        try:
            # 2. Ler dados armazenados no arquivo TXT
            arquivo = open("jogadores.txt", "r") # 'r' significa read (ler)
            conteudo = arquivo.read()

            # 3. Exibir informações no terminal
            if conteudo == "":
                print("Nenhum jogador cadastrado ainda.")
            else:
                print(conteudo)

            arquivo.close()
        except FileNotFoundError:
            print("Nenhum jogador cadastrado ainda. (Arquivo não encontrado)")

    elif opcao == "2":
        print("Saindo do programa...")
        break
    else:
        print("❌ Opção inválida! Escolha 1 ou 2.")
        