# Listas para armazenar os dados do usuário
usuarios = []



# Função para cadastrar usuário
def cadastrar_usuario():
    try:
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        endereco = input("Digite seu endereço: ")
        modelo = input("Insira o modelo de seu veículo: ")
        placa = input("Insira a placa de seu veículo: ")

      

        # Adiciona os dados 
        usuarios.append({
            'nome': nome,
            'email': email,
            'senha': senha,
            'endereco': endereco,
            'modelo': modelo,
            'placa': placa
        })
        print("Cadastro realizado com sucesso!")
    except ValueError as e:
        print(f"Erro no cadastro: {e}")

# Função para listar usuários
def listar_usuarios():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        for idx, usuario in enumerate(usuarios, start=1):
            print(f"{idx}. Nome: {usuario['nome']}, Email: {usuario['email']}, Placa: {usuario['placa']}")

# Função para atualizar usuário
def atualizar_usuario():
    listar_usuarios()
    try:
        idx = int(input("Selecione o número do usuário que deseja atualizar: ")) - 1
        if 0 <= idx < len(usuarios):
            usuarios[idx]['nome'] = input(f"Novo nome ({usuarios[idx]['nome']}): ") or usuarios[idx]['nome']
            usuarios[idx]['email'] = input(f"Novo email ({usuarios[idx]['email']}): ") or usuarios[idx]['email']
            usuarios[idx]['senha'] = input(f"Nova senha: ") or usuarios[idx]['senha']
            usuarios[idx]['endereco'] = input(f"Novo endereço ({usuarios[idx]['endereco']}): ") or usuarios[idx]['endereco']
            usuarios[idx]['modelo'] = input(f"Novo modelo ({usuarios[idx]['modelo']}): ") or usuarios[idx]['modelo']
            usuarios[idx]['placa'] = input(f"Nova placa ({usuarios[idx]['placa']}): ") or usuarios[idx]['placa']
            print("Usuário atualizado com sucesso!")
        else:
            print("Usuário não encontrado.")
    except (ValueError, IndexError):
        print("Entrada inválida.")

# Função para excluir usuário
def excluir_usuario():
    listar_usuarios()
    try:
        idx = int(input("Selecione o número do usuário que deseja excluir: ")) - 1
        if 0 <= idx < len(usuarios):
            usuarios.pop(idx)
            print("Usuário excluído com sucesso!")
        else:
            print("Usuário não encontrado.")
    except (ValueError, IndexError):
        print("Entrada inválida.")

# Função de cadastro de usuário
def cadastro_usuario():
    while True:
        print("\n--- CADASTRO DO USUAIO ---")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Excluir Usuário")
        print("5. Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            atualizar_usuario()
        elif opcao == '4':
            excluir_usuario()
        elif opcao == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função principal
def menu_principal():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Serviços")
        print("2. Chat Bot")
        print("3. Mecânicas")
        print("4. CRUD Usuários")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            servicos()
        elif opcao == '2':
            chat_bot()
        elif opcao == '3':
            mecanicas()
        elif opcao == '4':
            cadastro_usuario()
        elif opcao == '5':
            sair()
            break
        else:
            print("Opção inválida.")

def servicos():
    print("Lista de serviços: \n1. Troca de Óleo - R$ 100,00\n2. Revisão - R$ 80,00\n3. Troca de Pneu - R$ 600,00")

def chat_bot():
    print("Reconhecer problemas no carro\nAgende uma revisão\nPreço das peças\n")

def mecanicas():
    print("Mecânicas disponíveis:\n1. Centro Automotivo - Bela Vista\n2. Centro Automotivo - Rio Branco\n3. Centro Automotivo - Canindé")

def sair():
    print("Obrigado pela preferência!")

# Executar o menu principal
menu_principal()
