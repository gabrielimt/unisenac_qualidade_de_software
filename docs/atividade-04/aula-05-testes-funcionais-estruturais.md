# 🧪 Aula 5 – Testes Funcionais vs Estruturais  
## LocalEats

---

## 👥 Integrantes do Grupo
- Gabrieli Morales Taborda 

---

## 🎯 1. Funcionalidade escolhida

**Funcionalidade selecionada:**  
Busca de restaurantes

**Descrição da funcionalidade:**  
A funcionalidade permite que o usuário pesquise estabelecimentos utilizando termos de busca (nome ou tipo de comida) e aplique filtros como distância e categoria para refinar os resultados.

**O que o usuário espera:**  
O usuário espera encontrar rapidamente os restaurantes que correspondem exatamente aos termos e filtros aplicados, com resultados precisos e atualizados.

---

## 🔍 2. Testes Caixa-Preta (Visão do Usuário)

**Quais testes vocês fariam sem conhecer o código?**

### 🔹 Cenários de teste

- Cenário 1: (Busca Simples)
Inserir um nome de restaurante existente e verificar se ele aparece no topo da lista.

- Cenário 2: (Filtro Combinado)
Selecionar a categoria "Japonesa" e o filtro "Menos de 2km" para validar se apenas locais próximos e do tipo correto são exibidos.

- Cenário 3: (Busca Vazia)
Clicar no botão de busca sem digitar nada para verificar se o sistema exibe todos os restaurantes ou solicita um termo.

- Cenário 4: (Termos Inexistentes)
Buscar por uma palavra aleatória e validar se a mensagem "Nenhum resultado encontrado" é exibida corretamente.

---

### 🔹 Possíveis erros identificados

-  Resultados que não condizem com o termo pesquisado
-  Falha ao carregar a lista de resultados em conexões lentas
-  Inconsistência onde um restaurante favorito não aparece na busca geral

---

## 🔧 3. Testes Caixa-Branca (Visão do Sistema)

**Como essa funcionalidade poderia estar implementada internamente?**

### 🔹 Lógica hipotética (pseudo-código ou descrição)

```
Se (campoBusca não estiver vazio) {
    lista = BancoDeDados.buscar(termo);
    Se (filtrosAtivos == verdadeiro) {
        lista = lista.filtrarPorDistancia(raioUsuario);
        lista = lista.filtrarPorCategoria(categoriaSelecionada);
    }
    Retornar lista;
} Senão {
    Retornar erro("Campo obrigatório");
}
```

### 🔹 Situações a serem testadas

- Situação 1: O comportamento da função de cálculo de distância quando o GPS do usuário retorna um valor nulo (null) ou indefinido.
- Situação 2: Garantir que o loop de filtragem não entre em processamento infinito caso o banco de dados retorne milhares de registros de uma vez.
- Situação 3: Testar a prioridade dos filtros: se o filtro de distância deve ser processado antes ou depois do filtro de categoria no código.

### 🔹 Possíveis erros identificados

- Erro de arredondamento no cálculo matemático da distância, fazendo com que restaurantes "perto" sejam excluídos da lista.
- Variáveis de filtro que não são "limpas" entre uma busca e outra, acumulando critérios da pesquisa anterior.
- Falha na conexão com a API de mapas que impede o cálculo da rota interna.

## ⚖️ 4. Comparação entre as abordagens

Qual a principal diferença entre testar sem ver o código e com acesso ao código?

A principal diferença é o foco do olhar: na Caixa-Preta, o foco é o contrato entre o usuário e a interface (se eu peço X, recebo Y?). Na Caixa-Branca, o foco é a engrenagem (como os dados fluem, quais caminhos lógicos são percorridos e se há falhas de segurança ou performance escondidas).

Que tipo de problema cada abordagem ajuda a encontrar?

Caixa-preta:
Erros de usabilidade, requisitos não atendidos, problemas de design, falhas na jornada do usuário e mensagens de erro confusas na tela.

Caixa-branca:
Erros de lógica (ifs/elses mal estruturados), vazamento de memória, códigos que nunca são executados, vulnerabilidades de segurança e lentidão no processamento de dados.

## 💡 5. Reflexão no contexto do LocalEats

Qual abordagem parece mais importante neste momento do projeto?

Dado que o LocalEats apresenta "resultados incorretos nas buscas" e "inconsistências entre funcionalidades", a abordagem Caixa-Branca é a mais urgente. Problemas de lógica de busca geralmente não são apenas visuais; eles residem em como o código filtra e ordena os dados. Sem abrir a "caixa" e testar a lógica dos filtros, dificilmente a equipe entenderá por que o resultado X aparece quando deveria aparecer Y.

Apenas uma abordagem seria suficiente? Por quê?

Não. Se usarmos apenas Caixa-Branca, podemos ter um código tecnicamente perfeito que o usuário não sabe usar. Se usarmos apenas Caixa-Preta, podemos corrigir o sintoma de um erro agora, mas deixar uma falha estrutural que causará problemas maiores conforme o sistema cresce (como lentidão extrema ao atingir 1.000 usuários). As duas abordagens são as "duas faces da mesma moeda" da qualidade.

## 🚀 Conclusão

Eu entendi que para garantir a qualidade do LocalEats, devo agir tanto como uma usuária exigente quanto como uma desenvolvedora atenta. A visão de Caixa-Preta me ajuda a validar o valor do produto, enquanto a Caixa-Branca me dá a segurança de que o sistema é robusto e confiável por dentro.