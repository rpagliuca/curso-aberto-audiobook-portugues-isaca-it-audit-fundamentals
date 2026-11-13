# P5 — Infraestrutura, aplicações e bancos de dados
tipo: tema
dominio: IT Environment and Components 25%
topicos: Hardware · Redes e firewall · Sistema operacional · Virtualização · Controles de aplicação · Bancos de dados · Desenvolvimento

## Abertura
Capítulo de perguntas e respostas número cinco: infraestrutura, aplicações, bancos de dados e desenvolvimento.

## Perguntas

### inventario
P: Por que o inventário de ativos é a base dos controles de hardware?
R: Porque um ativo desconhecido não recebe atualização nem proteção.

### descarte
P: Qual é o controle no descarte de um disco?
R: Apagar os dados de forma segura ou destruir o disco.

### firewall
P: Qual é a regra-base mais segura de um firewall?
R: Negar tudo por padrão e liberar só o necessário.

### dmz
P: Onde ficam os servidores acessados pela internet, como o site da empresa?
R: Na zona desmilitarizada, a DMZ.
E: Uma rede intermediária, separada da rede interna.

### = firewall

### hardening
P: Como se chama retirar de um servidor os serviços, portas e contas desnecessários?
R: Endurecimento, hardening.

### patch
P: Que medida mostra se a gestão de atualizações funciona?
R: O tempo entre a publicação de uma correção crítica e a sua aplicação.

### hipervisor
P: Na virtualização, qual componente concentra o maior risco?
R: O hipervisor, hypervisor.
E: Quem o compromete alcança todas as máquinas virtuais.

### = hardening

### check-digit
P: Qual controle de entrada detecta dois números trocados de lugar na digitação?
R: O dígito verificador, check digit.

### limit-check
P: Qual verificação confere só um teto, como um pagamento acima de um valor?
R: A verificação de limite, limit check.

### hash-total
P: Como se chama a soma de um campo sem significado, como os números de conta, usada para conferir completude?
R: Total de hash, hash total.

### = check-digit

### integridade-ref
P: O que garante a integridade referencial?
R: Que uma chave estrangeira aponte sempre para um registro existente.

### dba
P: Qual é o principal risco do administrador de banco de dados?
R: Poder alterar dados diretamente, sem passar pela aplicação.
E: Por isso: segregação de funções, registro e revisão independente.

### euc
P: Como se chamam as planilhas e automações feitas pelas próprias áreas de negócio, fora da TI?
R: Computação do usuário final, end-user computing.

### = dba

### seguranca-requisitos
P: Em que momento do desenvolvimento os requisitos de segurança devem entrar?
R: Desde o início, nos requisitos.

### uat
P: Qual teste é a última aprovação do negócio antes da produção?
R: O teste de aceitação do usuário, user acceptance testing.

### regressao
P: Qual teste confirma que uma mudança não estragou o que já funcionava?
R: O teste de regressão, regression testing.

### paralela
P: Qual forma de implantação é a mais segura, mas mais cara?
R: A paralela, com o sistema novo e o antigo rodando juntos.

### = uat

### auditor-dev
P: Qual é o limite do auditor num projeto de desenvolvimento?
R: Pode aconselhar, mas não desenha nem aprova os controles.

## Encerramento
Fim do capítulo cinco. No próximo: operações, continuidade, nuvem e os temas específicos de auditoria.
