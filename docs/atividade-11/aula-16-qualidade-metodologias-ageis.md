# Aula 16 – Qualidade em Metodologias Ágeis

## Integrantes

- Gabrieli Morales Taborda

---

# 1. Análise de Práticas Ágeis no Processo

| Prática | Existe no processo? | Como é aplicada atualmente? | Pode ser melhorada? |
|----------|----------|----------|----------|
| Planejamento iterativo | Sim | O desenvolvimento é guiado por atividades graduais para implementar e testar funcionalidades. | Pode melhorar com a introdução de retrospectivas focadas na análise de defeitos encontrados. |
| Priorização de funcionalidades | Sim | Baseia-se no valor de negócio e fluxos críticos, como busca de restaurantes e login. | Pode adotar uma matriz de risco vs. impacto para priorizar a automação de testes. |
| Entregas incrementais | Sim | Funcionalidades e testes E2E são construídos em partes progressivas. | Pode melhorar com pipelines de Integração Contínua (CI) para validar entregas automaticamente. |
| Feedback frequente | Parcial | Ocorre principalmente através de avaliações após a conclusão dos testes E2E. | Pode se beneficiar de revisões de código (Code Review) diárias para evitar débito técnico. |
| Trabalho colaborativo | Sim | O uso de BDD (Gherkin) tem sido essencial para alinhar as regras de negócio com os testes. | Adoção da prática "Three Amigos" (Negócio, Dev, QA) durante o refinamento das tarefas. |
| Controle visual das atividades | Parcial | Acompanhamento padrão das tarefas do projeto. | Mapeamento explícito de colunas de Qualidade (ex: "Em Teste", "Pronto para Homologação") no Kanban. |
| Melhoria contínua | Sim | Há evolução visível, como a refatoração de seletores frágeis para o padrão Page Object Model. | Pode incluir a medição de métricas de qualidade, como a taxa de testes que falham por quebras de interface. |

### Conclusão

O processo de desenvolvimento do LocalEats possui uma base ágil promissora, destacando-se na entrega incremental e no forte foco em qualidade, comprovado pela adoção de testes automatizados e BDD. Como ponto forte, a equipe consegue transformar regras de negócio abstratas em validações práticas. Para melhorar, é necessário adotar práticas mais maduras de controle e feedback, como o Kanban para evidenciar gargalos de teste e CI/CD para evitar que a agilidade comprometa a estabilidade do sistema ao longo do tempo.

---

# 2. Propostas de Melhoria Ágil

| Melhoria Proposta | Metodologia Relacionada | Benefício Esperado |
|------------------|------------------------|--------------------|
| Utilizar um quadro Kanban com raias (swimlanes) específicas para "QA/Testes" | Kanban | Maior visibilidade do andamento das atividades e clareza sobre gargalos de qualidade[cite: 39]. |
| Implementar Integração Contínua (CI) para execução automática da suíte Pytest | XP (Extreme Programming) | Feedback imediato caso uma nova alteração quebre fluxos já automatizados e validados. |
| Adotar a prática de "Three Amigos" no refinamento de requisitos | Lean / Scrum | Alinhamento total sobre o comportamento esperado antes do código ser feito, evitando retrabalho. |
| Revisão de Código (Code Review) focada em padrões de projeto (ex: POM) | XP (Extreme Programming) | Eleva a qualidade técnica, garante manutenibilidade do código e distribui o conhecimento do sistema. |

---

# 3. Definition of Ready (DoR)

Uma funcionalidade estará pronta para desenvolvimento quando:

1. O requisito possui critérios de aceitação definidos e claros, preferencialmente no formato Gherkin (Given-When-Then)[cite: 44].
2. O fluxo principal, fluxos alternativos e tratamentos de erro foram discutidos e mapeados.
3. Quaisquer dependências de interface (protótipos de tela) ou serviços externos estão resolvidos ou acessíveis.
4. Os identificadores de automação (como `data-testid`) necessários para os testes E2E foram combinados com o desenvolvimento.
5. A tarefa foi compreendida tecnicamente e seu esforço foi estimado de forma colaborativa.

---

# 4. Definition of Done (DoD)

Uma funcionalidade será considerada concluída quando:

1. O código foi implementado, revisado e segue os padrões arquiteturais do projeto (ex: separação de responsabilidades).
2. Os critérios de aceitação da funcionalidade foram atendidos e validados com sucesso[cite: 49].
3. Os testes automatizados (unitários e ponta a ponta com Playwright) foram escritos e integrados à suíte.
4. A execução completa da suíte de testes passa sem nenhuma falha técnica ou regressão (zero quebras de interface).
5. A funcionalidade foi integrada à branch principal e está pronta para uso sem apresentar defeitos críticos no fluxo feliz.