# P8 — Revisão geral em cenários
tipo: misto
dominio: Temas misturados
topicos: Cenários de prova de todos os domínios · Qual é a melhor ação · Qual é o primeiro passo

## Abertura
Capítulo de perguntas e respostas número oito: revisão geral em cenários. Aqui as perguntas imitam o estilo da prova:
uma situação curta e a melhor ação. Responda em voz alta antes de ouvir.

## Perguntas

### c-plano-incidente
P: No meio do ano, a empresa sofre um incidente grave num sistema que não estava no plano de auditoria. O que a auditoria faz com o plano?
R: Revê o plano com base no risco novo, com aprovação do comitê.

### c-primeiro
P: Você recebe um trabalho de auditoria numa área que não conhece. Qual é o primeiro passo?
R: Entender o negócio e avaliar os riscos da área.

### c-gestor-pede
P: O diretor da área auditada pede para ver e aprovar o relatório antes de ele ir ao comitê, e quer retirar um achado. O que fazer?
R: Discutir os fatos, registrar a posição dele, mas manter o achado se a evidência o sustenta.

### c-auditor-corrige
P: O gestor pede ao auditor que configure ele mesmo a correção que recomendou, para ganhar tempo. O que o auditor responde?
R: Que não pode: o auditor recomenda, a gestão implanta.

### = c-primeiro

### c-evid-verbal
P: O administrador diz que os backups são testados todo mês. O que o auditor faz com essa afirmação?
R: Pede evidência, como registros de testes de restauração, ou observa um teste.

### c-amostra-fraude
P: Há suspeita de que exista pelo menos um pagamento a fornecedor fantasma. Qual amostragem usar?
R: Amostragem de descoberta.

### c-caat
P: O auditor precisa procurar pagamentos duplicados em dois milhões de registros. Qual técnica?
R: Software generalizado de auditoria sobre uma cópia dos dados.

### c-fraude-chefe
P: O auditor percebe indícios de fraude envolvendo o diretor financeiro. Ele confronta o diretor?
R: Não. Comunica ao comitê de auditoria e preserva a evidência.

### = c-auditor-corrige

### c-contas-ex
P: Doze contas de ex-funcionários estão ativas. Qual é a causa mais provável a investigar?
R: Falha no aviso de desligamento do RH para a TI.
E: A recomendação deve atacar esse fluxo, não só desativar as doze contas.

### c-regra-firewall
P: O firewall tem uma regra que libera qualquer origem para qualquer destino, sem dono. Qual é a recomendação?
R: Retirar a regra e revisar as regras periodicamente, com dono e justificativa.

### c-dev-producao
P: Um programador consegue levar o próprio código para a produção sem ninguém aprovar. Qual princípio foi violado?
R: Segregação de funções entre desenvolvimento e produção.

### = c-evid-verbal

### c-rpo
P: A análise de impacto define que se pode perder no máximo uma hora de dados, mas o backup é diário. O que está errado?
R: O backup não atende ao R.P.O.

### c-saas
P: Um sistema de RH vai para um fornecedor SaaS. A responsabilidade pelos dados dos funcionários passa para o fornecedor?
R: Não. Continua com a empresa.

### c-soc1
P: O fornecedor só tem um S.O.C. dois do tipo um. O que falta para ter evidência de funcionamento?
R: Um tipo dois, que cobre um período.

### c-revisao-massa
P: Na revisão de acessos, os gestores aprovaram tudo, sem nenhuma retirada. O que isso sugere?
R: Que a revisão é mecânica e não está funcionando.

### = c-rpo

### c-robo
P: Um robô de automação usa a senha de um administrador, guardada num arquivo de texto. Qual é a recomendação?
R: Dar ao robô uma conta própria com acesso mínimo e guardar a credencial em cofre.

### c-ia-dados
P: A empresa vai usar um modelo de inteligência artificial para triagem de currículos. Qual é a primeira preocupação do auditor?
R: A qualidade e o viés dos dados de treinamento.

### c-cicd
P: Numa esteira de CI/CD, um desenvolvedor consegue desligar os testes automáticos da própria mudança. Qual é o problema?
R: O controle pode ser contornado; o acesso à esteira precisa ser restrito.

### = c-revisao-massa

### c-iot
P: Câmeras de segurança conectadas estão na mesma rede dos servidores financeiros. Qual é a recomendação?
R: Segmentar a rede, isolando os dispositivos.

### c-escopo-final
P: Última. O auditado nega acesso a um sistema do escopo e não há acordo. O que vai no relatório?
R: A limitação de escopo, comunicada também ao comitê.

### = c-dev-producao

## Encerramento
Fim do capítulo oito, o último de perguntas e respostas. Faça o simulado diagnóstico no site e volte aos capítulos dos domínios onde a nota ficou mais baixa. Boa prova.
