from os import path, makedirs
from hashlib import sha256


def cadastrar_professor():
    try:
        # verifica se a pasta com os arquivos existe
        if not path.exists("arquivos"):
            makedirs("arquivos")

        with open("arquivos/professores.txt", "a+") as arquivo:
            nome = input("Nome do professor: ")
            senha = input("Senha do professor: ")
            senha_hash = sha256(senha.encode()).hexdigest()
            # verifica se o professor ja tem cadastro
            arquivo.seek(0)
            for linha in arquivo:
                nome_cadastrado = linha.strip().split(",")[0]
                if nome_cadastrado == nome:
                    print("Professor já cadastrado.")
                    return
            # salva o aluno formatado
            professor = f"{nome},{senha_hash}\n"
            arquivo.write(professor)
            print("Professor cadastrado com sucesso.")

    except FileNotFoundError:
        print("Arquivo de professores não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def autenticar_professor():
    try:
        nome = input("Nome: ")
        senha = input("Senha: ")
        senha_hash = sha256(senha.encode()).hexdigest()

        with open("arquivos/professores.txt", "r") as arquivo:
            for linha in arquivo:
                nome_cadastrado, senha_hash_cadastrada = linha.strip().split(",")
                if nome_cadastrado == nome and senha_hash_cadastrada == senha_hash:
                    print("Autenticação bem-sucedida.")
                    return True, nome

        print("Nome ou senha incorretos.")
        return False, ""
    except FileNotFoundError:
        print("Arquivo de professores não encontrado.")
        return False, ""
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False, ""


def cadastrar_aluno():
    posicao_dre = 1
    try:
        # verifica se a pasta com os arquivos existe
        if not path.exists("arquivos"):
            makedirs("arquivos")

        with open("arquivos/alunos.txt", "a+") as arquivo:
            nome = input("Nome do aluno: ")
            dre = input("DRE do aluno: ")
            # verifica se o aluno ja tem cadastro
            arquivo.seek(0)
            for linha in arquivo:
                dre_cadastrado = linha.strip().split(",")[posicao_dre]
                if dre_cadastrado == dre:
                    print("Aluno já cadastrado.")
                    return
            # salva o aluno formatado
            aluno = f"{nome},{dre}\n"
            arquivo.write(aluno)
            print("Aluno cadastrado com sucesso.")

    except FileNotFoundError:
        print("Arquivo de alunos não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def autenticar_aluno():
    posicao_dre = 1
    try:
        dre = input("DRE: ")

        with open("arquivos/alunos.txt", "r") as arquivo:
            for linha in arquivo:
                dre_cadastrado = linha.strip().split(",")[posicao_dre]
                if dre_cadastrado == dre:
                    print("Autenticação bem-sucedida.")
                    return True, dre
        print("DRE ou senha incorretos.")
        return False, 0

    except FileNotFoundError:
        print("Arquivo de alunos não encontrado.")
        return False, 0
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False, 0
