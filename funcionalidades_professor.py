from os import replace

posicao_codigo_turma = 0
posicao_codigo_disciplina = 1
posicao_nome_disciplina = 2
posicao_ano_semestre = 3
posicao_horario = 4
posicao_forma_avaliacao = 5
posicao_quantidade_avaliacoes = 6


def exibir_nota(alunos, pesos, quantidade_avaliacoes):
    if pesos:
        for i in range(quantidade_avaliacoes):
            peso = pesos[i]
            print(f"Peso {i + 1}: {peso}")
    for aluno in alunos:
        print(f"Nome: {aluno[0]}, DRE: {aluno[1]}")
        for i in range(quantidade_avaliacoes):
            nota = aluno[3:][i]
            print(f"Nota {i + 1}: {nota}")


def exibir_medias(alunos, pesos, quantidade_avaliacoes, forma_avaliacao):
    for aluno in alunos:
        if forma_avaliacao == "a":
            media = (
                sum(float(aluno[3:][i]) for i in range(quantidade_avaliacoes))
                / quantidade_avaliacoes
            )
        else:
            soma = sum(
                pesos[i] * float(aluno[3:][i]) for i in range(quantidade_avaliacoes)
            )
            media = soma / sum(pesos)
        print(f"Nome: {aluno[0]}, DRE: {aluno[1]}, Média: {media}")


def exibir_frequencia(alunos):
    for aluno in alunos:
        print(f"Nome: {aluno[0]}, DRE: {aluno[1]}, Frequência: {aluno[2]}%")


def exibir_info_turma(turma, formas_avaliacao, pesos, quantidade_avaliacoes):
    print(f"Código da disciplina: {turma[0]}")
    print(f"Nome da disciplina: {turma[1]}")
    print(f"Código da turma: {turma[2]}")
    print(f"Semestre: {turma[3]}")
    print(f"Horário: {turma[4]}h")
    forma_avaliacao_completa = (
        "Média Aritmética" if formas_avaliacao == "a" else "Média Ponderada"
    )
    print(f"Forma de avaliação: {forma_avaliacao_completa}")
    print(f"Avaliações: {turma[6]}")
    if pesos:
        for i in range(quantidade_avaliacoes):
            peso = pesos[i]
            print(f"Peso {i + 1}: {peso}")


def cadastrar_turma(nome_professor):
    # verifica se a turma existe, se existir volta para o menu
    codigo_turma = input("Código da turma: ").lower()
    with open("arquivos/turmas.txt", "a+") as arquivo:
        for linha in arquivo:
            codigo_turma_cadastrado = linha.strip().split(",")[posicao_codigo_turma]
            if codigo_turma_cadastrado == codigo_turma:
                print("Turma já cadastrada.")
                return

    # pede os dados da turma
    codigo_disciplina = input("Código da disciplina: ").lower()
    nome_disciplina = input("Nome da disciplina: ").lower()
    ano_semestre = input("Ano e semestre: ")
    horario = input("Horário: ")
    formas_avaliacao = input("Formas de avaliação: a/p ").lower()
    quantidade_avaliacoes = int(input("Quantas avaliações: "))

    # define os pesos das avaliacoes
    pesos = ("1," * quantidade_avaliacoes).rstrip(",")
    if formas_avaliacao == "p":
        pesos = input("Digite os pesos separados por vírgula: ")

    # dados iniciais dos alunos
    frequencia = 0
    notas = ("0," * quantidade_avaliacoes).rstrip(",")

    # mostra os alunos cadastrados no sistema
    if input("Ver alunos cadastrados no sistema: s/n ").lower() == "s":
        with open("arquivos/alunos.txt", "r") as arquivo:
            for linha in arquivo:
                nome_cadastrado, dre_cadastrado = linha.strip().split(",")
                print(f"Nome: {nome_cadastrado.title()}, DRE: {dre_cadastrado}")

    # verifica se o aluno sendo cadastrado na turma existe no sistema
    alunos = []
    while True:
        nome = input("Nome do aluno: ")
        dre = input("DRE do aluno: ")
        aluno_existe = False
        with open("arquivos/alunos.txt", "r") as arquivo:
            for linha in arquivo:
                nome_cadastrado, dre_cadastrado = linha.strip().split(",")
                if nome_cadastrado == nome and dre_cadastrado == dre:
                    aluno_existe = True
                    break

        if not aluno_existe:
            print("Aluno não encontrado, verifique a digitação")
            continue

        alunos.append((nome, dre, frequencia, notas))

        if input("Deseja adicionar mais um aluno (s/n)? ").lower() != "s":
            break

    # formata as informacoes para serem gravadas
    turma_info = f"{codigo_turma},{nome_disciplina},{codigo_disciplina},{ano_semestre},{horario},{formas_avaliacao},{quantidade_avaliacoes},{pesos},{nome_professor}"
    alunos_info = ",".join(
        [f"{aluno[0]},{aluno[1]},{aluno[2]},{aluno[3]}" for aluno in alunos]
    )

    # salva a turma e os alunos no arquivo
    with open("arquivos/turmas.txt", "a") as arquivo:
        arquivo.write(f"{turma_info}{alunos_info}\n")
        print("Turma cadastrada com sucesso.")


def excluir_turma():
    codigo_turma = input("Código da turma: ")
    # abre o arquivo original para leitura e um temporario para escrita
    with open("arquivos/turmas.txt", "r") as arquivo, open(
        "arquivos/turmas_temp.txt", "w"
    ) as arquivo_temp:
        for linha in arquivo:
            codigo_turma_cadastrado = linha.strip().split(",")[posicao_codigo_turma]
            # se o codigo não for o codigo da turma a ser excluida, escreve no arquivo temporario
            if codigo_turma_cadastrado != codigo_turma:
                arquivo_temp.write(linha)
    replace("arquivos/turmas_temp.txt", "arquivos/turmas.txt")


def exibir_informacoes_turma():
    codigo_turma = input("Código da turma: ")
    if not turma_existe(codigo_turma):
        print("Turma não existe")
        return
    with open("arquivos/turmas.txt", "r") as turmas:
        for turma in turmas:
            turma = turma.strip().split(",")
            if turma[2] == codigo_turma:
                quantidade_avaliacoes = int(turma[6])
                forma_avaliacao = turma[5]
                pesos = None

                if forma_avaliacao == "p":
                    pesos = list(map(int, turma[7 : 7 + quantidade_avaliacoes]))

                alunos = carrega_alunos(turma, forma_avaliacao)

                while True:
                    print("1. Ver as notas")
                    print("2. Ver as médias")
                    print("3. Ver a frequência")
                    print("4. Ver informações da turma")
                    print("5. Sair")
                    escolha = input("O que quer fazer: ")
                    if escolha == "1":
                        exibir_nota(alunos, pesos, quantidade_avaliacoes)
                    elif escolha == "2":
                        exibir_medias(
                            alunos, pesos, quantidade_avaliacoes, forma_avaliacao
                        )
                    elif escolha == "3":
                        exibir_frequencia(alunos)
                    elif escolha == "4":
                        exibir_info_turma(
                            turma, forma_avaliacao, pesos, quantidade_avaliacoes
                        )
                    elif escolha == "5":
                        break
                    else:
                        print("Opção inválida!")


def calcular_estatisticas_turma():
    pass


def exibir_informacoes_aluno():
    dre = input("Digite o DRE do aluno ")
    # printa as info da turma
    with open("arquivos/turmas.txt", "r") as turmas:
        for turma in turmas:
            turma = turma.strip().split(",")
            forma_avaliacao = turma[5]
            quantidade_avaliacoes = int(turma[6])
            pesos = None
            alunos = carrega_alunos(turma, forma_avaliacao)
            for aluno in alunos:
                if dre in aluno:
                    print(f"Código da disciplina: {turma[0]}")
                    print(f"Nome da disciplina: {turma[1]}")
                    print(f"Código da turma: {turma[2]}")
                    if forma_avaliacao == "p":
                        pesos = list(map(int, turma[7 : 7 + quantidade_avaliacoes]))
                        for i in range(quantidade_avaliacoes):
                            peso = pesos[i]
                            print(f"Peso {i + 1}: {peso}")
                    # printa as notas
                    for i in range(quantidade_avaliacoes):
                        nota = aluno[3:][i]
                        print(f"Nota {i + 1}: {nota}")
                    # printa a media
                    if forma_avaliacao == "a":
                        media = (
                            sum(
                                float(aluno[3:][i])
                                for i in range(quantidade_avaliacoes)
                            )
                            / quantidade_avaliacoes
                        )
                    else:
                        soma = sum(
                            pesos[i] * float(aluno[3:][i])
                            for i in range(quantidade_avaliacoes)
                        )
                        media = soma / sum(pesos)
                    print(
                        f"Nome: {aluno[0]}, DRE: {aluno[1]}, Frequência: {aluno[2]}, Média: {media}"
                    )
