from os import path, makedirs
from hashlib import sha256


def cadastrar_professor():
    try:
        # verifica se a pasta com os arquivos existe
        if not path.exists("arquivos"):
            makedirs("arquivos")

        with open("arquivos/professores.txt", "a+") as arquivo:
            nome = input("Nome do professor: ")
            senha = input("Senha: ")
            senha_hash = sha256(senha.encode()).hexdigest()
            # verifica se o professor ja tem cadastro
            arquivo.seek(0)
            for linha in arquivo:
                registro_nome, _ = linha.strip().split(",")
                if registro_nome == nome:
                    print("Professor já cadastrado.")
                    return

            professor = f"{nome},{senha_hash}\n"
            arquivo.write(professor)
            print("Professor cadastrado com sucesso.")
    except FileNotFoundError:
        print("Arquivo de professores não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


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
                    return True

        print("Nome ou senha incorretos.")
        return False
    except FileNotFoundError:
        print("Arquivo de professores não encontrado.")
        return False
    except Exception as e:
        print(f"Erro: {e}")
        return False


# so o professor que pode cadastrar alunos em uma turma
def cadastrar_aluno():
    try:
        # verifica se a pasta com os arquivos existe
        if not path.exists("arquivos"):
            makedirs("arquivos")

        with open("arquivos/alunos.txt", "a+") as arquivo:
            nome = input("Nome do aluno: ")
            senha = input("Senha do aluno: ")
            senha_hash = sha256(senha.encode()).hexdigest()
            dre = input("DRE do aluno: ")
            # verifica se o aluno ja tem cadastro
            arquivo.seek(0)
            for linha in arquivo:
                _, _, dre_cadastrado = linha.strip().split(",")
                if dre_cadastrado == dre:
                    print("Aluno já cadastrado.")
                    return

            aluno = f"{nome},{senha_hash},{dre}\n"
            arquivo.write(aluno)
        print("Aluno cadastrado com sucesso.")
    except FileNotFoundError:
        print("Arquivo de alunos não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")


def autenticar_aluno():
    try:
        dre = input("DRE: ")
        senha = input("Senha: ")
        senha_hash = sha256(senha.encode()).hexdigest()

        with open("arquivos/alunos.txt", "r") as arquivo:
            for linha in arquivo:
                _, registro_senha_hash, registro_dre = linha.strip().split(",")

                if registro_senha_hash == senha_hash and registro_dre == dre:
                    print("Autenticação bem-sucedida.")
                    return True

        print("DRE ou senha incorretos.")
        return False
    except FileNotFoundError:
        print("Arquivo de alunos não encontrado.")
        return False
    except Exception as e:
        print(f"Erro: {e}")
        return False
