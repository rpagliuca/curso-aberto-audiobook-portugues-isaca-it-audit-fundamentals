# Seção 1 — A função de auditoria, controles e riscos

dominios: Audit Function (5%) · Controls, Risk and Audit (8%)

## Narração

Bem-vindo ao curso de preparação para o certificado IT Audit Fundamentals, da ISACA. Antes do conteúdo, uma palavra sobre a prova e sobre como este curso está montado.

A prova tem duas horas, é feita pela internet com um fiscal acompanhando pela câmera, e a nota mínima para aprovação é sessenta e cinco por cento. O conteúdo se divide em seis domínios, cada um com um peso. Executar uma auditoria vale trinta e cinco por cento. Ambiente e componentes de TI vale vinte e cinco. Temas específicos de auditoria vale quinze. Visão geral de tecnologias novas vale doze. Controles, riscos e auditoria vale oito. E a função de auditoria vale cinco.

Este curso tem dez seções de cerca de dez minutos, uma para cada dez por cento da prova. Esta primeira junta a função de auditoria e controles e riscos; depois vêm quatro seções sobre executar uma auditoria, três sobre o ambiente de TI, uma sobre temas específicos e uma sobre tecnologias novas. A prova é em inglês, então, sempre que um termo aparecer, você vai ouvir também o nome dele em inglês.

Vamos começar pelo que é, afinal, uma auditoria de sistemas de informação. É o exame formal, com testes, para saber quatro coisas. Primeiro, se os sistemas cumprem leis, regulamentos, contratos e normas do setor. Segundo, se seguem as políticas e os procedimentos da própria organização. Terceiro, se os dados têm o nível adequado de confidencialidade, integridade e disponibilidade. E quarto, se a operação de TI é eficiente e atinge as metas.

Para isso, o auditor revisa os controles, reúne evidências, avalia os pontos fortes e fracos e escreve um relatório com as fraquezas e as recomendações.

O processo típico tem três grandes fases. A primeira é o planejamento, em inglês planning. A segunda é o trabalho de campo, chamado fieldwork, em que o auditor testa e documenta. A terceira é o relatório e o acompanhamento, reporting e follow-up. Guarde essas três fases, porque as quatro seções sobre executar uma auditoria seguem exatamente essa ordem.

Para a ISACA, sistema de informação é mais amplo que tecnologia da informação: inclui, além do equipamento e do software, os processos e as pessoas que usam a informação.

Agora, a função de auditoria dentro da organização. A auditoria de sistemas pode fazer parte da auditoria interna, pode ser um grupo independente ou pode trabalhar junto com a auditoria financeira. Em qualquer caso, o papel dela precisa estar escrito num documento chamado carta de auditoria, em inglês audit charter. A carta de auditoria define a responsabilidade, a autoridade e a prestação de contas da função de auditoria. Quem a aprova é o nível mais alto da organização: o conselho de administração e o comitê de auditoria.

Não confunda a carta de auditoria com a carta de contratação, a engagement letter. A carta de auditoria cobre toda a atividade de auditoria da organização. A carta de contratação trata de um trabalho específico, com um objetivo próprio.

Um princípio atravessa tudo isso: independência. A função de auditoria deve se reportar ao comitê de auditoria, e não à área que ela audita. A ISACA separa dois tipos. A independência organizacional diz respeito à posição da auditoria na estrutura da empresa. A independência profissional diz respeito à postura do auditor: ele não pode ter interesse no resultado. Se um auditor ajudou a implantar um sistema, ele não deveria auditar esse mesmo sistema logo depois. Na prova, diante de um conflito de interesse, a resposta costuma ser comunicar o conflito antes de seguir.

Um modelo útil para situar a auditoria é o das três linhas, publicado pelo Instituto dos Auditores Internos, o IIA. A primeira linha é a gestão operacional, que é dona dos riscos e executa os controles no dia a dia. A segunda linha são as funções de risco e de conformidade, que apoiam e monitoram a primeira. A terceira linha é a auditoria interna, que dá uma avaliação independente sobre as duas primeiras.

A ISACA organiza a prática profissional em três camadas de documentos. As normas, em inglês standards, são obrigatórias. As diretrizes, guidelines, explicam como aplicar as normas. As ferramentas e técnicas, tools and techniques, dão exemplos e não criam exigência. As normas, por sua vez, se dividem em três grupos. As normas gerais tratam de ética, independência, objetividade, cuidado profissional e competência. As normas de execução, performance, tratam do planejamento, do escopo, do risco, da evidência e da supervisão. E as normas de relatório, reporting, tratam do tipo de relatório e do que deve ser comunicado. Tudo isso faz parte do ITAF, o framework de auditoria de TI da ISACA. A prova não pede números de normas; ela pede que você saiba aplicá-las.

Por fim, o código de ética da ISACA. Os pontos que mais caem são: trabalhar com objetividade e cuidado profissional, manter sigilo sobre o que soube no trabalho, a menos que a lei exija divulgação, aceitar só trabalhos para os quais tem competência e informar todos os fatos relevantes que, omitidos, distorceriam o resultado.

Agora, o segundo domínio desta seção: controles, riscos e auditoria.

Um controle é uma política, um procedimento, uma prática ou uma estrutura organizacional que reduz o risco. O controle interno, internal control, existe para dar à gestão segurança razoável de que os objetivos serão atingidos e de que eventos indesejados serão evitados, ou detectados e corrigidos. A expressão segurança razoável, reasonable assurance, aparece muito na prova: nenhum controle dá certeza absoluta.

Os controles se classificam pela função. O controle preventivo, preventive, impede que o erro ou o ataque aconteça. Exemplos: segregação de funções, controle de acesso, validação de dados na entrada, criptografia. O controle detectivo, detective, percebe e avisa que algo aconteceu. Exemplos: revisão de logs de acesso, totais de controle, relatórios de exceção, a própria auditoria interna. O controle corretivo, corrective, reduz o impacto e conserta o problema. Exemplos: backup, plano de recuperação de desastres, plano de resposta a incidentes.

Os controles também podem ser manuais ou automatizados. E aqui entram duas ideias que a prova cobra. O objetivo de controle, control objective, é o resultado que se quer alcançar, por exemplo, garantir que só pessoas autorizadas alterem a folha de pagamento. A atividade de controle, ou medida de controle, é o que de fato se faz para chegar lá, por exemplo, exigir aprovação de um gestor para cada alteração.

Outra distinção importante: controles gerais de TI e controles de aplicação. Os controles gerais, em inglês IT general controls, valem para todo o ambiente: gestão de acesso, gestão de mudanças, operação, backup, segurança física. Os controles de aplicação, application controls, ficam dentro de um sistema específico e cuidam da entrada, do processamento e da saída dos dados. Se os controles gerais forem fracos, o auditor não pode confiar muito nos controles de aplicação, porque alguém poderia, por exemplo, alterar o programa sem passar pela gestão de mudanças.

Quando o auditor acha um controle fraco, antes de relatar ele procura um controle compensatório, compensating control, que reduza o mesmo risco por outro caminho. Por exemplo, um relatório de erros mal feito pode ser compensado por uma conciliação manual de todas as transações. Já os controles sobrepostos, overlapping controls, são dois controles fortes cobrindo o mesmo risco, como um crachá na porta e um vigilante conferindo o crachá.

E o risco. Na auditoria, o conceito central é o risco de auditoria, audit risk: a chance de o auditor chegar a uma conclusão errada, deixando passar um erro relevante. Ele tem três componentes. O risco inerente, inherent risk, é o risco do próprio processo, sem considerar controle nenhum. O risco de controle, control risk, é a chance de os controles internos não evitarem nem detectarem o erro a tempo. E o risco de detecção, detection risk, é a chance de os testes do auditor não encontrarem o erro. Dos três, o auditor só controla o risco de detecção, ajustando quanto e como testa. Se o risco inerente e o de controle forem altos, o auditor reduz o risco de detecção testando mais.

Junto com o risco vem a materialidade, materiality: o tamanho a partir do qual um erro ou uma fraqueza importa para a decisão de quem lê o relatório. Em sistemas, a materialidade nem sempre é um valor em dinheiro; uma falha de acesso num sistema pequeno pode ser material se expuser dados de clientes.

Vamos fixar com três perguntas. Tente responder antes de ouvir a resposta.

Pergunta um: quem deve aprovar a carta de auditoria? Pense. O conselho de administração e o comitê de auditoria, o nível mais alto da organização.

Pergunta dois: uma revisão semanal dos logs de acesso é um controle de que tipo? Pense. É um controle detectivo, porque percebe o acesso indevido depois que ele aconteceu.

Pergunta três: dos três componentes do risco de auditoria, qual o auditor consegue controlar? Pense. O risco de detecção, ajustando a natureza, a época e a extensão dos testes.

Na próxima seção começamos o domínio mais pesado da prova, executar uma auditoria, pelo planejamento baseado em risco.

## Resumo

- Prova: 2 h, online com fiscal remoto, aprovação com 65%. Pesos: executar a auditoria 35%, ambiente de TI 25%, temas específicos 15%, tecnologias novas 12%, controles e riscos 8%, função de auditoria 5%.
- Fases da auditoria: planejamento (planning), trabalho de campo (fieldwork), relatório e acompanhamento (reporting, follow-up).
- Carta de auditoria (audit charter): responsabilidade, autoridade e prestação de contas da função; aprovada pelo conselho e pelo comitê de auditoria. Carta de contratação (engagement letter): um trabalho específico.
- Independência organizacional (posição na estrutura) e profissional (postura do auditor). A auditoria reporta ao comitê de auditoria.
- Três linhas (IIA): gestão operacional, risco e conformidade, auditoria interna.
- ISACA: normas (obrigatórias: gerais, de execução, de relatório), diretrizes, ferramentas e técnicas; tudo dentro do ITAF.
- Controles: preventivo, detectivo, corretivo; manual ou automatizado; objetivo de controle e atividade de controle; controles gerais de TI e de aplicação; compensatório e sobreposto.
- Risco de auditoria = inerente + de controle + de detecção; o auditor só controla o de detecção. Materialidade: o que importa para quem decide.

## Quiz

### Quem aprova a carta de auditoria (audit charter)?
- [x] O conselho de administração e o comitê de auditoria
- [ ] O diretor de TI
- [ ] O auditor responsável por cada trabalho
- [ ] O órgão regulador do setor
> A carta define autoridade e responsabilidade da função de auditoria; por isso vem do nível mais alto, que garante a independência.

### Qual é a diferença entre carta de auditoria e carta de contratação (engagement letter)?
- [ ] São o mesmo documento com nomes diferentes
- [x] A carta de auditoria cobre toda a função; a de contratação, um trabalho específico
- [ ] A carta de contratação é aprovada pelo conselho; a de auditoria, pelo auditor
- [ ] A carta de auditoria só existe em auditoria externa
> A carta de contratação detalha objetivo e escopo de um trabalho; a carta de auditoria é o mandato permanente.

### Uma revisão semanal dos logs de acesso é um controle:
- [ ] Preventivo
- [x] Detectivo
- [ ] Corretivo
- [ ] Dissuasivo
> Ela percebe o acesso indevido depois que ele ocorreu.

### Backup e plano de recuperação de desastres são controles:
- [ ] Preventivos
- [ ] Detectivos
- [x] Corretivos
- [ ] Compensatórios por definição
> Reduzem o impacto e restauram a operação depois do evento.

### Dos componentes do risco de auditoria, qual o auditor controla diretamente?
- [ ] Risco inerente
- [ ] Risco de controle
- [x] Risco de detecção
- [ ] Nenhum deles
> O auditor ajusta natureza, época e extensão dos testes para reduzir o risco de detecção.

### Antes de relatar um controle fraco, o auditor deve procurar:
- [ ] Um controle sobreposto
- [x] Um controle compensatório
- [ ] A aprovação do auditado
- [ ] Um novo objetivo de controle
> Um controle compensatório pode reduzir o mesmo risco por outro caminho, e isso muda a gravidade do achado.
