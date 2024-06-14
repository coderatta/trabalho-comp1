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
    pass


def ver_frequencia(dre):
    pass


def ver_medias(dre):
    pass


def calcular_quanto_falta_para_aprovacao(dre):
    pass
