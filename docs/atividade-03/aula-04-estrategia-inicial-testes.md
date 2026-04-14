# Estratégia Inicial de Testes – LocalEats

## 1. Funcionalidades
- Login e Cadastro
- Busca de restaurantes (por culinária, local e preço)
- Visualização de detalhes (cardápios, fotos e avaliações)
- Publicação de avaliações e experiências
- Sistema de recomendações personalizadas
- Favoritar locais

---

## 2. Níveis de Teste

### Funcionalidade: Busca de restaurantes
- Unitário: validar a lógica dos filtros de busca isoladamente (ex: checar se o filtro de preço funciona).
- Integração: verificar a comunicação entre a interface de busca e a API de consulta ao banco de dados.
- Sistema: validar o fluxo completo de busca nas versões web e mobile, garantindo que os resultados não apresentem inconsistências entre si.
- Aceitação: o usuário consegue encontrar rapidamente um restaurante usando os critérios desejados e sem resultados incorretos?

### Funcionalidade: Visualização de detalhes
- Unitário: validar o cálculo matemático da média das notas do restaurante.
- Integração: verificar a conexão com o serviço que armazena e carrega as imagens e cardápios.
- Sistema: testar o tempo de resposta do carregamento das fotos simulando acesso em massa para mapear a lentidão relatada.
- Aceitação: o usuário considera a visualização das informações clara e a tela intuitiva?

### Funcionalidade: Publicação de avaliações
- Unitário: validar se os campos de texto e nota não aceitam caracteres inválidos.
- Integração: verificar se a avaliação enviada pelo app é gravada e persistida corretamente no banco de dados.
- Sistema: validar o ciclo de vida da avaliação, garantindo que ela não desapareça do sistema após atualizações.
- Aceitação: o usuário consegue compartilhar sua experiência de forma simples e registrar sua nota sem dificuldade?

### Funcionalidade: Favoritar locais
- Unitário: validar as funções internas de adicionar e remover IDs da lista de favoritos.
- Integração: verificar a sincronização da lista local de favoritos do usuário com a nuvem/servidor.
- Sistema: testar se um local favoritado no app mobile reflete instantaneamente na versão web.
- Aceitação: o usuário consegue acessar seus locais favoritos facilmente e concluir a ação sem falhas?

---

## 3. Prioridades e Riscos

Alta prioridade:
- Busca de restaurantes e Publicação/Visualização de avaliações.

Justificativa:
O negócio da plataforma é conectar clientes a restaurantes. Falhas na busca (resultados incorretos) impedem o usuário de usar a ferramenta. Além disso, avaliações que somem após atualizações geram perda de confiança e afetam diretamente a reputação do app perante a associação de comerciantes, exigindo ação imediata.

Baixa prioridade: 
- Favoritar locais e Sistema de recomendações.

Justificativa:
Embora melhorem a experiência do usuário, falhas nessas áreas não impedem o fluxo principal do sistema (encontrar um lugar e ver informações). Como o prazo é curto e há problemas graves em produção, essas funcionalidades podem ser testadas e ajustadas em um segundo momento.

---

## 4. Pirâmide de Testes

- Maior foco: Testes Unitários.
- Médio foco: Testes de Integração.
- Menor foco: Testes de Sistema e de Aceitação (UI/E2E).

Justificativa:
Com base na eficiência e no custo, testes unitários e de integração são executados mais rapidamente e são mais fáceis de manter, permitindo corrigir bugs nas lógicas de busca e desaparecimento de avaliações com agilidade. Como as telas atuais foram relatadas como "confusas e pouco intuitivas", automatizar muitos testes de sistema agora geraria alto custo de refatoração no futuro. O topo da pirâmide deve focar apenas nos fluxos críticos.

---

## 5. Testes em Produção

- Uso de: Monitoramento de performance (APM), observabilidade de logs e Testes A/B (ou Canary Releases).
- Aplicar em: Investigação da lentidão em horários de pico, mapeamento de falhas em determinados smartphones e validação de melhorias nas telas confusas.

Justificativa:
Como a aplicação já está no ar e apresenta problemas graves no mundo real, é quase impossível simular em laboratório a fragmentação de smartphones dos usuários e o volume de tráfego imprevisível do evento gastronômico. O uso de testes em produção permite capturar métricas reais e lançar melhorias de interface para pequenos grupos de usuários (Teste A/B) de forma segura antes de impactar toda a base.