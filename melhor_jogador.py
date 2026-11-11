# # 1. Abre o arquivo jogadores.txt para leitura
arquivo = open("jogadores.txt", "r")
linhas = arquivo.readlines() # # Lê todas as linhas e guarda em uma lista
arquivo.close()

# # 2. Inicializa as variáveis para a busca (Exatamente como no slide)
maior_pontuacao = -1 # Inicializado com um valor baixo
melhor_jogador = ""

# # 3. Percorre cada linha do arquivo procurando o campeão
for linha in linhas:
    # # Remove espaços em branco ou quebras de linha invisíveis nas pontas
    linha = linha.strip()
    
    # # Se a linha estiver em branco, pula para a próxima
    if not linha:
        continue
        
    # # Separa o nome e a pontuação usando o '-' apenas se ele existir na linha
    if '-' in linha:
        nome, pts = linha.split('-')
        nome = nome.strip()
        pts = int(pts.strip()) # Converte a pontuação para número inteiro
        
        # # Verifica se este jogador tem a maior pontuação até agora
        if pts > maior_pontuacao:
            maior_pontuacao = pts
            melhor_jogador = nome

# # 4. Exibe o resultado final fora do loop
print(f"O melhor jogador é {melhor_jogador} com {maior_pontuacao} pontos.")