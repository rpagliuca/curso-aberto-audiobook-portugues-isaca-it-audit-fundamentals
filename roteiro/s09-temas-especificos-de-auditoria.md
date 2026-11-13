# Seção 9 — Temas específicos de auditoria

dominios: Specific Audit Subjects (15%)

## Narração

Seção nove: temas específicos de auditoria, que valem quinze por cento da prova. São os assuntos que um auditor de TI mais audita na vida real: acesso lógico, gestão de mudanças, terceiros, incidentes e segurança da informação, incluindo privacidade.

Comece pelo acesso lógico, logical access. É o controle sobre quem pode usar quais sistemas e dados. Ele se apoia em quatro ideias, na ordem em que acontecem. A identificação, identification, é dizer quem você é, normalmente com um nome de usuário. A autenticação, authentication, é provar que você é quem diz ser. A autorização, authorization, é o sistema decidir o que você pode fazer. E a responsabilização, accountability, é conseguir ligar cada ação a uma pessoa, por meio dos registros.

A autenticação usa três tipos de fator: algo que você sabe, como uma senha; algo que você tem, como um celular ou um token; e algo que você é, como a digital ou o rosto. A autenticação multifator, multi-factor authentication, combina pelo menos dois tipos diferentes. Atenção: duas senhas são dois fatores do mesmo tipo, e por isso não contam como multifator.

Dois princípios atravessam todo o acesso lógico. O privilégio mínimo, least privilege: cada pessoa recebe só o acesso necessário para a sua função. E a segregação de funções, segregation of duties: tarefas que, juntas, permitiriam uma fraude ficam com pessoas diferentes. O exemplo clássico é que quem cadastra um fornecedor não deveria aprovar pagamentos a ele. Quando a segregação não é possível, por exemplo, numa equipe pequena, entra um controle compensatório, como a revisão independente das transações.

O ciclo de vida do acesso é chamado, em inglês, de joiners, movers and leavers: quem entra, quem muda de função e quem sai. Na entrada, o acesso é concedido com aprovação do gestor e do dono do dado. Na mudança de função, o acesso antigo é retirado, e não apenas somado ao novo. Esse acúmulo de acessos ao longo das mudanças de função tem nome em inglês: privilege creep. E na saída, o acesso é desativado imediatamente. Contas de ex-funcionários ativas são um dos achados mais comuns em auditoria.

A revisão periódica de acessos, user access review, é o controle detectivo que fecha o ciclo: os gestores ou os donos dos dados confirmam, de tempos em tempos, que cada pessoa ainda precisa do acesso que tem. O auditor verifica se a revisão aconteceu, se foi feita por quem conhece a necessidade, e se os acessos marcados para retirada foram de fato retirados.

O acesso privilegiado merece cuidado especial. Contas de administrador devem ser nominais, poucas, usadas só quando necessário e com as ações registradas. Soluções de gestão de acesso privilegiado, privileged access management, guardam as senhas dessas contas, liberam o acesso por tempo limitado e gravam as sessões.

Agora a gestão de mudanças, change management. É o processo que controla toda alteração em sistemas, programas e configurações. Os passos típicos: um pedido formal, a avaliação de impacto e risco, a aprovação, o desenvolvimento num ambiente separado, o teste, a aprovação do usuário, a liberação para a produção por alguém diferente de quem desenvolveu e o registro de tudo.

A prova cobra muito a segregação entre desenvolvimento e produção: o programador não deveria levar o próprio código para a produção. E as mudanças emergenciais, emergency changes: quando algo precisa ser corrigido na hora, a mudança pode pular etapas, mas precisa ser registrada, e aprovada e revisada depois, num prazo curto.

Um teste de auditoria clássico: o auditor tira uma lista das mudanças que de fato aconteceram em produção, a partir do próprio sistema, e confere se cada uma tem pedido, aprovação e teste. O caminho contrário, partir dos pedidos aprovados, não encontra as mudanças feitas sem pedido, que são justamente as mais arriscadas.

Agora os terceiros, third parties. Fornecedores de software, de nuvem, de suporte e de serviços terceirizados fazem parte do ambiente de controle. A gestão de risco de terceiros, third-party risk management, tem um ciclo: avaliação antes de contratar, due diligence; contrato com cláusulas de segurança, níveis de serviço, confidencialidade e direito de auditar; monitoramento durante a relação; e saída planejada no fim.

Quando não é possível auditar o fornecedor diretamente, o auditor usa relatórios de auditores independentes. Os mais citados são os relatórios S.O.C., de controles de organizações de serviço. O S.O.C. um trata de controles que afetam as demonstrações financeiras do cliente. O S.O.C. dois trata de segurança, disponibilidade, integridade de processamento, confidencialidade e privacidade. E existe a diferença entre tipo um e tipo dois. O tipo um avalia o desenho dos controles numa data. O tipo dois avalia também se os controles funcionaram ao longo de um período, normalmente de seis meses a um ano. Para o auditor, o tipo dois dá muito mais segurança.

Ao usar esses relatórios, o auditor confere o escopo, o período, as exceções encontradas e os controles que o relatório diz serem responsabilidade do cliente, os chamados controles complementares do usuário. Os subcontratados do fornecedor, às vezes chamados de quarta parte, também entram na análise.

Agora os incidentes de segurança. A gestão de incidentes de segurança, security incident management, tem fases conhecidas: preparação, detecção e análise, contenção, erradicação, recuperação e lições aprendidas. A preparação inclui ter um plano, uma equipe definida e canais para reportar. E as lições aprendidas fecham o ciclo, melhorando os controles. O auditor verifica se os incidentes são registrados, classificados, escalados no prazo e se há evidência do que foi feito.

Um modelo muito usado para organizar a segurança é o framework de segurança cibernética do N.I.S.T., o instituto de padrões dos Estados Unidos. As funções dele são: governar, identificar, proteger, detectar, responder e recuperar.

Na segurança da informação em geral, alguns controles aparecem sempre. A classificação da informação, data classification, define níveis como pública, interna e confidencial, e cada nível tem regras de proteção. O dono do dado, data owner, decide a classificação e quem acessa. A criptografia protege os dados em trânsito e armazenados, e as chaves precisam de gestão cuidadosa. E o treinamento de conscientização, security awareness, reduz o risco de engenharia social, como o phishing.

Por fim, a privacidade, privacy. Leis como a L.G.P.D., no Brasil, e o G.D.P.R., na Europa, exigem que dados pessoais sejam tratados com base legal, para uma finalidade definida, no mínimo necessário e com direitos do titular respeitados. O auditor verifica se a organização sabe quais dados pessoais tem, onde estão, por que os guarda e por quanto tempo.

Vamos fixar com três perguntas.

Pergunta um: uma senha e uma pergunta secreta formam autenticação multifator? Pense. Não. As duas são algo que você sabe, o mesmo tipo de fator.

Pergunta dois: para testar a gestão de mudanças, de onde o auditor deve tirar a população? Pense. Das mudanças que de fato aconteceram em produção, e não dos pedidos aprovados.

Pergunta três: qual relatório S.O.C. avalia se os controles funcionaram ao longo de um período? Pense. O tipo dois.

Na próxima e última seção de conteúdo: tecnologias novas.

## Resumo

- Acesso lógico (logical access): identificação (identification), autenticação (authentication), autorização (authorization), responsabilização (accountability).
- Fatores: algo que sabe, tem, é. Multifator (multi-factor authentication) exige tipos diferentes; duas senhas não contam.
- Privilégio mínimo (least privilege) e segregação de funções (segregation of duties); sem segregação, controle compensatório.
- Ciclo de acesso (joiners, movers and leavers): aprovar na entrada, retirar o antigo na mudança (evita privilege creep), desativar na saída. Revisão periódica (user access review) com retirada efetiva.
- Acesso privilegiado: contas nominais e poucas, registro, gestão de acesso privilegiado (privileged access management).
- Gestão de mudanças (change management): pedido, impacto, aprovação, teste, aceite, liberação por outra pessoa, registro. Emergenciais (emergency changes) aprovadas depois. População tirada da produção.
- Terceiros (third-party risk management): due diligence, contrato com direito de auditar, monitoramento, saída. S.O.C. um (financeiro) e S.O.C. dois (segurança e outros); tipo um (desenho numa data) e tipo dois (funcionamento num período). Controles complementares do usuário; quarta parte.
- Incidentes (security incident management): preparação, detecção e análise, contenção, erradicação, recuperação, lições aprendidas. N.I.S.T.: governar, identificar, proteger, detectar, responder, recuperar.
- Segurança: classificação (data classification), dono do dado (data owner), criptografia e chaves, conscientização (security awareness) contra phishing.
- Privacidade (privacy): L.G.P.D. e G.D.P.R.; base legal, finalidade, mínimo necessário, direitos do titular.

## Quiz

### Senha mais pergunta secreta é autenticação multifator?
- [ ] Sim, porque são dois fatores
- [x] Não, porque os dois são "algo que você sabe"
- [ ] Sim, se a senha for forte
- [ ] Só se a pergunta mudar todo dia
> Multifator exige tipos diferentes: saber, ter, ser.

### Um funcionário mudou três vezes de área e manteve todos os acessos antigos. Isso se chama:
- [ ] Privilégio mínimo
- [x] Privilege creep
- [ ] Segregação de funções
- [ ] Revisão de acesso
> O acesso antigo deve ser retirado em cada mudança de função.

### Para testar a gestão de mudanças, a melhor população é:
- [ ] Os pedidos de mudança aprovados
- [x] As mudanças que de fato ocorreram em produção, extraídas do sistema
- [ ] As mudanças que o gestor indicar
- [ ] Só as mudanças emergenciais
> Partir dos pedidos não encontra as mudanças feitas sem pedido.

### Uma mudança emergencial em produção deve:
- [ ] Ser proibida em qualquer caso
- [ ] Dispensar registro
- [x] Ser registrada e aprovada e revisada depois, num prazo curto
- [ ] Ser feita só pelo auditor
> A urgência permite pular etapas, não o controle.

### Qual relatório dá mais segurança sobre o funcionamento dos controles de um fornecedor?
- [ ] SOC 1 tipo 1
- [ ] SOC 2 tipo 1
- [x] SOC 2 tipo 2
- [ ] Uma declaração do próprio fornecedor
> O tipo 2 testa o funcionamento ao longo de um período; o SOC 2 cobre segurança e disponibilidade.

### Quem decide a classificação de uma informação e quem pode acessá-la?
- [ ] O administrador de rede
- [ ] O auditor
- [x] O dono do dado (data owner)
- [ ] O fornecedor de nuvem
> O dono do dado responde por ele; a TI executa a proteção como custodiante.
