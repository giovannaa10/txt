# Função para salvar o jogador no arquivo TXT
def salvar_jogador(nome, pontuacao):
    # O modo 'a' (append) adiciona o texto ao final
    with open("jogadores.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{pontuacao}\n")
    print(f"🎮 Jogador {nome} cadastrado com sucesso!")

# Função para buscar o jogador com maior pontuação
def buscar_melhor_jogador():
    try:
        with open("jogadores.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        
        maior_pontuacao = -1
        melhor_jogador = ""

        for linha in linhas:
            linha_limpa = linha.strip()
            # Garante que a linha não está vazia e que contém a vírgula antes de separar
            if linha_limpa and "," in linha_limpa:
                nome, pts = linha_limpa.split(",")
                if int(pts) > maior_pontuacao:
                    maior_pontuacao = int(pts)
                    melhor_jogador = nome

        if melhor_jogador:
            print(f"🏆 Melhor jogador: {melhor_jogador} com {maior_pontuacao} pontos")
        else:
            print("Nenhum jogador encontrado.")
    except FileNotFoundError:
        print("O arquivo jogadores.txt ainda não existe.")

# Função principal do cadastro
def menu():
    while True:
        print("\n=== CADASTRO DE JOGADORES ===")
        print("1 - Cadastrar Novo Jogador")
        print("2 - Exibir Melhor Jogador")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do jogador: ")
            pontuacao = input("Digite a pontuação inicial: ")
            salvar_jogador(nome, pontuacao)
        elif opcao == "2":
            buscar_melhor_jogador()
        elif opcao == "3":
            print("Saindo do programa. Até logo!")
            break

# Executa o programa
menu()