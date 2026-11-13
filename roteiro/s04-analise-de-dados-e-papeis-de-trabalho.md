# Seção 4 — Executar a auditoria III: análise de dados e papéis de trabalho

dominios: Performing an Audit (35%)

## Narração

Seção quatro: o computador como ferramenta do auditor, a análise de dados, os papéis de trabalho e a fraude.

Quando os dados estão em sistemas, o auditor usa o próprio computador para testá-los. O nome técnico é técnicas de auditoria assistidas por computador, em inglês computer-assisted audit techniques, ou simplesmente CAATs. A grande vantagem é poder examinar cem por cento da população em vez de uma amostra, e fazer isso de forma repetível. Outras vantagens: reduzir o erro humano, ganhar tempo e testar coisas que seriam impossíveis à mão, como comparar milhões de registros.

A ferramenta mais comum é o software generalizado de auditoria, generalized audit software. É um programa feito para auditores, capaz de ler arquivos de vários formatos e fazer operações típicas: totalizar, estratificar, extrair amostras, procurar duplicidades, procurar lacunas numa sequência, comparar dois arquivos e calcular idades, como a idade de um saldo a receber. Também existem os programas utilitários, utility software, que vêm com o sistema operacional ou com o banco de dados e podem ser usados para consultas e relatórios.

Há técnicas que testam o funcionamento do sistema, e não só os dados. Os dados de teste, test data, são transações fictícias que o auditor prepara e processa no sistema, conferindo se o resultado é o esperado. A instalação integrada de teste, integrated test facility, cria uma entidade fictícia dentro do ambiente de produção, como uma filial inventada, e processa transações de teste junto com as reais. O cuidado aqui é retirar depois os efeitos dessas transações, para não contaminar os dados reais. A simulação paralela, parallel simulation, faz o caminho inverso: o auditor escreve o próprio programa que imita a lógica do sistema, processa os dados reais nele e compara os resultados.

E há técnicas que ficam embutidas no sistema e coletam informação continuamente. O módulo embutido de auditoria, conhecido pela sigla SCARF, grava transações que atendem a critérios definidos pelo auditor, por exemplo, pagamentos acima de um valor. O instantâneo, snapshot, fotografa uma transação em vários pontos do processamento, para mostrar como ela foi transformada. E os ganchos de auditoria, audit hooks, são pontos no programa que disparam um alerta quando acontece algo suspeito, para o auditor agir logo.

Antes de usar qualquer dado, o auditor confere se ele está completo e íntegro. Por exemplo, compara o total de registros extraídos com o total do sistema de origem. Também trabalha sobre uma cópia, nunca altera dados de produção, e documenta a extração. Uma análise feita sobre dados incompletos leva a uma conclusão errada, por melhor que seja a técnica.

Isso nos leva à análise de dados, data analytics. O processo típico tem cinco passos: definir o objetivo da análise, obter os dados, validar os dados, analisar e, por fim, interpretar e relatar. Exemplos clássicos: cruzar o cadastro de fornecedores com o de funcionários, procurando endereços ou contas bancárias iguais. Procurar pagamentos duplicados. Procurar lançamentos feitos de madrugada ou no fim de semana. Comparar a lista de usuários ativos de um sistema com a lista de demitidos do RH.

Quando a análise roda o tempo todo, ela vira auditoria contínua ou monitoramento contínuo. A diferença cai na prova. A auditoria contínua, continuous auditing, é feita pela auditoria, para dar avaliação independente com mais frequência. O monitoramento contínuo, continuous monitoring, é feito pela gestão, como parte dos próprios controles. A auditoria pode se apoiar no monitoramento da gestão, mas não deve ser dona dele, para não perder a independência.

Agora, os papéis de trabalho, em inglês audit work papers ou audit documentation. São o registro de tudo o que o auditor fez: o planejamento, o programa de auditoria, os testes executados, as evidências obtidas, as conclusões e as revisões. A regra de ouro é que um outro auditor experiente, sem ter participado do trabalho, consiga entender pelos papéis de trabalho o que foi feito e chegar à mesma conclusão.

Alguns pontos sobre papéis de trabalho que a prova cobra. Eles precisam ser revisados por um supervisor, e a revisão fica registrada. Eles pertencem à organização ou à firma de auditoria, não ao auditor individual. O acesso a eles deve ser controlado, porque contêm informação sensível. E eles são guardados por um período definido em política, respeitando exigências legais. Hoje os papéis de trabalho costumam ser eletrônicos, e isso exige os mesmos cuidados de qualquer sistema: controle de acesso, backup e proteção contra alteração depois da revisão.

Uma ligação importante: cada achado do relatório precisa estar apoiado em evidência que está nos papéis de trabalho. Se não está documentado, para a auditoria não aconteceu.

Por fim, a fraude. Fraude é um ato intencional para obter vantagem indevida, normalmente com ocultação. Um modelo clássico para entender a fraude é o triângulo da fraude: pressão, oportunidade e racionalização. A pressão é o motivo, como uma dívida. A oportunidade é a falha de controle que permite o ato. E a racionalização é a justificativa que a pessoa dá a si mesma. Dos três, a oportunidade é o único que os controles atacam diretamente, e a segregação de funções é o controle mais lembrado para isso.

Qual é a responsabilidade do auditor diante da fraude? A prova é cuidadosa aqui. A responsabilidade principal de prevenir e detectar fraude é da gestão, por meio dos controles internos. O auditor não garante que encontrará toda fraude. Mas ele precisa considerar o risco de fraude no planejamento, ficar atento aos sinais de alerta, em inglês red flags, e aplicar ceticismo profissional, professional skepticism, que é não aceitar explicações sem evidência.

Exemplos de sinais de alerta: um funcionário que nunca tira férias, um fornecedor sem endereço físico, transações logo abaixo do limite de aprovação, documentos que só existem em cópia, e resistência a fornecer informações.

Se o auditor encontrar indícios de fraude, ele não investiga por conta própria nem confronta o suspeito. Ele comunica ao nível adequado da gestão, ou ao comitê de auditoria se a gestão estiver envolvida, e avalia, com orientação jurídica, se há obrigação de comunicar a autoridades. Preservar a evidência também é essencial, porque ela pode ir para um processo.

Vamos fixar com três perguntas.

Pergunta um: qual é a principal vantagem das técnicas de auditoria assistidas por computador? Pense. Poder testar cem por cento da população, de forma repetível.

Pergunta dois: qual técnica cria uma entidade fictícia dentro do ambiente de produção para processar transações de teste? Pense. A instalação integrada de teste, integrated test facility.

Pergunta três: o auditor encontra indícios de fraude envolvendo o diretor da área. A quem ele comunica? Pense. Ao comitê de auditoria, porque a gestão da área está envolvida.

Na próxima seção, fechamos o domínio executar uma auditoria: achados, relatório e acompanhamento.

## Resumo

- Técnicas de auditoria assistidas por computador (computer-assisted audit techniques, CAATs): testar cem por cento da população, de forma repetível.
- Software generalizado de auditoria (generalized audit software): totalizar, estratificar, amostrar, duplicidades, lacunas, comparar arquivos, idade de saldos.
- Testam o sistema: dados de teste (test data), instalação integrada de teste (integrated test facility, com entidade fictícia em produção), simulação paralela (parallel simulation).
- Embutidas: módulo embutido de auditoria (SCARF), instantâneo (snapshot), ganchos de auditoria (audit hooks).
- Antes de analisar: validar completude e integridade dos dados, trabalhar sobre cópia, documentar a extração.
- Análise de dados (data analytics): objetivo, obter, validar, analisar, relatar.
- Auditoria contínua (continuous auditing) é da auditoria; monitoramento contínuo (continuous monitoring) é da gestão.
- Papéis de trabalho (audit work papers): outro auditor deve chegar à mesma conclusão; revisados por supervisor; pertencem à organização; acesso controlado; retenção por política.
- Fraude: triângulo pressão, oportunidade e racionalização. Prevenir é da gestão; o auditor considera o risco, procura sinais de alerta (red flags) e aplica ceticismo profissional (professional skepticism).
- Indício de fraude: comunicar ao nível adequado (comitê, se a gestão estiver envolvida), preservar a evidência, não investigar sozinho.

## Quiz

### A principal vantagem das CAATs é:
- [ ] Dispensar o planejamento
- [x] Permitir testar a população inteira, de forma repetível
- [ ] Substituir os papéis de trabalho
- [ ] Eliminar a necessidade de evidência
> Com o computador, o auditor examina todos os registros e pode repetir o teste.

### Qual técnica processa transações de teste numa entidade fictícia dentro da produção?
- [ ] Simulação paralela
- [x] Instalação integrada de teste (integrated test facility)
- [ ] Instantâneo (snapshot)
- [ ] Software generalizado de auditoria
> A integrated test facility exige retirar depois os efeitos das transações de teste.

### Na simulação paralela, o auditor:
- [ ] Assiste ao operador processar os dados
- [x] Processa os dados reais num programa próprio e compara com o resultado do sistema
- [ ] Insere transações fictícias na produção
- [ ] Grava transações acima de um limite
> O programa do auditor imita a lógica do sistema; diferenças apontam erro.

### Quem é o dono do monitoramento contínuo (continuous monitoring)?
- [ ] A auditoria interna
- [x] A gestão
- [ ] O auditor externo
- [ ] O regulador
> Monitoramento contínuo é controle da gestão; a auditoria contínua é da auditoria.

### Os papéis de trabalho devem permitir que:
- [ ] Só o autor entenda o que foi feito
- [x] Outro auditor experiente chegue à mesma conclusão
- [ ] O auditado altere as conclusões
- [ ] A evidência seja descartada após o relatório
> Esse é o critério de documentação suficiente.

### Qual elemento do triângulo da fraude os controles internos atacam diretamente?
- [ ] Pressão
- [ ] Racionalização
- [x] Oportunidade
- [ ] Nenhum
> Controles como segregação de funções reduzem a oportunidade.
