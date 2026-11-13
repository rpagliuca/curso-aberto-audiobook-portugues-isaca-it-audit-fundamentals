# Seção 10 — Tecnologias novas

dominios: Overview of Newer Technologies (12%)

## Narração

Seção dez, a última de conteúdo: visão geral de tecnologias novas, que vale doze por cento da prova. A prova aqui é de visão geral. Ela quer que você saiba o que cada tecnologia é, qual risco novo ela traz e qual pergunta o auditor deve fazer. A regra que vale para todas: a tecnologia muda, mas os princípios de controle continuam os mesmos. Governança, acesso, mudança, dados e continuidade.

Comece pela inteligência artificial, artificial intelligence. É a capacidade de um sistema executar tarefas que normalmente exigiriam inteligência humana, como reconhecer padrões, prever ou gerar texto. O aprendizado de máquina, machine learning, é a forma mais comum: em vez de seguir regras escritas por um programador, o modelo aprende a partir de dados de exemplo, os dados de treinamento, training data.

Daí vem o primeiro risco: o modelo é tão bom quanto os dados com que aprendeu. Dados incompletos, desatualizados ou enviesados produzem decisões enviesadas. Esse é o viés, em inglês bias. Um modelo de crédito treinado com decisões antigas pode reproduzir uma discriminação que existia nelas.

O segundo risco é a explicabilidade, explainability. Muitos modelos funcionam como uma caixa-preta: dão a resposta, mas não mostram por quê. Para decisões que afetam pessoas, como crédito ou contratação, a organização precisa conseguir explicar e contestar o resultado.

O terceiro risco é a deriva do modelo, model drift. O mundo muda e o modelo, treinado com o passado, vai perdendo a precisão. Por isso modelos precisam de monitoramento contínuo do desempenho e de retreinamento controlado, como qualquer mudança.

A inteligência artificial generativa, generative AI, que produz texto, imagem e código, traz riscos próprios. Ela pode inventar informações com aparência de verdade, o que se chama alucinação. Funcionários podem colar dados confidenciais em ferramentas públicas. E o conteúdo gerado pode violar direitos autorais.

O que o auditor pergunta sobre inteligência artificial? Existe uma política e um responsável? Há um inventário dos modelos em uso, inclusive os embutidos em produtos comprados? Os dados de treinamento têm origem conhecida, qualidade verificada e base legal? O modelo foi testado quanto a viés e precisão antes de ir para a produção? Há supervisão humana, human in the loop, nas decisões de alto impacto? E as mudanças no modelo passam pela gestão de mudanças? O próprio auditor também pode usar inteligência artificial nas suas análises, mas continua responsável por validar o resultado.

Agora a automação robótica de processos, robotic process automation. São programas, os robôs, que imitam o que uma pessoa faz na tela: copiar dados de um sistema para outro, preencher formulários, conciliar planilhas. O risco principal está nas credenciais: o robô precisa de um usuário, e muitas vezes esse usuário tem acesso amplo e senha guardada de forma insegura. Outros riscos: robôs alterados sem gestão de mudanças, e robôs que param quando a tela de um sistema muda, sem ninguém perceber. O auditor trata o robô como um usuário privilegiado e como um programa: acesso mínimo, dono definido, mudanças controladas e monitoramento das execuções.

Agora o DevOps, a junção de desenvolvimento e operações. Em vez de grandes liberações a cada poucos meses, as equipes entregam pequenas mudanças várias vezes por dia, com muita automação. A base é a integração contínua e a entrega contínua, em inglês continuous integration e continuous delivery, a esteira conhecida como CI/CD. Cada mudança no código dispara automaticamente a compilação, os testes e, se tudo passar, a liberação.

Para o auditor, a pergunta muda. Em vez de procurar uma assinatura de aprovação em cada mudança, ele avalia se os controles estão embutidos na esteira e se funcionam. Por exemplo: toda mudança exige revisão de código por outra pessoa antes de entrar? Os testes automáticos são obrigatórios e não podem ser pulados? Quem pode alterar a própria esteira? Em DevOps a segregação de funções não desaparece: ela passa a ser garantida pela ferramenta, como a regra de que ninguém aprova a própria mudança.

Quando a segurança entra nessa esteira desde o início, com análise automática de código e de componentes de terceiros, fala-se em DevSecOps. E a infraestrutura como código, infrastructure as code, descreve servidores e redes em arquivos versionados, que passam pelo mesmo controle de mudanças que o software. Os contêineres, que você ouviu na seção seis, costumam fazer parte desse mundo, e as imagens deles também precisam de controle de origem e de vulnerabilidades.

Agora a Internet das Coisas, em inglês Internet of Things. São dispositivos conectados que não são computadores tradicionais: câmeras, sensores industriais, fechaduras, medidores, equipamentos médicos. Os riscos típicos: senhas padrão de fábrica que nunca são trocadas, falta de atualização de software, pouca capacidade para criptografia e grande quantidade de dispositivos, muitas vezes fora do inventário da TI. Um dispositivo desses pode virar a porta de entrada para a rede inteira. Os controles: inventário, troca das senhas padrão, segmentação da rede para isolar os dispositivos, atualização sempre que possível e monitoramento do tráfego.

Agora o blockchain. É um registro distribuído, distributed ledger: muitas cópias do mesmo livro de registros, mantidas por vários participantes. Cada bloco de transações é ligado ao anterior por criptografia, e um mecanismo de consenso, consensus, define como os participantes concordam sobre o que entra. O resultado é um registro muito difícil de alterar depois de gravado. Os contratos inteligentes, smart contracts, são programas gravados no blockchain que executam regras sozinhos quando as condições são cumpridas.

Atenção às pegadinhas. Difícil de alterar não quer dizer correto: se um dado errado ou fraudulento entrar, ele fica lá para sempre. Um contrato inteligente com erro de programação executa o erro automaticamente. E a segurança depende muito das chaves privadas, private keys: quem perde a chave perde o acesso, e quem a rouba pode agir como o dono. O auditor pergunta como os dados são validados antes de entrar, quem pode participar, como as chaves são guardadas e como os contratos inteligentes são testados e alterados.

Duas ideias rápidas para fechar. A confiança zero, zero trust, é um modelo de segurança em que nada é confiável só por estar dentro da rede: cada acesso é verificado, com identidade, dispositivo e contexto. E o big data trata volumes de dados enormes e variados, o que amplia o valor da análise de dados para a auditoria e, ao mesmo tempo, os riscos de privacidade e de qualidade dos dados.

Vamos fixar com três perguntas.

Pergunta um: um modelo de aprendizado de máquina foi treinado com decisões antigas que discriminavam um grupo. Qual é o risco? Pense. Viés, em inglês bias.

Pergunta dois: em DevOps, como fica a segregação de funções? Pense. Ela continua, garantida pela ferramenta, por exemplo, ninguém aprova a própria mudança.

Pergunta três: um registro em blockchain é difícil de alterar. Isso garante que o dado esteja correto? Pense. Não. Garante só que ele não muda depois de gravado.

Com isso, terminamos o conteúdo. Agora vale fazer o simulado diagnóstico no site e ouvir os capítulos de perguntas e respostas, que retomam todos os domínios. Bons estudos e boa prova.

## Resumo

- Princípio: a tecnologia muda, os princípios de controle ficam (governança, acesso, mudança, dados, continuidade).
- Inteligência artificial (artificial intelligence) e aprendizado de máquina (machine learning): o modelo aprende com dados de treinamento (training data). Riscos: viés (bias), explicabilidade (explainability), deriva (model drift).
- I.A. generativa (generative AI): alucinação, vazamento de dados confidenciais, direitos autorais.
- Auditoria de I.A.: política e responsável, inventário de modelos, origem e qualidade dos dados, testes de viés e precisão, supervisão humana (human in the loop), mudanças controladas.
- Automação robótica (robotic process automation): robô como usuário privilegiado e como programa; credenciais seguras, dono, mudanças controladas, monitoramento.
- DevOps e CI/CD (continuous integration, continuous delivery): controles embutidos na esteira; revisão de código por outra pessoa; testes obrigatórios; acesso restrito à esteira. DevSecOps; infraestrutura como código (infrastructure as code).
- Internet das Coisas (Internet of Things): senhas padrão, falta de atualização, fora do inventário; segmentar e monitorar.
- Blockchain: registro distribuído (distributed ledger), consenso (consensus), contratos inteligentes (smart contracts), chaves privadas (private keys). Imutável não é o mesmo que correto.
- Confiança zero (zero trust): verificar cada acesso. Big data: mais análise, mais risco de privacidade e qualidade.

## Quiz

### Um modelo de crédito reproduz discriminações das decisões antigas usadas no treinamento. Qual é o risco?
- [x] Viés (bias)
- [ ] Deriva do modelo (model drift)
- [ ] Alucinação
- [ ] Privilege creep
> Dados de treinamento enviesados produzem decisões enviesadas.

### Um modelo vai perdendo precisão porque o comportamento dos clientes mudou. Isso é:
- [ ] Viés
- [x] Deriva do modelo (model drift)
- [ ] Explicabilidade
- [ ] Consenso
> O modelo foi treinado com o passado; precisa de monitoramento e retreinamento controlado.

### Qual é o principal risco de um robô de automação (RPA)?
- [ ] Ser lento demais
- [x] Usar credenciais com acesso amplo guardadas de forma insegura
- [ ] Não ter interface gráfica
- [ ] Rodar só em nuvem
> O robô deve ser tratado como usuário privilegiado: acesso mínimo e credenciais protegidas.

### Em DevOps, a segregação de funções:
- [ ] Deixa de existir
- [x] Continua, garantida pela ferramenta (ninguém aprova a própria mudança)
- [ ] Passa a ser responsabilidade do auditor
- [ ] Só vale para a produção física
> Os controles migram para a esteira de CI/CD.

### Qual é o controle básico para dispositivos de Internet das Coisas?
- [ ] Deixar as senhas de fábrica
- [x] Inventariar, trocar senhas padrão e segmentar a rede
- [ ] Ligar todos à rede interna principal
- [ ] Dispensar atualizações
> Dispositivos IoT costumam ser a porta de entrada mais fraca.

### Um dado gravado em blockchain:
- [ ] É sempre correto
- [x] É difícil de alterar, mas pode estar errado se entrou errado
- [ ] Pode ser apagado por qualquer participante
- [ ] Dispensa controle de chaves
> Imutabilidade não garante a qualidade da entrada.
