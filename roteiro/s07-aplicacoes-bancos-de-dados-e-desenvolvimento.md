# Seção 7 — Ambiente de TI II: aplicações, bancos de dados e desenvolvimento

dominios: IT Environment and Components (25%)

## Narração

Seção sete: aplicações, bancos de dados e o ciclo de desenvolvimento de sistemas. Se a seção anterior era a base, esta é onde mora a informação do negócio.

Comece pelas aplicações. São os sistemas que apoiam os processos de negócio: vendas, compras, contabilidade, folha de pagamento. Muitas organizações usam um sistema integrado de gestão, em inglês enterprise resource planning, o E.R.P., que junta vários processos num só sistema e num só banco de dados. A vantagem é a integração. O risco é que um erro ou um acesso indevido se espalha por vários processos de uma vez.

Há também a computação do usuário final, end-user computing: planilhas, pequenos bancos de dados e automações feitas pelas próprias áreas de negócio, fora da TI. Elas são úteis, mas costumam escapar dos controles de mudança, de acesso e de backup. Quando uma planilha dessas alimenta uma decisão importante ou um número financeiro, o auditor precisa olhar para ela como olharia para um sistema.

Na seção um você ouviu sobre os controles de aplicação, application controls. Agora o detalhe. Eles se dividem em controles de entrada, de processamento e de saída.

Os controles de entrada, input controls, garantem que só entrem dados válidos, completos e autorizados. Os mais cobrados são as validações. A verificação de faixa, range check, confere se o valor está entre um mínimo e um máximo. A verificação de limite, limit check, confere só um teto, como um pagamento acima de um valor. A verificação de razoabilidade, reasonableness check, confere se o valor faz sentido no contexto. A verificação de existência confere se o código informado existe no cadastro. A verificação de formato, ou de campo, confere se o dado tem o tipo certo. E o dígito verificador, check digit, é um número calculado a partir dos outros, que detecta erros de digitação, como dois números trocados de lugar.

Os controles de processamento garantem que o sistema processe tudo, uma vez só e do jeito certo. Os totais de controle aparecem aqui. O total de lote, batch total, soma os valores de um lote antes e depois do processamento. O total de hash, hash total, soma um campo que não tem significado, como o número das contas, só para confirmar que nenhum registro foi perdido ou alterado. E os totais de execução a execução, run-to-run totals, conferem os totais entre uma etapa e a seguinte.

Os controles de saída cuidam do resultado: relatórios que chegam só a quem deve receber, conciliação dos totais de saída com os de entrada, e guarda ou destruição segura de relatórios sensíveis.

E as interfaces, que ligam um sistema a outro. Hoje elas costumam ser interfaces de programação, em inglês application programming interfaces, as A.P.I.s. Numa interface, o auditor verifica se tudo o que saiu de um sistema chegou ao outro, completo e sem alteração, e se os erros são tratados, e não simplesmente descartados.

Agora os bancos de dados. Um sistema de gerenciamento de banco de dados, database management system, organiza, guarda e protege os dados. O modelo mais comum é o relacional, em que os dados ficam em tabelas ligadas por chaves. A chave primária, primary key, identifica cada registro de forma única. A chave estrangeira, foreign key, aponta para um registro de outra tabela. E a integridade referencial, referential integrity, garante que uma chave estrangeira sempre aponte para um registro que existe. Por exemplo, que não exista um pedido de um cliente que não está no cadastro.

A normalização, normalization, é organizar as tabelas para evitar dados repetidos, o que reduz inconsistências. E o dicionário de dados, data dictionary, descreve cada campo: o nome, o tipo, o significado e quem é o dono.

O papel-chave aqui é o administrador de banco de dados, database administrator, que tem poder para alterar qualquer dado diretamente, sem passar pela aplicação. Por isso a segregação de funções é essencial: o administrador de banco não deveria lançar transações de negócio, e as ações dele devem ser registradas e revisadas por outra pessoa. Alterações diretas nos dados de produção precisam de aprovação e de registro.

O que o auditor verifica no banco de dados: quem tem acesso direto, especialmente com privilégio alto; se os logs do banco estão ligados e protegidos; se há backup testado; e se a integridade referencial está ativa nas tabelas importantes.

Agora o ciclo de desenvolvimento de sistemas, em inglês system development life cycle, conhecido pela sigla S.D.L.C. As fases tradicionais são estas: estudo de viabilidade, levantamento de requisitos, desenho, desenvolvimento, testes, implantação e revisão pós-implantação. No modelo em cascata, waterfall, cada fase termina antes da seguinte começar, com documentação formal. Nos métodos ágeis, agile, o sistema é entregue em ciclos curtos, com o usuário perto da equipe o tempo todo. Os dois precisam de controles; nos ágeis, eles ficam mais automáticos e mais distribuídos ao longo do trabalho.

A prova gosta de dois pontos sobre requisitos. Primeiro, os requisitos de segurança e de controle devem entrar desde o início, e não ser acrescentados no fim, quando custam muito mais. Segundo, o usuário de negócio precisa participar e aprovar os requisitos.

Os tipos de teste. O teste unitário, unit testing, testa cada parte do programa isoladamente. O teste de integração, integration testing, testa se as partes funcionam juntas. O teste de sistema testa o sistema inteiro, incluindo desempenho e segurança. O teste de aceitação do usuário, user acceptance testing, é feito pelo próprio usuário para confirmar que o sistema atende ao negócio, e é a última aprovação antes de ir para a produção. E o teste de regressão, regression testing, confirma que uma mudança não estragou o que já funcionava.

Ambientes separados são um controle importante: desenvolvimento, teste e produção. O desenvolvedor não deveria ter acesso para alterar a produção.

A implantação pode ser feita de quatro formas. Em paralelo, parallel changeover, o sistema novo e o antigo rodam juntos por um tempo, o que é mais seguro e mais caro. Em fases, phased changeover, módulo a módulo. Em piloto, pilot, num local primeiro. E de uma vez, abrupt changeover, desligando o antigo e ligando o novo, que é o mais arriscado. Na migração de dados, o auditor confere se os dados chegaram completos e corretos, com conciliação de totais.

Por fim, a revisão pós-implantação, post-implementation review, verifica se o sistema entregou os benefícios prometidos e se os controles funcionam.

E o papel do auditor no desenvolvimento? Ele pode participar como consultor, revisando se os controles estão previstos, mas não deve desenhar nem aprovar os controles, para não perder a independência na auditoria futura do sistema.

Vamos fixar com três perguntas.

Pergunta um: qual controle detecta dois números trocados de lugar na digitação de um código? Pense. O dígito verificador, check digit.

Pergunta dois: qual teste é a última aprovação do negócio antes da produção? Pense. O teste de aceitação do usuário, user acceptance testing.

Pergunta três: qual forma de implantação é a mais segura, mas mais cara? Pense. Em paralelo, com o sistema novo e o antigo rodando juntos.

Na próxima seção: operações de TI, gestão de serviços, continuidade e nuvem.

## Resumo

- Aplicações: E.R.P. (enterprise resource planning) integra processos e espalha erros. Computação do usuário final (end-user computing) escapa de controles e precisa de atenção quando alimenta decisões.
- Entrada (input controls): faixa (range check), limite (limit check), razoabilidade (reasonableness check), existência, formato, dígito verificador (check digit).
- Processamento: total de lote (batch total), total de hash (hash total), totais de execução a execução (run-to-run totals). Saída: distribuição restrita, conciliação, guarda ou destruição.
- Interfaces e A.P.I.s (application programming interfaces): tudo o que saiu chegou, completo, e os erros são tratados.
- Banco de dados (database management system): chave primária (primary key), chave estrangeira (foreign key), integridade referencial (referential integrity), normalização (normalization), dicionário de dados (data dictionary).
- Administrador de banco (database administrator): poder total; segregação de funções, registro e revisão das ações.
- S.D.L.C. (system development life cycle): viabilidade, requisitos, desenho, desenvolvimento, testes, implantação, revisão pós-implantação (post-implementation review). Cascata (waterfall) e ágil (agile). Segurança desde os requisitos.
- Testes: unitário (unit), integração (integration), sistema, aceitação do usuário (user acceptance testing, última aprovação), regressão (regression).
- Implantação: paralela (parallel changeover, mais segura), em fases (phased), piloto (pilot), de uma vez (abrupt changeover, mais arriscada).
- O auditor pode aconselhar no desenvolvimento, mas não desenha nem aprova controles.

## Quiz

### Qual controle detecta dois dígitos trocados de lugar num código de conta?
- [ ] Verificação de faixa
- [x] Dígito verificador (check digit)
- [ ] Total de lote
- [ ] Teste de regressão
> O dígito verificador é calculado a partir dos outros e falha quando há transposição.

### Um total de hash (hash total) soma:
- [ ] O valor em dinheiro de todas as transações
- [x] Um campo sem significado, como números de conta, só para conferir completude
- [ ] O número de usuários do sistema
- [ ] O tempo de processamento
> A soma não tem sentido de negócio; serve para mostrar que nada foi perdido ou alterado.

### A integridade referencial (referential integrity) garante que:
- [ ] Todo campo tenha valor
- [x] Uma chave estrangeira aponte sempre para um registro existente
- [ ] Os dados sejam criptografados
- [ ] O banco tenha backup
> Evita, por exemplo, um pedido de cliente inexistente.

### Qual é o principal risco do administrador de banco de dados?
- [ ] Não saber programar
- [x] Poder alterar dados diretamente, sem passar pela aplicação
- [ ] Trabalhar só em desenvolvimento
- [ ] Usar o modelo relacional
> Por isso suas ações precisam de segregação, registro e revisão independente.

### Qual teste é a última aprovação do negócio antes da produção?
- [ ] Teste unitário
- [ ] Teste de integração
- [x] Teste de aceitação do usuário (user acceptance testing)
- [ ] Teste de regressão
> É o usuário quem confirma que o sistema atende ao negócio.

### Qual forma de implantação traz o maior risco?
- [ ] Paralela
- [ ] Em fases
- [ ] Piloto
- [x] De uma vez (abrupt changeover)
> Sem o sistema antigo rodando, não há como voltar rápido nem comparar resultados.
