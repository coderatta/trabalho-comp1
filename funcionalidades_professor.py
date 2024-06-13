from os import path, replace


# funciona
def turma_existe(codigo_turma):
    try:
        if path.exists("arquivos/turmas.txt"):
            with open("arquivos/turmas.txt", "r") as turmas:
                for linha in turmas:
                    campos = linha.strip().split(",")
                    codigo_turma_existente = campos[2]
                    if codigo_turma == codigo_turma_existente:
                        return True
                return False
    except FileNotFoundError:
        print("Arquivo de turmas não encontrado.")
        return False


# funciona
def cadastrar_turma():
    codigo_turma = input("Código da turma: ")
    if turma_existe(codigo_turma):
        print("Turma já existe.")
        return

    # pede os dados da turma
    codigo_disciplina = input("Código da disciplina: ")
    nome_disciplina = input("Nome da disciplina: ")
    ano_semestre = input("Ano e semestre: ")
    horario = input("Horário: ")
    formas_avaliacao = input("Formas de avaliação: a/p ")
    quantidade_avaliacoes = int(input("Quantas avaliações: "))
    if formas_avaliacao == "p":
        pesos = input("Digite os pesos separados por vírgula: ")

    # mostra os alunos cadastrados no sistema
    print("Adicionar alunos.")
    escolha = input("Ver alunos cadastrados no sistema: s/n ")
    if escolha == "s":
        if path.exists("arquivos/alunos.txt"):
            with open("arquivos/alunos.txt", "r") as arquivo:
                for aluno in arquivo:
                    nome, _, dre = aluno.strip().split(",")
                    print(f"Nome: {nome}, DRE: {dre}")

    alunos = []
    while True:
        nome = input("Nome do aluno: ")
        dre = input("DRE do aluno: ")
        # verifica se o aluno existe no sistema
        aluno_existe = False
        if path.exists("arquivos/alunos.txt"):
            with open("arquivos/alunos.txt", "r") as arquivo:
                for linha in arquivo:
                    _, _, dre_cadastrado = linha.strip().split(",")
                    if dre_cadastrado == dre:
                        aluno_existe = True
                        break

        if not aluno_existe:
            print("Aluno não existe no sistema.")
            continue
        # adiciona o aluno na lista de alunos
        frequencia = 0
        notas = [0] * quantidade_avaliacoes
        alunos.append((nome, dre, frequencia, notas))

        adicionar_mais = input("Deseja adicionar mais um aluno (s/n)? ")
        if adicionar_mais.lower() != "s":
            break

    # salva a turma e os alunos no arquivo
    with open("arquivos/turmas.txt", "a") as turmas:
        if formas_avaliacao == "p":
            turma_info = f"{codigo_disciplina},{nome_disciplina},{codigo_turma},{ano_semestre},{horario},{formas_avaliacao},{quantidade_avaliacoes},{pesos}"
        else:
            turma_info = f"{codigo_disciplina},{nome_disciplina},{codigo_turma},{ano_semestre},{horario},{formas_avaliacao},{quantidade_avaliacoes}"

        alunos_info = ""
        for aluno in alunos:
            nome, dre, frequencia, notas = aluno
            notas_str = ",".join(map(str, notas))
            alunos_info += f",{nome},{dre},{frequencia},{notas_str}"

        turmas.write(f"{turma_info}{alunos_info}\n")

    print("Turma cadastrada com sucesso.")


def editar_turma():
    codigo_turma = input("Código da turma: ")
    if not turma_existe(codigo_turma):
        print("Turma não existe")
        return

    turmas = []
    turma_encontrada = None
    with open("arquivos/turmas.txt", "r") as arquivo:
        for linha in arquivo:
            campos = linha.strip().split(",")
            if campos[2] == codigo_turma:
                turma_encontrada = campos
            else:
                turmas.append(campos)

    escolha = input("Deseja ver as informações dessa turma: s/n ")
    if escolha == "s":
        print("Informações atuais da turma:")
        print(f"Código da Disciplina: {campos[0]}")
        print(f"Nome da Disciplina: {campos[1]}")
        print(f"Código da Turma: {campos[2]}")
        print(f"Ano e Semestre: {campos[3]}")
        print(f"Horário: {campos[4]}")
        print(f"Formas de Avaliação: {campos[5]}")
        print(f"Quantidade de Avaliações: {campos[6]}")
        if turma[5] == "p":
            pesos = turma[7].split(",")
            print(f"Pesos: {', '.join(pesos)}")
            aluno_start_index = 8
        else:
            aluno_start_index = 7
            num_avaliacoes = int(turma[6])
    # mostra os alunos
    print("Alunos:")
    index = aluno_start_index
    while index < len(turma):
        nome = campos[index]
        dre = campos[index + 1]
        frequencia = campos[index + 2]
        notas = campos[index + 3 : index + 3 + num_avaliacoes]
        print(
            f"Nome: {nome}, DRE: {dre}, Frequência: {frequencia}, Notas: {', '.join(notas)}"
        )
        index += 3 + num_avaliacoes
    # pede as novas informacoes
    codigo_disciplina = input("Código da disciplina: ")
    nome_disciplina = input("Nome da disciplina: ")
    ano_semestre = input("Ano e semestre: ")
    horario = input("Horário: ")
    formas_avaliacao = input("Formas de avaliação: a/p ")
    quantidade_avaliacoes = int(input("Quantas avaliações: "))
    if formas_avaliacao == "p":
        pesos = input("Digite os pesos separados por vírgula: ")
    alunos = turma[aluno_start_index:]

    # Exibir e permitir a modificação dos alunos
    num_alunos = len(alunos) // (
        quantidade_avaliacoes + 3
    )  # nome, dre, frequencia, notas
    for i in range(num_alunos):
        base_idx = i * (quantidade_avaliacoes + 3)
        nome = input(f"Nome do aluno [{alunos[base_idx]}]: ") or alunos[base_idx]
        dre = input(f"DRE do aluno [{alunos[base_idx + 1]}]: ") or alunos[base_idx + 1]
        frequencia = (
            input(f"Frequência [{alunos[base_idx + 2]}]: ") or alunos[base_idx + 2]
        )
        notas = []
        for j in range(quantidade_avaliacoes):
            nota = (
                input(f"Nota {j + 1} [{alunos[base_idx + 3 + j]}]: ")
                or alunos[base_idx + 3 + j]
            )
            notas.append(nota)

        alunos[base_idx] = nome
        alunos[base_idx + 1] = dre
        alunos[base_idx + 2] = frequencia
        for j in range(quantidade_avaliacoes):
            alunos[base_idx + 3 + j] = notas[j]

    turma = turma[:aluno_start_index] + alunos

    # Adicionar de volta a turma modificada na lista de turmas
    turmas.append(turma)

    with open("arquivos/turmas.txt", "w") as arquivo:
        for turma in turmas:
            linha = ",".join(turma)
            arquivo.write(f"{linha}\n")
    print("Turma modificada com sucesso.")


# funciona
def excluir_turma():
    turma_a_ser_removida = 0
    codigo_turma = input("Código da turma: ")
    if not turma_existe(codigo_turma):
        print("Turma não existe")
        return

    with open("arquivos/turmas.txt", "r") as arq, open(
        "arquivos/turmas_temp.txt", "w"
    ) as arq_temp:
        # seleciona a turma a ser removida
        for linha in arq:
            if linha.strip().split(",")[2] == codigo_turma:
                turma_a_ser_removida = linha
        print(turma_a_ser_removida)
        # passa as outras turmas para um novo arquivo
        arq.seek(0)
        for linha in arq:
            print(linha)
            if linha != turma_a_ser_removida:
                arq_temp.write(linha)

        replace("arquivos/turmas_temp.txt", "arquivos/turmas.txt")


def exibir_informacoes_turma():
    codigo_turma = input("Código da turma: ")
    if not turma_existe(codigo_turma):
        print("Turma não existe")
        return

    with open("arquivos/turmas.txt", "r") as turmas:
        for turma in turmas:
            if turma.strip().split(",")[2] == codigo_turma:
                quantidade_avaliacoes = int(turma.strip().split(",")[6])
                pesos = turma.strip().split(",")[
                    7 : 7 + int(turma.strip().split(",")[6])
                ]
                while True:
                    print("1. Ver as notas")
                    print("2. Ver as médias")
                    print("3. Ver a frequência")
                    print("4. Ver tudo")
                    escolha = input("O que quer fazer: ")
                    if escolha == "1":
                        if turma.strip().split(",")[5] == "a":
                            pass

                        else:
                            # carrega os alunos em uma lista
                            alunos = [
                                x
                                for x in turma.strip().split(",")[
                                    7 + int(turma.strip().split(",")[6]) :
                                ]
                            ]
                            # separa os alunos em sublistas
                            alunos_lista = [
                                alunos[i : i + 3 + int(turma.strip().split(",")[6])]
                                for i in range(
                                    0, len(alunos), 3 + int(turma.strip().split(",")[6])
                                )
                            ]
                            # printa os alunos e suas notas com os pesos
                            for aluno in alunos_lista:
                                print(f"Nome: {aluno[0]}, DRE: {aluno[1]}")
                                for i in range(int(quantidade_avaliacoes)):
                                    print(
                                        f"Nota {i + 1}: {aluno[3:][i]}, Peso {pesos[i]}"
                                    )

                    elif escolha == "2":
                        if turma.strip().split(",")[5] == "a":
                            pass
                        else:
                            # carrega os alunos em uma lista
                            alunos = [
                                x
                                for x in turma.strip().split(",")[
                                    7 + int(turma.strip().split(",")[6]) :
                                ]
                            ]
                            # separa os alunos em sublistas
                            alunos_lista = [
                                alunos[i : i + 3 + int(turma.strip().split(",")[6])]
                                for i in range(
                                    0, len(alunos), 3 + int(turma.strip().split(",")[6])
                                )
                            ]
                            # faz a media ponderada e printa
                            for aluno in alunos_lista:
                                soma = 0
                                for i in range(int(quantidade_avaliacoes)):
                                    soma += int(pesos[i]) * float(aluno[3:][i])
                                media = soma / sum([int(peso) for peso in pesos])
                                print(
                                    f"Nome: {aluno[0]}, DRE: {aluno[1]}, Média: {media}"
                                )
                    elif escolha == "3":
                        if turma.strip().split(",")[5] == "a":
                            pass
                        else:
                            # carrega os alunos em uma lista
                            alunos = [
                                x
                                for x in turma.strip().split(",")[
                                    7 + int(turma.strip().split(",")[6]) :
                                ]
                            ]
                            # separa os alunos em sublistas
                            alunos_lista = [
                                alunos[i : i + 3 + int(turma.strip().split(",")[6])]
                                for i in range(
                                    0, len(alunos), 3 + int(turma.strip().split(",")[6])
                                )
                            ]
                            for aluno in alunos_lista:
                                print(
                                    f"Nome: {aluno[0]}, DRE: {aluno[1]}, Frequência: {aluno[2]}%"
                                )
                    elif escolha == "4":
                        if turma.strip().split(",")[5] == "a":
                            pass
                        else:
                            # carrega os alunos em uma lista
                            alunos = [
                                x
                                for x in turma.strip().split(",")[
                                    7 + int(turma.strip().split(",")[6]) :
                                ]
                            ]
                            # separa os alunos em sublistas
                            alunos_lista = [
                                alunos[i : i + 3 + int(turma.strip().split(",")[6])]
                                for i in range(
                                    0, len(alunos), 3 + int(turma.strip().split(",")[6])
                                )
                            ]
                            # printa as info da turma e dos alunos
                            print(
                                "Código da disciplina: " + turma.strip().split(",")[0]
                            )
                            print("Nome da disciplina: " + turma.strip().split(",")[1])
                            print("Código da turma: " + turma.strip().split(",")[2])
                            print("Semestre: " + turma.strip().split(",")[3])
                            print("Horário: " + turma.strip().split(",")[4] + "h")
                            if turma.strip().split(",")[5] == "a":
                                print(f"Forma de avaliação: Média aritmética")
                            else:
                                print(f"Forma de avaliação: Média ponderada")
                            for aluno in alunos_lista:
                                soma = 0
                                print(
                                    f"Nome: {aluno[0]}, DRE: {aluno[1]}, Frequência: {aluno[2]}%"
                                )
                                for i in range(int(quantidade_avaliacoes)):
                                    print(
                                        f"Nota {i + 1}: {aluno[3:][i]}, Peso {pesos[i]}"
                                    )
                                    soma += int(pesos[i]) * float(aluno[3:][i])
                                media = soma / sum([int(peso) for peso in pesos])
                                print(f"Média: {media}")
                                print()
                    else:
                        print("Opção inválida!")


def calcular_estatisticas_turma():
    codigo_turma = input("Código da turma: ")
    if not turma_existe(codigo_turma):
        print("Turma não existe")
        return


def exibir_informacoes_aluno():
    codigo_turma = input("Código da turma: ")
    if not turma_existe(codigo_turma):
        print("Turma não existe")
        return
