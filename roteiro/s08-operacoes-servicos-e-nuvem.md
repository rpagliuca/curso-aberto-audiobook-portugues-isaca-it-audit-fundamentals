# Seção 8 — Ambiente de TI III: operações, serviços e nuvem

dominios: IT Environment and Components (25%)

## Narração

Seção oito, a última do ambiente de TI: operações, gestão de serviços, continuidade de negócios e computação em nuvem.

As operações de TI são o trabalho do dia a dia que mantém os sistemas rodando: agendar e executar as rotinas de processamento, monitorar servidores e redes, fazer backups, atender usuários e tratar falhas.

Comece pelo agendamento de rotinas, job scheduling. Muitos processos rodam sozinhos, em lote, por exemplo, o fechamento diário ou a folha de pagamento. Os controles aqui são: só pessoas autorizadas alteram a agenda, as rotinas rodam na ordem certa, as falhas são registradas e tratadas, e reprocessamentos são aprovados. O auditor olha o registro de execuções e verifica se as falhas tiveram tratamento.

Para organizar os serviços de TI, muitas organizações usam um modelo de gestão de serviços, IT service management. O mais conhecido é o I.T.I.L., uma biblioteca de boas práticas. Alguns processos dele caem na prova.

A gestão de incidentes, incident management, quer restaurar o serviço normal o mais rápido possível. A gestão de problemas, problem management, procura a causa raiz dos incidentes, para que eles não voltem. Guarde a diferença: incidente é apagar o fogo, problema é descobrir por que o fogo começa. Se o mesmo incidente se repete muitas vezes, falta gestão de problemas.

A gestão de configuração, configuration management, mantém um registro dos itens de TI e de como eles se relacionam, num banco de dados de configuração, configuration management database. Ele mostra o impacto de uma mudança antes de ela ser feita. A gestão de mudanças, que vamos detalhar na seção nove, controla como esses itens são alterados. E a gestão de liberações, release management, organiza como as mudanças chegam à produção, em pacotes testados.

O acordo de nível de serviço, em inglês service level agreement, é o compromisso entre o fornecedor do serviço e o cliente: disponibilidade, tempo de resposta, tempo de solução. Pode ser com um fornecedor externo ou entre a TI e as áreas de negócio. O auditor verifica se os níveis estão definidos de forma mensurável, se são medidos de verdade, e se o desempenho é relatado e cobrado.

Agora a continuidade, um assunto que a prova adora. Tudo começa pela análise de impacto no negócio, business impact analysis. Ela identifica os processos críticos e mede o impacto, ao longo do tempo, de uma parada em cada um. A análise de impacto vem antes do plano: sem ela, não se sabe o que recuperar primeiro.

Dela saem dois números. O tempo objetivo de recuperação, recovery time objective, ou R.T.O., é quanto tempo o processo pode ficar parado. O ponto objetivo de recuperação, recovery point objective, ou R.P.O., é quanto dado a organização aceita perder, medido em tempo. Se o R.P.O. é de uma hora, os dados precisam ser copiados pelo menos a cada hora. Quanto menores esses números, mais cara a solução.

O plano de continuidade de negócios, business continuity plan, cuida de manter o negócio funcionando. O plano de recuperação de desastres, disaster recovery plan, é a parte voltada para a tecnologia: como recuperar sistemas e dados. O plano precisa ter responsáveis, lista de contatos, procedimentos e ser guardado também fora do local principal.

Os locais alternativos de processamento aparecem muito. O site quente, hot site, já tem equipamentos e dados, pronto para assumir em horas. O site morno, warm site, tem parte da estrutura e leva alguns dias. O site frio, cold site, é só o espaço com energia e refrigeração, e leva semanas. O site espelhado, mirrored site, roda em paralelo com o principal e assume quase na hora. E o acordo recíproco, reciprocal agreement, é duas organizações se comprometendo a ajudar uma à outra. É barato, mas pouco confiável.

Os backups. O backup completo, full backup, copia tudo. O incremental copia só o que mudou desde o último backup de qualquer tipo: é rápido de fazer e mais lento de restaurar. O diferencial copia o que mudou desde o último backup completo. Cópias precisam ficar também fora do local principal, e os testes de restauração são o controle que mais importa: backup que nunca foi restaurado é uma esperança, não um controle.

Os testes do plano, do mais simples ao mais completo: a revisão de documento, checklist; o exercício de mesa, em inglês tabletop exercise ou walkthrough, em que a equipe percorre o plano discutindo um cenário; a simulação; o teste paralelo, em que o site alternativo é ativado sem parar o principal; e a interrupção completa, full interruption test, que desliga o principal de verdade. Esta última é a mais realista e a mais arriscada, e raramente é a primeira escolha. Depois de qualquer teste, os resultados são documentados e o plano é atualizado.

Agora a nuvem, cloud computing. Os três modelos de serviço são estes. Infraestrutura como serviço, IaaS: o provedor entrega servidores, rede e armazenamento virtuais, e o cliente cuida do sistema operacional para cima. Plataforma como serviço, PaaS: o provedor entrega também o sistema operacional e o ambiente de execução, e o cliente cuida da aplicação e dos dados. E software como serviço, SaaS: o provedor entrega a aplicação pronta, e o cliente cuida basicamente dos usuários, dos acessos e dos dados.

Os modelos de implantação: a nuvem pública, public cloud, compartilhada entre muitos clientes; a privada, private cloud, dedicada a uma organização; a híbrida, hybrid cloud, que combina as duas; e a comunitária, community cloud, compartilhada por organizações com necessidades parecidas.

A ideia mais importante para a prova é o modelo de responsabilidade compartilhada, shared responsibility model. A segurança é dividida entre o provedor e o cliente, e a divisão muda conforme o modelo de serviço. Mas uma coisa nunca muda: a responsabilidade pelos dados e pelo risco continua sendo do cliente. Terceirizar o serviço não terceiriza a responsabilidade.

O que o auditor verifica na nuvem? O contrato: níveis de serviço, localização dos dados, direito de auditar, right to audit, notificação de incidentes e a saída do contrato, ou seja, como recuperar os dados se a relação acabar. Os relatórios independentes do provedor, como os relatórios S.O.C., que vamos ver na seção nove. E a parte que é do cliente: configuração, acessos, criptografia e backup.

Vamos fixar com três perguntas.

Pergunta um: qual é a diferença entre gestão de incidentes e gestão de problemas? Pense. Incidentes restauram o serviço; problemas acham a causa raiz.

Pergunta dois: o que vem antes do plano de continuidade? Pense. A análise de impacto no negócio, business impact analysis.

Pergunta três: na nuvem, de quem é a responsabilidade pelos dados? Pense. Sempre do cliente.

Na próxima seção, os temas específicos de auditoria: acesso lógico, gestão de mudanças, terceiros, incidentes e segurança.

## Resumo

- Agendamento de rotinas (job scheduling): alteração autorizada, ordem certa, falhas tratadas, reprocessamento aprovado.
- Gestão de serviços (IT service management, I.T.I.L.): incidentes (incident management) restauram o serviço; problemas (problem management) acham a causa raiz. Configuração (configuration management database), liberações (release management).
- Acordo de nível de serviço (service level agreement): mensurável, medido, relatado e cobrado.
- Análise de impacto no negócio (business impact analysis) vem antes do plano. R.T.O. (recovery time objective): tempo parado aceitável. R.P.O. (recovery point objective): perda de dados aceitável.
- Plano de continuidade (business continuity plan) e de recuperação de desastres (disaster recovery plan).
- Sites: quente (hot), morno (warm), frio (cold), espelhado (mirrored), acordo recíproco (reciprocal agreement).
- Backup completo (full), incremental e diferencial; cópia fora do local; testar a restauração.
- Testes do plano: checklist, exercício de mesa (tabletop, walkthrough), simulação, paralelo, interrupção completa (full interruption).
- Nuvem (cloud computing): IaaS, PaaS, SaaS; pública, privada, híbrida, comunitária. Responsabilidade compartilhada (shared responsibility model); os dados são sempre do cliente.
- Auditoria de nuvem: contrato, direito de auditar (right to audit), localização dos dados, saída, relatórios S.O.C. e controles do cliente.

## Quiz

### O mesmo incidente se repete toda semana. O que está faltando?
- [ ] Gestão de incidentes
- [x] Gestão de problemas
- [ ] Gestão de capacidade
- [ ] Um novo acordo de nível de serviço
> A gestão de problemas busca a causa raiz para que o incidente não volte.

### Qual é a primeira etapa para montar um plano de continuidade?
- [ ] Contratar um hot site
- [ ] Comprar fitas de backup
- [x] Fazer a análise de impacto no negócio (business impact analysis)
- [ ] Testar a interrupção completa
> A análise de impacto define o que é crítico e os tempos de recuperação.

### O RPO (recovery point objective) indica:
- [ ] Quanto tempo o processo pode ficar parado
- [x] Quanto dado a organização aceita perder, medido em tempo
- [ ] O custo do site alternativo
- [ ] O número de pessoas da equipe de crise
> RPO de uma hora exige cópias pelo menos a cada hora.

### Qual site alternativo assume mais rápido, entre estes?
- [ ] Cold site
- [ ] Warm site
- [x] Hot site
- [ ] Acordo recíproco
> O hot site já tem equipamentos e dados; o mirrored site, se houver, é ainda mais rápido.

### Qual é o controle mais importante sobre backups?
- [ ] Usar sempre backup incremental
- [x] Testar a restauração periodicamente
- [ ] Guardar as cópias ao lado do servidor
- [ ] Fazer backup só uma vez por ano
> Sem teste de restauração, não há garantia de que o backup funciona.

### Numa contratação SaaS, de quem é a responsabilidade pelos dados?
- [ ] Do provedor
- [x] Do cliente
- [ ] Do auditor externo
- [ ] De ninguém
> No modelo de responsabilidade compartilhada, terceirizar o serviço não terceiriza a responsabilidade pelos dados.
