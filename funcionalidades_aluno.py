from funcionalidades_professor import carrega_alunos


def ver_notas(dre):
    with open("arquivos/turmas.txt", "r") as turmas:
        for turma in turmas:
            turma = turma.strip().split(",")
            forma_avaliacao = turma[5]
            quantidade_avaliacoes = int(turma[6])
            alunos = carrega_alunos(turma, forma_avaliacao)
            for aluno in alunos:
                if dre in aluno:
                    print(f"Código da disciplina: {turma[0]}")
                    print(f"Nome da disciplina: {turma[1]}")
                    print(f"Código da turma: {turma[2]}")
                    print(f"Nome: {aluno[0]}, DRE: {aluno[1]}")
                    for i in range(quantidade_avaliacoes):
                        nota = aluno[3:][i]
                        print(f"Nota {i + 1}: {nota}")


def ver_frequencia(dre):
    with open("arquivos/turmas.txt", "r") as turmas:
        for turma in turmas:
            turma = turma.strip().split(",")
            forma_avaliacao = turma[5]
            alunos = carrega_alunos(turma, forma_avaliacao)
            for aluno in alunos:
                if dre in aluno:
                    print(f"Código da disciplina: {turma[0]}")
                    print(f"Nome da disciplina: {turma[1]}")
                    print(f"Código da turma: {turma[2]}")
                    print(f"Nome: {aluno[0]}, DRE: {aluno[1]}, Frequência: {aluno[2]}%")


def ver_medias(dre):
    with open("arquivos/turmas.txt", "r") as turmas:
        for turma in turmas:
            turma = turma.strip().split(",")
            forma_avaliacao = turma[5]
            quantidade_avaliacoes = int(turma[6])
            pesos = None
            if forma_avaliacao == "p":
                pesos = list(map(int, turma[7 : 7 + quantidade_avaliacoes]))
            alunos = carrega_alunos(turma, forma_avaliacao)
            for aluno in alunos:
                if dre in aluno:
                    print(f"Código da disciplina: {turma[0]}")
                    print(f"Nome da disciplina: {turma[1]}")
                    print(f"Código da turma: {turma[2]}")
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
                    print(f"Nome: {aluno[0]}, DRE: {aluno[1]}, Média: {media}")


def calcular_quanto_falta_para_aprovacao(dre):
    pass
