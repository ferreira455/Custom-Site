import subprocess

def git_commit_and_push(message):
    try:
        # Adicionar arquivos ao staging
        subprocess.run(["git", "add", "."], check=True)
        print("Arquivos adicionados ao staging.")

        # Criar o commit com a mensagem
        subprocess.run(["git", "commit", "-m", message], check=True)
        print(f"Commit criado com a mensagem: '{message}'")

        # Enviar para o branch remoto
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Alterações enviadas para o repositório remoto.")
    
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar um comando: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    commit_message = input("Digite a mensagem do commit: ")
    git_commit_and_push(commit_message)
