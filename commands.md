Aqui está uma lista de comandos Git comuns e o que cada um faz:

### **Comandos de Configuração**

1. **`git config --global user.name "Seu Nome"`**  
   Configura o nome de usuário global para todos os repositórios Git no seu sistema.

2. **`git config --global user.email "seuemail@example.com"`**  
   Configura o email global para todos os repositórios Git no seu sistema.

3. **`git config --list`**  
   Exibe as configurações atuais do Git.

---

### **Comandos de Repositório**

4. **`git init`**  
   Inicializa um novo repositório Git no diretório atual.

5. **`git clone <url_do_repositorio>`**  
   Clona um repositório remoto para o seu diretório local.

6. **`git status`**  
   Exibe o status atual do repositório, mostrando arquivos modificados, adicionados ou não rastreados.

7. **`git remote add origin <url_do_repositorio>`**  
   Adiciona um repositório remoto com o nome "origin" e o URL fornecido.

8. **`git remote -v`**  
   Exibe os repositórios remotos configurados no repositório atual.

---

### **Comandos de Branch**

9. **`git branch`**  
   Lista todas as branches no repositório local. A branch atual estará marcada com um asterisco.

10. **`git branch <nome_da_branch>`**  
    Cria uma nova branch com o nome fornecido.

11. **`git checkout <nome_da_branch>`**  
    Muda para a branch especificada.

12. **`git checkout -b <nome_da_branch>`**  
    Cria uma nova branch e muda para ela imediatamente.

13. **`git merge <nome_da_branch>`**  
    Mescla a branch especificada na branch atual.

14. **`git branch -d <nome_da_branch>`**  
    Deleta a branch especificada, desde que ela já tenha sido mesclada.

---

### **Comandos de Commit**

15. **`git add <arquivo>`**  
    Adiciona um arquivo específico ao "staging" para ser comitado.

16. **`git add .`**  
    Adiciona todos os arquivos modificados ou novos ao "staging".

17. **`git commit -m "mensagem"`**  
    Faz um commit das mudanças que foram adicionadas ao "staging" com a mensagem fornecida.

18. **`git commit --amend`**  
    Altera o último commit. Você pode modificar a mensagem ou adicionar novos arquivos ao commit anterior.

---

### **Comandos de Histórico**

19. **`git log`**  
    Exibe o histórico de commits da branch atual.

20. **`git log --oneline`**  
    Exibe o histórico de commits de forma compacta, com uma linha por commit.

21. **`git show <hash_do_commit>`**  
    Exibe detalhes de um commit específico.

---

### **Comandos de Remoto**

22. **`git push`**  
    Envia os commits locais para o repositório remoto.

23. **`git push origin <nome_da_branch>`**  
    Envia os commits da branch especificada para o repositório remoto.

24. **`git pull`**  
    Baixa as alterações do repositório remoto e as mescla na branch local.

25. **`git fetch`**  
    Baixa as alterações do repositório remoto, mas não as mescla automaticamente.

26. **`git push origin --delete <nome_da_branch>`**  
    Deleta uma branch no repositório remoto.

---

### **Comandos de Revertendo Mudanças**

27. **`git reset --hard`**  
    Desfaz todas as alterações no repositório local, retornando ao último commit.

28. **`git reset --soft <commit>`**  
    Faz o "reset" para o commit especificado, mas mantém as alterações no "staging".

29. **`git revert <commit>`**  
    Cria um novo commit que desfaz as mudanças feitas pelo commit especificado.

---

### **Comandos de Trabalho com Arquivos**

30. **`git rm <arquivo>`**  
    Remove um arquivo do repositório e o marca para exclusão no próximo commit.

31. **`git mv <arquivo_origem> <arquivo_destino>`**  
    Move ou renomeia um arquivo no repositório.

32. **`git clean -f`**  
    Remove arquivos não rastreados do diretório de trabalho.

---

### **Comandos de Colaboração**

33. **`git pull origin <nome_da_branch>`**  
    Baixa as mudanças do repositório remoto para a branch especificada e as mescla automaticamente.

34. **`git fetch origin`**  
    Baixa as mudanças do repositório remoto sem mesclar automaticamente.

35. **`git stash`**  
    Salva temporariamente as alterações locais não commitadas para que você possa trabalhar em outra coisa sem perder seu progresso.

36. **`git stash pop`**  
    Restaura as alterações salvas com o último `git stash`.
