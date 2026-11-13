# Guia de leitura

Texto para ler, não para ouvir: o mesmo conteúdo das dez seções em forma de tabelas, regras de decisão e um glossário português–inglês. A prova é em inglês, então os termos aparecem nas duas línguas.

## A prova

| Item | Valor |
|---|---|
| Formato | Online, com fiscal remoto pela câmera |
| Duração | 2 horas |
| Aprovação | 65% |
| Idioma | Inglês |

| Domínio | Peso | Seções do curso |
|---|---|---|
| Performing an Audit | 35% | 2, 3, 4 e 5 |
| IT Environment and Components | 25% | 6, 7 e 8 |
| Specific Audit Subjects | 15% | 9 |
| Overview of Newer Technologies | 12% | 10 |
| Controls, Risk and Audit | 8% | 1 |
| Audit Function | 5% | 1 |

**Como a prova pensa.** Quase toda questão de cenário pede "a melhor" ou "a primeira" ação. Três regras resolvem a maioria: o risco decide a prioridade; o auditor recomenda, mas não implanta; o que não se resolve com o auditado sobe ao comitê de auditoria.

## 1. A função de auditoria, controles e riscos

### Documentos e papéis

| Documento | Cobre | Aprovado por |
|---|---|---|
| Carta de auditoria (audit charter) | Toda a função: responsabilidade, autoridade, prestação de contas | Conselho e comitê de auditoria |
| Carta de contratação (engagement letter) | Um trabalho: objetivo, escopo, cronograma, relatórios | Acordada com o contratante |

- **Independência organizacional**: a auditoria reporta ao comitê de auditoria, não à área auditada.
- **Independência profissional**: o auditor não audita o que ajudou a implantar. Conflito se comunica antes de seguir.
- **Três linhas (IIA)**: gestão operacional; risco e conformidade; auditoria interna.
- **ISACA**: normas (standards, obrigatórias: gerais, de execução, de relatório) → diretrizes (guidelines) → ferramentas e técnicas (tools and techniques). Tudo dentro do ITAF.
- **Ética**: objetividade, cuidado profissional, sigilo (salvo exigência legal), só aceitar trabalho para o qual há competência, informar fatos relevantes.

### Controles

| Tipo | Faz | Exemplos |
|---|---|---|
| Preventivo (preventive) | Impede | Segregação de funções, controle de acesso, validação de entrada |
| Detectivo (detective) | Percebe e avisa | Revisão de logs, totais de controle, relatório de exceções |
| Corretivo (corrective) | Reduz o impacto e conserta | Backup, plano de recuperação de desastres |

- **Controles gerais de TI (IT general controls)** valem para todo o ambiente; **controles de aplicação (application controls)** ficam num sistema. Gerais fracos derrubam a confiança nos de aplicação.
- **Compensatório (compensating control)**: reduz o mesmo risco por outro caminho. Procure antes de relatar uma fraqueza.
- **Segurança razoável (reasonable assurance)**: nenhum controle dá certeza absoluta.

### Risco de auditoria (audit risk)

| Componente | O que é | Quem controla |
|---|---|---|
| Inerente (inherent risk) | Risco do processo sem controles | Ninguém; o auditor avalia |
| De controle (control risk) | Controles não evitarem nem detectarem | A gestão |
| De detecção (detection risk) | Os testes não acharem o erro | **O auditor**, pela natureza, época e extensão dos testes |

**Materialidade (materiality)**: o que muda a decisão de quem lê o relatório. Em sistemas, nem sempre é dinheiro.

## 2. Planejamento baseado em risco

- Universo de auditoria (audit universe) → avaliação de riscos (risk assessment) → plano anual aprovado pelo comitê, revisto quando surge risco novo.
- **Primeiro passo de um trabalho**: entender o negócio e avaliar os riscos da área. Testar vem depois.
- **Objetivo** (o que se quer concluir) ≠ **escopo** (sistemas, locais, processos, período).
- **Limitação de escopo**: registrar → tentar resolver → comunicar no relatório e ao comitê. Nunca contornar.
- **Programa de auditoria (audit program)**: liga risco → controle → teste.
- **Especialista**: a auditoria avalia competência e independência e continua dona da conclusão.

| Tipo de auditoria | Pergunta |
|---|---|
| Conformidade (compliance) | A regra está sendo seguida? |
| Financeira | As demonstrações são confiáveis? |
| Operacional | O processo é eficiente e eficaz? |
| Integrada (integrated) | Finanças, operação e sistemas juntos |
| Sistemas de informação | Os controles sobre a TI funcionam? |
| Forense (forensic) | Houve fraude? Evidência para processo |

## 3. Evidência, testes e amostragem

**Evidência**: suficiente, confiável, relevante. Da mais forte para a mais fraca: obtida pelo próprio auditor (reexecução, observação, inspeção) → externa e independente → interna → verbal.

| Teste | Pergunta | Amostragem típica |
|---|---|---|
| De controle ou conformidade (compliance test) | O controle foi aplicado? | Atributos (attribute sampling) |
| Substantivo (substantive test) | O valor está certo? | Variáveis (variable sampling) |

Controle forte → menos teste substantivo. Controle fraco → mais teste substantivo.

| Amostragem | Quando |
|---|---|
| Estatística (statistical) | Conclusão objetiva, com erro medido |
| Por julgamento (judgmental) | Rápida, sem medir o erro |
| Pare ou siga (stop-or-go) | Atributos, quando se espera pouquíssimo erro |
| Descoberta (discovery) | Basta um caso, como fraude |
| Estratificada (stratified) | Variáveis, com faixas de valor |

| Se aumenta... | A amostra... |
|---|---|
| Nível de confiança (confidence level) | Aumenta |
| Erro esperado (expected error rate) | Aumenta |
| Erro tolerável (tolerable error rate) | Diminui |
| Força do controle interno | Diminui |

## 4. Análise de dados, papéis de trabalho e fraude

| Técnica (CAATs) | Como funciona |
|---|---|
| Software generalizado de auditoria (generalized audit software) | Lê arquivos, totaliza, estratifica, acha duplicidades e lacunas |
| Dados de teste (test data) | Transações fictícias processadas no sistema |
| Instalação integrada de teste (integrated test facility) | Entidade fictícia na produção; retirar os efeitos depois |
| Simulação paralela (parallel simulation) | Programa do auditor processa dados reais e compara |
| Módulo embutido (SCARF) | Grava transações que atendem a critérios |
| Instantâneo (snapshot) | Fotografa a transação em vários pontos |
| Ganchos de auditoria (audit hooks) | Alertam em tempo real |

- Validar a completude dos dados antes de analisar; trabalhar sobre cópia.
- **Auditoria contínua (continuous auditing)** é da auditoria; **monitoramento contínuo (continuous monitoring)** é da gestão.
- **Papéis de trabalho**: outro auditor chega à mesma conclusão; revisados por supervisor; pertencem à organização; acesso controlado.
- **Fraude**: triângulo pressão, oportunidade, racionalização. Prevenir é da gestão. O auditor considera o risco, aplica ceticismo profissional e, diante de indício, comunica ao nível adequado (comitê, se a gestão estiver envolvida), sem investigar sozinho.

## 5. Achados, relatório e acompanhamento

| Parte do achado | Pergunta |
|---|---|
| Condição (condition) | O que é? |
| Critério (criteria) | O que deveria ser? |
| Causa (cause) | Por que é diferente? |
| Efeito (effect) | Qual o impacto? |

- A recomendação ataca a **causa**.
- Discordância da gestão com evidência sólida: o achado fica, a posição da gestão vai junto.
- Assunto grave: comunicar na hora.
- **O auditor recomenda, a gestão corrige, a auditoria acompanha (follow-up)**, e o vencido vai ao comitê.
- **Garantia de qualidade**: supervisão de cada trabalho e avaliações internas e externas.
- **Autoavaliação de controles (control self-assessment)**: a gestão avalia, a auditoria facilita.

## 6. Infraestrutura, redes e sistemas operacionais

| Componente | Risco | O auditor verifica |
|---|---|---|
| Hardware | Ativo desconhecido, falta de capacidade, descarte com dados | Inventário, manutenção, capacidade, apagamento seguro |
| Firewall | Regras antigas e amplas | Negar por padrão, revisão de regras, mudança aprovada |
| Rede | Invasor alcança tudo | Segmentação, DMZ, VPN, wireless criptografado |
| Sistema operacional | Administradores em excesso, sem atualização | Hardening, baseline, patch por prazo, logs protegidos |
| Virtualização | Hipervisor comprometido, máquinas esquecidas | Acesso restrito à console, inventário de máquinas virtuais |

## 7. Aplicações, bancos de dados e desenvolvimento

| Controle de aplicação | Exemplo |
|---|---|
| Faixa (range check) | Idade entre 16 e 100 |
| Limite (limit check) | Pagamento acima de um teto |
| Razoabilidade (reasonableness check) | Horas extras incompatíveis com o mês |
| Dígito verificador (check digit) | Pega números trocados de lugar |
| Total de lote (batch total) | Soma de valores antes e depois |
| Total de hash (hash total) | Soma de um campo sem sentido, como números de conta |
| Execução a execução (run-to-run totals) | Totais entre etapas |

- **Banco de dados**: chave primária e estrangeira, integridade referencial, normalização, dicionário de dados. O administrador de banco tem poder total: segregação, registro e revisão.
- **Desenvolvimento (SDLC)**: segurança desde os requisitos; ambientes separados; o usuário aprova no teste de aceitação (UAT); regressão protege o que já funcionava.
- **Implantação**: paralela (mais segura) > piloto > em fases > de uma vez (mais arriscada).
- O auditor aconselha no projeto, mas não desenha nem aprova controles.

## 8. Operações, serviços e nuvem

- **Incidente** restaura o serviço; **problema** acha a causa raiz.
- **SLA**: mensurável, medido e cobrado.
- **Análise de impacto no negócio (BIA)** vem antes do plano. **RTO** = tempo parado aceitável; **RPO** = perda de dados aceitável.

| Site alternativo | Prontidão |
|---|---|
| Espelhado (mirrored) | Quase imediata |
| Quente (hot) | Horas |
| Morno (warm) | Dias |
| Frio (cold) | Semanas |
| Acordo recíproco (reciprocal) | Barato e pouco confiável |

- Backup completo, incremental (rápido de fazer, lento de restaurar) e diferencial. **Teste de restauração** é o controle que importa.
- Testes do plano, do mais leve ao mais pesado: checklist → exercício de mesa (tabletop) → simulação → paralelo → interrupção completa.

| Nuvem | O cliente cuida de |
|---|---|
| IaaS | Sistema operacional, aplicação, dados, acessos |
| PaaS | Aplicação, dados, acessos |
| SaaS | Dados, usuários e acessos |

Em qualquer modelo, **os dados e o risco são do cliente**. Contrato com direito de auditar (right to audit), localização dos dados e saída.

## 9. Temas específicos de auditoria

- Acesso lógico: identificação → autenticação → autorização → responsabilização.
- **Multifator** exige tipos diferentes (saber, ter, ser). Duas senhas não contam.
- Privilégio mínimo e segregação de funções; sem segregação, controle compensatório.
- Entrada, mudança e saída (joiners, movers, leavers): acesso antigo retirado na mudança (evita privilege creep) e desativação imediata na saída.
- **Gestão de mudanças**: a população do teste vem da produção, não dos pedidos aprovados. Emergencial: registrar e aprovar depois.

| Relatório SOC | Cobre |
|---|---|
| SOC 1 | Controles que afetam as demonstrações financeiras do cliente |
| SOC 2 | Segurança, disponibilidade, integridade de processamento, confidencialidade, privacidade |
| Tipo 1 | Desenho, numa data |
| Tipo 2 | Desenho e funcionamento, num período (mais segurança) |

- Incidentes: preparação → detecção e análise → contenção → erradicação → recuperação → lições aprendidas.
- NIST CSF: governar, identificar, proteger, detectar, responder, recuperar.
- O dono do dado (data owner) classifica e decide o acesso.

## 10. Tecnologias novas

| Tecnologia | Risco principal | Pergunta do auditor |
|---|---|---|
| Inteligência artificial | Viés, explicabilidade, deriva do modelo | Dados de treinamento avaliados? Modelo testado? Supervisão humana? |
| IA generativa | Alucinação, vazamento de dados | Há política de uso e proteção de dados? |
| RPA | Credenciais amplas e inseguras | O robô é tratado como usuário privilegiado? |
| DevOps e CI/CD | Mudanças sem controle | Revisão por outra pessoa e testes obrigatórios na esteira? |
| Internet das Coisas | Senhas padrão, sem atualização | Inventário, segmentação, monitoramento? |
| Blockchain | Dado errado gravado para sempre, chaves | Validação na entrada, guarda das chaves, teste dos contratos inteligentes? |
| Zero trust | — | Cada acesso é verificado, mesmo dentro da rede? |

## Glossário português–inglês

| Português | Inglês |
|---|---|
| Carta de auditoria | Audit charter |
| Carta de contratação | Engagement letter |
| Trabalho de campo | Fieldwork |
| Acompanhamento | Follow-up |
| Universo de auditoria | Audit universe |
| Programa de auditoria | Audit program |
| Escopo | Scope |
| Evidência | Audit evidence |
| Reexecução | Reperformance |
| Teste de conformidade | Compliance test |
| Teste substantivo | Substantive test |
| Amostragem | Sampling |
| Papéis de trabalho | Audit work papers |
| Ceticismo profissional | Professional skepticism |
| Sinais de alerta | Red flags |
| Achado | Audit finding |
| Reunião de encerramento | Exit meeting |
| Resposta da gestão | Management response |
| Garantia de qualidade | Quality assurance |
| Autoavaliação de controles | Control self-assessment |
| Endurecimento | Hardening |
| Configuração de referência | Configuration baseline |
| Gestão de atualizações | Patch management |
| Computação do usuário final | End-user computing |
| Dígito verificador | Check digit |
| Integridade referencial | Referential integrity |
| Teste de aceitação do usuário | User acceptance testing |
| Revisão pós-implantação | Post-implementation review |
| Análise de impacto no negócio | Business impact analysis |
| Acordo de nível de serviço | Service level agreement |
| Responsabilidade compartilhada | Shared responsibility model |
| Direito de auditar | Right to audit |
| Privilégio mínimo | Least privilege |
| Segregação de funções | Segregation of duties |
| Revisão de acessos | User access review |
| Gestão de mudanças | Change management |
| Viés | Bias |
| Deriva do modelo | Model drift |
| Registro distribuído | Distributed ledger |
| Confiança zero | Zero trust |
