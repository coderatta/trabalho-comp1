from autenticacao import *
from funcionalidades_aluno import *
from funcionalidades_professor import *


def main():
    while True:
        print("1. Login como Professor")
        print("2. Login como Aluno")
        print("3. Cadastrar Professor")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            autenticado, nome = autenticar_professor()
            if autenticado:
                while True:
                    print("1. Cadastrar turma")
                    print("2. Editar turma")
                    print("3. Excluir turma")
                    print("4. Cadastrar aluno")
                    print("5. Exibir informações de uma turma")
                    print("6. Calcular estatísticas de uma turma")
                    print("7. Exibir informações de um aluno")
                    print("8. Logout")
                    print("9. Sair")
                    escolha = input("Escolha uma opção: ")

                    if escolha == "1":
                        cadastrar_turma(nome)
                    elif escolha == "2":
                        editar_turma(nome)
                    elif escolha == "3":
                        excluir_turma(nome)
                    elif escolha == "4":
                        cadastrar_aluno()
                    elif escolha == "5":
                        exibir_informacoes_turma()
                    elif escolha == "6":
                        calcular_estatisticas_turma()
                    elif escolha == "7":
                        exibir_informacoes_aluno()
                    elif escolha == "8":
                        break
                    elif escolha == "9":
                        exit()
                    else:
                        print("Opção inválida!")

        elif escolha == "2":
            autenticado, dre = autenticar_aluno()
            if autenticado:
                while True:
                    print("1. Ver notas")
                    print("2. Ver médias")
                    print("3. Ver frequência")
                    print("4. Calcular pontos necessários para aprovação")
                    print("5. Logout")
                    print("6. Sair")
                    escolha = input("Escolha uma opcao: ")

                    if escolha == "1":
                        ver_notas(dre)
                    elif escolha == "2":
                        ver_medias(dre)
                    elif escolha == "3":
                        ver_frequencia(dre)
                    elif escolha == "4":
                        calcular_quanto_falta_para_aprovacao(dre)
                    elif escolha == "5":
                        break
                    elif escolha == "6":
                        exit()
                    else:
                        print("Opção inválida!")

        elif escolha == "3":
            cadastrar_professor()
        elif escolha == "4":
            break
        else:
            print("Opção inválida!")

    print("Fim do programa")


if __name__ == "__main__":
    main()
