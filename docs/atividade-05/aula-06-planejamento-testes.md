# Aula 6 – Planejamento e Execução de Testes

> Disciplina: Qualidade de Software  
> Projeto: LocalEats  
> Integrantes do grupo:  
> - Gabrieli Morales

---

# 1. Plano de Testes

## 1.1 Objetivo
Descreva o objetivo do plano de testes.

> Validar as principais funcionalidades do sistema LocalEats, garantindo que o fluxo de navegação, a busca de estabelecimentos e a visualização de detalhes ocorram sem comportamentos inesperados, assegurando a estabilidade da interface para o usuário final.

---

## 1.2 Escopo

### O que será testado
- Navegação inicial na Home
- Busca de restaurantes por nome ou categoria
- Visualização de detalhes do restaurante e de seus pratos/menus

### O que NÃO será testado
- Integração real com gateways de pagamento
- Envio de e-mails de confirmação e recuperação de senha
- Testes de carga, estresse e performance do servidor

---

## 1.3 Funcionalidades selecionadas
Liste as funcionalidades que serão foco dos testes:

- Login/Cadastro
- Busca de restaurantes
- Visualização de detalhes do restaurante e cardápio

---

## 1.4 Estratégia de Testes

Descreva como os testes serão realizados.

- Tipos de teste:
  - (x) Funcional
  - (x) Usabilidade
  - ( ) Outros: _______

- Abordagem:
  > Testes manuais (Caixa-Preta) baseados em cenários definidos previamente, focando na experiência do usuário e priorizando tanto os caminhos felizes (happy paths) quanto os cenários de exceção (erros).

---

## 1.5 Responsáveis

Defina os papéis na equipe:

| Nome | Responsabilidade |
|------|----------------|
|Gabrieli|Planeamento, especificação de casos de teste, execução e análise crítica dos resultados.|

---

# 2. Casos de Teste

Crie no mínimo 5 casos de teste.

---

## CT-01 – Cadastro de novo usuário

**Pré-condição:** Estar na página de Registro/Cadastro do sistema.

**Passos:**
1. Preencher o campo de Nome;
2. Preencher o campo de E-mail;
3. Preencher o campo de Senha;
4. Clicar no botão "Cadastrar".

**Dados de entrada (se aplicável):** Nome: "Usuario Teste", E-mail: "teste@localeats.com", Senha: "SenhaForte123"

**Resultado esperado:** O sistema deve processar o cadastro, exibir uma mensagem de sucesso na tela e redirecionar o usuário imediatamente para a página de Login.

---

## CT-02 – Login com credenciais inválidas

**Pré-condição:** Estar na página de Login do sistema.

**Passos:**  
1. Inserir um e-mail válido no campo de usuário.
2. Inserir uma senha incorreta no campo de senha.
3. Clicar no botão "Entrar".

**Dados de entrada (se aplicável):** E-mail: "teste@localeats.com", Senha: "senha_errada"

**Resultado esperado:** O sistema deve impedir o acesso, manter o usuário na página de login e exibir um alerta visual (em vermelho) com a mensagem: "E-mail ou senha incorretos".

---

## CT-03 – Busca de restaurante

**Pré-condição:** Estar na página inicial (Home) do LocalEats.

**Passos:** 
1. Clicar no campo de busca.
2. Digitar o termo de pesquisa.
3. Clicar no ícone de lupa ou pressionar a tecla Enter.

**Dados de entrada (se aplicável):** Termo: "Pizza"

**Resultado esperado:** O sistema deve processar a busca e listar na tela apenas os estabelecimentos relacionados ao termo "Pizza".

---

## CT-04 – Busca sem resultados

**Pré-condição:** Estar na página inicial (Home) do LocalEats.

**Passos:**  
1. Clicar no campo de busca.
2. Digitar um termo que não corresponda a nenhum restaurante cadastrado.
3. Clicar no ícone de lupa ou pressionar a tecla Enter.

**Dados de entrada (se aplicável):** Termo: "xyz123abc"

**Resultado esperado:** O sistema deve exibir claramente a mensagem de feedback: "Nenhum restaurante encontrado para a sua busca", orientando o usuário.

---

## CT-05 – Visualização de detalhes do restaurante

**Pré-condição:** Estar na página de resultados de busca com restaurantes listados na tela.

**Passos:**  
1. Identificar o card de um restaurante específico.
2. Clicar sobre o card do restaurante.

**Dados de entrada (se aplicável):** Nenhum.

**Resultado esperado:** O sistema deve redirecionar o usuário para a página específica do restaurante, exibindo corretamente suas informações de contato, o menu completo e os respectivos preços.

---

# 3. Execução dos Testes

Preencha a tabela com os resultados obtidos.

| ID     | Resultado (Passou/Falhou) | Evidência (descrição ou print) |
|--------|--------------------------|--------------------------------|
| CT-01  |Passou|O redirecionamento para o login foi efetuado após confirmação dos dados.|
| CT-02  |Passou|A mensagem de "Credenciais Inválidas" foi exibida na tela conforme o esperado.|
| CT-03  |Passou|Filtro funcionou corretamente retornando os itens pesquisados na interface.|
| CT-04  |Falhou|O sistema não mostrou mensagem de erro amigável, retornando apenas uma tela branca vazia (falta de empty state).|
| CT-05  |Passou|Página de detalhes carregou todos os itens do menu e preços sem quebra de layout.|

---

# 4. Análise dos Resultados

- Quantidade de testes executados: 5
- Quantidade de testes que passaram: 4
- Quantidade de testes que falharam: 1(CT-04)

## Principais problemas encontrados
- Ausência de Empty States (Estados Vazios) adequados durante as buscas. Quando nenhum resultado é encontrado, a aplicação deixa a tela em branco, o que prejudica a usabilidade e pode confundir o usuário fazendo-o pensar que o sistema travou.

---

# 5. Reflexão

Responda às questões abaixo:

- O plano de testes ajudou a organizar melhor o processo? Por quê?

Sim, o plano foi fundamental para guiar o foco da equipe. Ele permitiu que não apenas olhássemos para os cenários onde tudo dá certo, mas também estruturássemos os testes de falha proposital, garantindo uma cobertura metódica das funcionalidades principais.

- Algum problema só foi identificado durante a execução? Explique.

Sim, a falha de usabilidade na busca vazia (CT-04) só ficou evidente durante a execução prática. No planejamento, presumia-se que haveria um tratamento de erro padrão, mas a execução mostrou a ausência de feedback visual na interface.

- O que o grupo melhoraria no processo de testes?

Inserir testes específicos de responsividade em dispositivos móveis, uma vez que aplicações de delivery são amplamente utilizadas em celulares. Além disso, a documentação das evidências poderia ser enriquecida com prints reais das telas para facilitar a visualização dos bugs reportados.

---

## Conclusão

Descreva se o comportamento da funcionalidade foi considerado aceitável e por quê.

---

# 6. Conclusão Geral

Faça um resumo final:

- **Qualidade geral do sistema testado:** O sistema é funcional e estável em seus fluxos principais, mas apresenta falhas críticas de experiência do usuário (UX) em cenários de exceção.
- **Principais pontos positivos:** Navegação fluida, carregamento rápido de informações e interface intuitiva para o "caminho feliz".
- **Principais problemas identificados:** Falta de feedback visual (Empty States) em buscas sem resultado, o que pode levar à confusão do usuário.
- **Impressão geral do grupo sobre o processo de testes:** A abordagem individual permitiu uma visão técnica completa do ciclo de QA, evidenciando que a qualidade vai além do simples funcionamento, dependendo diretamente da clareza das respostas do sistema ao usuário.