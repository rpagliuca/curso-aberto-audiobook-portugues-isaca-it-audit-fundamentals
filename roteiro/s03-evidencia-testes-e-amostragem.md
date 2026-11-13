# Seção 3 — Executar a auditoria II: evidência, testes e amostragem

dominios: Performing an Audit (35%)

## Narração

Seção três: evidência, testes e amostragem. É o miolo do trabalho de campo, e um dos assuntos que mais aparecem na prova.

Comece pela evidência, em inglês audit evidence. É toda informação que o auditor usa para chegar à conclusão. Sem evidência, não há achado nem opinião: há só impressão. A ISACA pede que a evidência seja suficiente, confiável e relevante. Suficiente quer dizer que há quantidade bastante para convencer uma pessoa razoável. Confiável quer dizer que dá para acreditar nela. Relevante quer dizer que ela tem relação direta com o objetivo de controle que está sendo avaliado.

A confiabilidade da evidência depende de alguns fatores, e a prova cobra a comparação entre eles. Primeiro, a independência de quem fornece: uma confirmação vinda de fora da organização, como o extrato enviado pelo banco, é mais confiável que um relatório produzido pelo próprio auditado. Segundo, a qualificação de quem fornece: um especialista é mais confiável que um leigo. Terceiro, a objetividade: um dado medido é mais confiável que uma opinião. Quarto, a forma de obtenção: o que o auditor observa ou recalcula por conta própria vale mais do que aquilo que lhe contam. E quinto, o momento: evidência do período auditado vale mais do que evidência antiga.

Guarde uma regra prática. Evidência obtida diretamente pelo auditor é a mais forte. Evidência externa vem em seguida. Evidência interna e verbal é a mais fraca, e quase sempre precisa ser confirmada por outra.

Agora, as técnicas de coleta. A entrevista, ou indagação, em inglês inquiry, é perguntar às pessoas como o processo funciona. É útil para entender, mas sozinha é evidência fraca. A observação, observation, é ver o processo acontecendo, por exemplo, assistir ao operador fazer o backup. O problema é que as pessoas podem se comportar melhor quando estão sendo observadas. A inspeção, inspection, é examinar documentos, registros e configurações. A reexecução, reperformance, é o auditor refazer o controle por conta própria para ver se dá o mesmo resultado. O recálculo confere contas. A confirmação externa pede a um terceiro que confirme uma informação. E o passo a passo, walkthrough, é acompanhar uma transação do início ao fim no sistema, para confirmar que o processo funciona como foi descrito.

Na prova, quando a pergunta for qual é a evidência mais confiável de que um controle funciona, a reexecução feita pelo próprio auditor costuma ganhar da entrevista e da observação.

Agora os testes. Há dois grandes tipos, e essa distinção é essencial.

O teste de controle, que a ISACA chama de teste de conformidade, compliance test, verifica se um controle existe e funciona como deveria. A pergunta dele é sim ou não: o controle foi aplicado? Por exemplo, verificar se todas as alterações de programa da amostra têm aprovação registrada.

O teste substantivo, substantive test, verifica a própria informação, os valores, os saldos, as transações. A pergunta dele é quanto: o valor está certo? Por exemplo, recalcular a folha de pagamento de uma amostra de funcionários, ou contar o estoque físico e comparar com o sistema.

A relação entre os dois cai muito. Se os testes de controle mostram que os controles são fortes, o auditor pode reduzir os testes substantivos. Se os controles são fracos, ele precisa aumentar os testes substantivos, porque não pode confiar nos controles para evitar o erro. É a ideia do risco de detecção que você ouviu na seção um, agora na prática.

Quase nunca dá para testar cem por cento das transações. Por isso o auditor usa amostragem, sampling. Os termos básicos: a população, population, é o conjunto inteiro de onde se tira a amostra. A amostra, sample, é a parte examinada. E a conclusão sobre a amostra é estendida à população.

Há duas famílias de amostragem. A amostragem estatística, statistical sampling, usa seleção aleatória e cálculo de probabilidade. Ela permite dizer, com um nível de confiança conhecido, quanto a conclusão pode estar errada. A amostragem não estatística, nonstatistical sampling, também chamada de amostragem por julgamento, judgmental sampling, usa a experiência do auditor para escolher os itens. É mais rápida, mas não permite medir o erro da amostra. Na prova: se a questão pedir uma conclusão objetiva e defensável sobre a população, a resposta é amostragem estatística.

Agora os tipos de amostragem que a ISACA cobra. A amostragem por atributos, attribute sampling, é usada em testes de controle. Ela mede a taxa de ocorrência: em quantos por cento dos casos o controle falhou. A amostragem por variáveis, variable sampling, é usada em testes substantivos. Ela estima um valor, como o total em reais de um saldo.

Dentro da amostragem por atributos há duas variações. A amostragem pare ou siga, stop-or-go sampling, permite parar cedo se os primeiros itens não mostram erro. Ela é usada quando se espera pouquíssimo erro. E a amostragem de descoberta, discovery sampling, é usada quando basta encontrar um único caso para concluir, como na busca de fraude. Dentro da amostragem por variáveis, a mais citada é a estratificada, stratified sampling, que divide a população em faixas, por exemplo, por valor, e tira amostras de cada uma, dando mais atenção às faixas de valor alto.

Por fim, os parâmetros que definem o tamanho da amostra. O nível de confiança, confidence level, é a certeza que o auditor quer ter, como noventa e cinco por cento. A taxa de erro tolerável, tolerable error rate, é o máximo de erro que o auditor aceita sem mudar a conclusão. A taxa de erro esperada, expected error rate, é quanto erro ele imagina encontrar. E a precisão, precision, é a margem em torno do resultado.

As regras que a prova cobra são estas. Quanto maior o nível de confiança, maior a amostra. Quanto maior o erro esperado, maior a amostra. Quanto maior o erro tolerável, menor a amostra. E quanto mais forte o controle interno, menor pode ser a amostra, porque o auditor pode usar um nível de confiança menor.

Uma última ideia: o risco de amostragem, sampling risk, é a chance de a amostra não representar a população, levando a uma conclusão errada. A amostragem estatística não elimina esse risco, mas permite medi-lo.

Vamos fixar com três perguntas.

Pergunta um: qual tipo de teste verifica se um controle foi aplicado? Pense. O teste de controle, que a ISACA chama de teste de conformidade, compliance test.

Pergunta dois: se a taxa de erro esperada aumenta, o que acontece com o tamanho da amostra? Pense. Aumenta.

Pergunta três: qual amostragem se usa quando basta encontrar um único caso, como numa suspeita de fraude? Pense. A amostragem de descoberta, discovery sampling.

Na próxima seção: técnicas de auditoria com o computador, análise de dados e papéis de trabalho.

## Resumo

- Evidência (audit evidence): suficiente, confiável e relevante.
- Confiabilidade: fonte independente (externa vale mais que interna), fornecedor qualificado, dado objetivo, obtida diretamente pelo auditor, do período auditado.
- Técnicas: entrevista (inquiry), observação (observation), inspeção (inspection), reexecução (reperformance), recálculo, confirmação externa, passo a passo (walkthrough). A reexecução é a evidência mais forte de que um controle funciona.
- Teste de controle ou de conformidade (compliance test): o controle foi aplicado? Teste substantivo (substantive test): o valor está certo? Controle forte permite menos teste substantivo.
- Amostragem estatística (statistical sampling): aleatória, mede o erro. Não estatística ou por julgamento (nonstatistical, judgmental sampling): não mede.
- Atributos (attribute sampling): taxa de ocorrência, testes de controle; inclui pare ou siga (stop-or-go) e descoberta (discovery). Variáveis (variable sampling): valores, testes substantivos; inclui estratificada (stratified).
- Tamanho da amostra: sobe com o nível de confiança e com o erro esperado; cai com o erro tolerável e com controle interno forte.
- Risco de amostragem (sampling risk): a amostra não representar a população.

## Quiz

### Qual destas evidências é, em geral, a mais confiável?
- [ ] A explicação verbal do gestor da área
- [ ] Um relatório gerado pelo auditado
- [x] Uma confirmação enviada diretamente ao auditor por um terceiro independente
- [ ] Um e-mail interno encaminhado pelo auditado
> Evidência de fonte externa e independente, recebida diretamente, é mais confiável que evidência interna ou verbal.

### O auditor refaz o cálculo de juros de uma amostra de contratos para ver se o sistema calcula certo. Isso é:
- [ ] Observação
- [ ] Entrevista
- [x] Reexecução
- [ ] Confirmação externa
> O auditor executa por conta própria e compara o resultado.

### Verificar se todas as mudanças de programa da amostra têm aprovação registrada é um:
- [x] Teste de controle (conformidade)
- [ ] Teste substantivo
- [ ] Teste de estresse
- [ ] Teste de penetração
> A pergunta é se o controle de aprovação foi aplicado: sim ou não.

### Os testes de controle mostraram controles fracos. O auditor deve:
- [ ] Reduzir os testes substantivos
- [x] Aumentar os testes substantivos
- [ ] Encerrar o trabalho sem relatório
- [ ] Trocar a amostragem estatística por julgamento
> Sem poder confiar nos controles, o auditor precisa testar mais a própria informação para manter o risco de detecção baixo.

### Qual amostragem se usa para estimar o valor total de um saldo?
- [ ] Atributos
- [ ] Descoberta
- [x] Variáveis
- [ ] Pare ou siga
> A amostragem por variáveis estima valores; a por atributos mede taxa de ocorrência.

### O que acontece com o tamanho da amostra se o auditor aceita um erro tolerável maior?
- [ ] Aumenta
- [x] Diminui
- [ ] Não muda
- [ ] Passa a ser cem por cento
> Aceitar mais erro exige menos itens para chegar à mesma conclusão.
