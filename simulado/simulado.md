# Simulado diagnóstico

20 questões distribuídas pelos pesos da prova: Performing an Audit 7, IT Environment 5, Specific Audit
Subjects 3, Newer Technologies 2, Controls, Risk and Audit 2, Audit Function 1. Formato de cada questão
igual ao quiz das seções. "## D? Nome" abre um domínio.

## D1 Audit Function

### Um auditor de sistemas participou, no ano passado, da escolha e da configuração do novo sistema de compras. Agora o plano anual prevê uma auditoria desse sistema e ele foi escalado. Qual é a melhor ação?
- [ ] Executar a auditoria normalmente, porque conhece bem o sistema
- [x] Comunicar o conflito à gestão da auditoria antes de começar, para que outro auditor seja avaliado
- [ ] Executar a auditoria e omitir do relatório a própria participação
- [ ] Pedir ao gestor de compras que aprove a sua participação
> Auditar o próprio trabalho fere a independência profissional. O conflito é comunicado antes de seguir; normalmente outro auditor assume.

## D2 Controls, Risk and Audit

### Numa equipe pequena, a mesma pessoa cadastra fornecedores e lança pagamentos. Não há como separar as funções. Qual controle é o mais adequado?
- [ ] Nenhum, porque a segregação é impossível
- [ ] Trocar a senha dessa pessoa todo mês
- [x] Uma revisão independente e periódica dos cadastros e pagamentos por outra pessoa
- [ ] Um backup diário da base de fornecedores
> Sem segregação, entra um controle compensatório: a revisão independente reduz o mesmo risco por outro caminho.

### Uma área processa transações de alto valor com muitas exceções manuais, e os testes mostraram controles fracos. Para manter o risco de auditoria aceitável, o auditor deve:
- [ ] Reduzir os testes, porque os controles já foram avaliados
- [x] Aumentar a extensão dos testes substantivos, reduzindo o risco de detecção
- [ ] Aceitar um risco de auditoria maior nessa área
- [ ] Reclassificar o risco inerente como baixo
> Com risco inerente e de controle altos, o único componente que o auditor ajusta é o risco de detecção, testando mais.

## D3 Performing an Audit

### Ao montar o plano anual, a função de auditoria tem horas para cobrir só um terço do universo de auditoria. Qual critério deve orientar a escolha?
- [ ] A ordem em que as áreas pediram auditoria
- [ ] Auditar as áreas que nunca tiveram achados
- [x] O resultado da avaliação de riscos de cada item do universo
- [ ] Distribuir as horas igualmente entre todas as áreas
> Na abordagem baseada em risco, os itens de risco mais alto entram primeiro.

### Durante o trabalho de campo, o gestor de TI se recusa a liberar os logs do banco de dados, que estão no escopo. O auditor tentou resolver com ele e não conseguiu. O próximo passo é:
- [ ] Retirar o banco de dados do escopo e seguir
- [ ] Obter os logs com a ajuda de um administrador, sem avisar o gestor
- [x] Levar a limitação de escopo ao nível superior e ao comitê de auditoria e registrá-la no relatório
- [ ] Concluir que o controle é eficaz, por falta de evidência contrária
> Limitação de escopo não resolvida é comunicada e relatada; nunca aceita em silêncio nem contornada.

### Qual evidência dá ao auditor a maior segurança de que o controle de bloqueio de conta após cinco tentativas erradas funciona?
- [ ] A política de senhas aprovada pela diretoria
- [ ] A declaração do administrador de que o bloqueio está ativo
- [x] O auditor tentar, numa conta de teste, seis logins errados e observar o bloqueio
- [ ] Um e-mail antigo da equipe de suporte sobre o assunto
> A reexecução pelo próprio auditor é a evidência mais forte do funcionamento de um controle.

### O auditor quer estimar o valor total de notas fiscais com erro numa população de cinquenta mil notas, dando mais atenção às de valor alto. Qual amostragem é a mais adequada?
- [ ] Amostragem de descoberta
- [ ] Amostragem por atributos do tipo pare ou siga
- [x] Amostragem por variáveis, estratificada por valor
- [ ] Amostragem por julgamento das notas mais recentes
> Estimar valor é amostragem por variáveis; estratificar por valor dá peso às faixas mais altas.

### O auditor quer comparar a lista completa de fornecedores com a de funcionários, procurando contas bancárias iguais. A técnica mais eficiente é:
- [ ] Entrevistar o gestor de compras
- [x] Usar software generalizado de auditoria sobre cópias das duas bases
- [ ] Selecionar vinte fornecedores por julgamento
- [ ] Pedir ao RH uma declaração de que não há conflito
> As técnicas assistidas por computador permitem cruzar cem por cento das duas populações.

### Na reunião de encerramento, o gestor discorda de um achado sobre contas de ex-funcionários ativas. O auditor revê a evidência e ela confirma o achado. O que fazer?
- [ ] Retirar o achado para preservar a relação
- [ ] Rebaixar a gravidade para baixa
- [x] Manter o achado e registrar a posição da gestão no relatório
- [ ] Adiar o relatório até haver acordo
> Achado apoiado em evidência permanece; a discordância da gestão fica registrada.

### Seis meses após o relatório, várias ações combinadas com a gestão estão vencidas e sem justificativa. Qual é a responsabilidade da auditoria?
- [ ] Executar ela mesma as correções pendentes
- [ ] Nenhuma, porque a correção é da gestão
- [x] Relatar as ações vencidas ao comitê de auditoria, como parte do acompanhamento
- [ ] Encerrar os achados para não poluir os indicadores
> O acompanhamento é da auditoria; a correção é da gestão; o vencido sobe ao comitê.

## D4 IT Environment and Components

### O auditor encontra dezenas de regras no firewall sem dono nem justificativa, algumas liberando qualquer origem para qualquer destino. Qual é a recomendação mais adequada?
- [ ] Trocar o fabricante do firewall
- [x] Revisar periodicamente as regras, com dono e justificativa, partindo de negar tudo por padrão
- [ ] Desligar o firewall para simplificar a rede
- [ ] Liberar todo o tráfego interno
> Negar por padrão e revisar as regras com dono e justificativa reduz a superfície de ataque.

### Um único servidor físico roda máquinas virtuais do sistema de pagamentos e do site público, e vários administradores têm acesso à console do hipervisor. Qual é o maior risco?
- [ ] Falta de espaço em disco
- [x] O comprometimento do hipervisor dar acesso a todas as máquinas virtuais
- [ ] O site ficar mais lento
- [ ] A licença do sistema operacional vencer
> O hipervisor é ponto único de ataque; o acesso a ele deve ser dos mais restritos.

### Um sistema de pagamentos recebe arquivos de outro sistema todas as noites. Qual controle confirma que nenhum registro se perdeu no caminho?
- [ ] Verificação de formato
- [x] Conciliação de totais de controle, como contagem de registros e total de hash, entre origem e destino
- [ ] Dígito verificador no nome do arquivo
- [ ] Teste de aceitação do usuário
> Totais de controle conferidos nos dois lados mostram completude e integridade da interface.

### Um sistema novo vai substituir o da folha de pagamento, e erro no primeiro mês seria inaceitável. Qual forma de implantação o auditor deve esperar ver?
- [ ] De uma vez, para encurtar o projeto
- [x] Em paralelo, comparando os resultados dos dois sistemas
- [ ] Piloto sem comparação de resultados
- [ ] Sem migração de dados
> A implantação paralela é a mais segura: o antigo segue rodando e os resultados são comparados.

### A análise de impacto no negócio definiu que o sistema de vendas pode perder, no máximo, quinze minutos de dados. O backup atual é diário. Qual conclusão?
- [ ] O backup atende, porque é feito todo dia
- [x] O backup não atende ao R.P.O. definido; é preciso replicação ou cópias mais frequentes
- [ ] O problema é o R.T.O., não o backup
- [ ] Basta guardar o backup fora do local
> O RPO de quinze minutos exige cópias pelo menos a cada quinze minutos.

## D5 Specific Audit Subjects

### Para testar se toda mudança em produção foi aprovada, qual é a melhor fonte para a amostra?
- [ ] Os pedidos de mudança aprovados no sistema de chamados
- [x] A lista de alterações extraída da própria produção, como registros de versão e de implantação
- [ ] As mudanças que o gestor de TI indicar
- [ ] As mudanças do último dia do mês
> Partir dos pedidos aprovados não encontra as mudanças feitas sem pedido, que são as mais arriscadas.

### Um provedor de nuvem crítico entrega um relatório SOC 2 tipo 1. O que o auditor deve considerar?
- [ ] Que o relatório prova o funcionamento dos controles no último ano
- [x] Que o tipo 1 avalia só o desenho numa data; um tipo 2 daria evidência de funcionamento ao longo de um período
- [ ] Que relatórios SOC não têm valor para auditoria
- [ ] Que o cliente deixa de ter responsabilidade sobre os dados
> O tipo 2 testa o funcionamento num período; e os controles complementares do usuário seguem com o cliente.

### Na revisão de acessos, os gestores aprovaram todas as contas sem nenhuma retirada, inclusive de pessoas que mudaram de área há meses. O que isso indica?
- [ ] Que os acessos estão corretos
- [x] Que a revisão é feita de forma mecânica e não evita o acúmulo de acessos
- [ ] Que a autenticação multifator é desnecessária
- [ ] Que o privilégio mínimo foi aplicado
> Aprovação em massa sugere revisão ineficaz; o acúmulo por mudança de função é o privilege creep.

## D6 Overview of Newer Technologies

### Uma empresa adota CI/CD e libera dezenas de mudanças por dia, sem aprovação manual de cada uma. O que o auditor deve avaliar?
- [ ] Se cada mudança tem uma assinatura em papel
- [x] Se os controles estão embutidos na esteira: revisão de código por outra pessoa, testes obrigatórios e acesso restrito à esteira
- [ ] Se a empresa voltou ao modelo em cascata
- [ ] Nada, porque DevOps dispensa controles
> Em DevOps os controles migram para a ferramenta, e a segregação continua: ninguém aprova a própria mudança.

### Um modelo de aprendizado de máquina aprova crédito. Qual pergunta do auditor trata o risco de viés?
- [ ] Qual é a velocidade do servidor que roda o modelo?
- [x] Os dados de treinamento foram avaliados quanto a origem e qualidade, e o modelo foi testado quanto a viés antes da produção?
- [ ] O modelo usa nuvem pública?
- [ ] Quantos usuários acessam o sistema?
> Viés nasce dos dados de treinamento; a resposta é governança dos dados e teste do modelo.
