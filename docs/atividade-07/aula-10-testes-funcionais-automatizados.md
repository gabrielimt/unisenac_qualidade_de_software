# 🧩 Atividade PBL – Aula 10  
## Testes Funcionais Automatizados – LocalEats

---

## 👥 Integrante(s)
- Gabrieli Morales Taborda

---

## 🔹 1. Fluxo funcional escolhido

### 📌 Fluxo:
Login de usuário

🔎 **Descrição**  
Permite autenticar um usuário no sistema.

🎯 **Importância**  
Fluxo essencial para acesso às funcionalidades.

---

## 🔹 2. Teste com Codegen

### 💻 Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### 🔗 Link para o código gerado

👉 https://github.com/gabrielimt/unisenac_qualidade_de_software/docs/atividade-07/tests/codegen_login.py

### 🧠 Observações

- O Codegen ajudou a iniciar rapidamente o teste  
- O código gerado é verboso  
- Foi necessário refatorar

---

## 🔹 3. Teste automatizado com Pytest

### 🔗 Link para o teste

👉 https://github.com/gabrielimt/unisenac_qualidade_de_software/docs/atividade-07/tests/test_login.py

### 📌 O que o teste faz?

- Acessa o sistema  
- Realiza login  
- Valida mensagem de sucesso

---

## 🔹 4. Refatoração com Page Object Model (POM)

### 🔗 Link para Page Object

👉 https://github.com/gabrielimt/unisenac_qualidade_de_software/docs/atividade-07/tests/login_page.py

### 🔗 Link para teste refatorado

👉 https://github.com/gabrielimt/unisenac_qualidade_de_software/docs/atividade-07/tests/test_login.py

### 🧠 Melhorias realizadas

- Separação entre teste e lógica de UI  
- Código mais organizado  
- Maior reutilização  

---

## 🔹 5. Execução dos testes

### ▶️ Comando

```bash
python -m pytest tests/test_login.py -v
```

### 📊 Resultado

- Total de testes: 1  
- Testes passaram: 1  
- Testes falharam: 0  

### 📸 Evidência

![Evidência de Sucesso do Teste]([https://github.com/gabrielimt/unisenac_qualidade_de_software/blob/main/docs/atividade-07/image7.png])

---

## 🔹 6. Análise crítica

- O teste quebrou ao alterar textos da interface  
- Seletores por texto são frágeis  
- Teste precisa de melhorias para ser mais robusto

---

## 🔹 7. Reflexão

- Testes automatizados não substituem testes manuais  
- Devem focar em fluxos críticos  
- Aumentam a confiança no sistema  

---

## 💡 Conclusão

A automação de testes melhora a qualidade, mas exige boas práticas para manutenção.