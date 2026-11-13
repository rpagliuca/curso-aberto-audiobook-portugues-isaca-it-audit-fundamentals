# Seção 6 — Ambiente de TI I: infraestrutura, redes e sistemas operacionais

dominios: IT Environment and Components (25%)

## Narração

Seção seis. Começamos o segundo domínio mais pesado da prova, ambiente e componentes de TI, com vinte e cinco por cento das questões. São três seções. Esta trata da base física e lógica: hardware, redes, sistemas operacionais e virtualização. A prova não espera que você seja engenheiro de redes. Ela espera que você saiba o que cada componente faz, quais riscos ele traz e o que o auditor verifica.

Comece pelo hardware. Os componentes clássicos de um computador são o processador, a memória, o armazenamento e os dispositivos de entrada e saída. Numa organização, o hardware vai de servidores no datacenter e equipamentos de armazenamento até notebooks, celulares e impressoras dos usuários.

O que o auditor olha no hardware? Primeiro, o inventário de ativos, asset inventory: a organização sabe o que tem, onde está e quem é o responsável? Um ativo que ninguém conhece não recebe atualização nem proteção. Segundo, a manutenção: existe um plano de manutenção preventiva, com contratos de suporte em vigor? Terceiro, a capacidade: os servidores e discos têm folga para o crescimento? A gestão de capacidade, capacity management, acompanha o uso e planeja compras antes que falte recurso. Quarto, os relatórios de disponibilidade e de problemas de hardware, que mostram se as falhas estão sendo registradas e tratadas. E quinto, o descarte: equipamentos e discos descartados precisam ter os dados apagados de forma segura, ou destruídos, para que a informação não saia junto.

Agora as redes. Uma rede local, em inglês local area network, liga equipamentos num mesmo prédio ou campus. Uma rede de longa distância, wide area network, liga locais distantes, como a matriz e as filiais. A internet é a maior rede de longa distância que existe.

Para organizar o funcionamento das redes, existe um modelo de referência em sete camadas, o modelo O.S.I. De baixo para cima: física, enlace, rede, transporte, sessão, apresentação e aplicação. Na prática, a internet usa o conjunto de protocolos TCP/IP, que agrupa essas funções em menos camadas. Para a prova, basta saber que cada camada cuida de uma parte da comunicação, e que equipamentos diferentes atuam em camadas diferentes.

Os equipamentos principais são estes. O switch liga os equipamentos dentro de uma rede local. O roteador, router, liga redes diferentes e decide o caminho dos pacotes. O firewall filtra o tráfego, deixando passar só o que as regras permitem. E o balanceador de carga, load balancer, distribui as requisições entre vários servidores.

Sobre o firewall, a prova cobra alguns pontos. A regra mais segura é negar tudo por padrão e liberar só o necessário. As regras precisam ser revisadas periodicamente, porque regras antigas e esquecidas viram brechas. E as mudanças nas regras passam pela gestão de mudanças, com aprovação.

Outro conceito: a segmentação de rede, network segmentation. É dividir a rede em partes isoladas, para que um invasor que entre numa parte não alcance tudo. Um exemplo clássico é a zona desmilitarizada, em inglês demilitarized zone, a famosa D.M.Z.: uma rede intermediária onde ficam os servidores que precisam ser acessados pela internet, como o site da empresa, separada da rede interna.

O acesso remoto à rede da empresa costuma passar por uma rede privada virtual, virtual private network, a V.P.N., que cria um túnel criptografado pela internet. As redes sem fio, wireless, exigem criptografia forte e autenticação, porque o sinal vaza para fora do prédio.

O que o auditor verifica em redes? Se existe um diagrama de rede atualizado. Se as configurações dos equipamentos seguem um padrão aprovado. Se as senhas padrão de fábrica foram trocadas. Se os acessos administrativos são restritos e registrados. Se o tráfego é monitorado. E se há redundância nos pontos críticos, para que a queda de um equipamento não pare a empresa.

Agora o sistema operacional, operating system. É o software que gerencia o hardware e permite que os outros programas rodem. Exemplos: Windows, Linux e os sistemas dos celulares. Ele controla quem pode usar cada recurso, e por isso é uma camada crítica de segurança: quem domina o sistema operacional domina tudo o que roda em cima dele.

Os riscos típicos do sistema operacional são estes. Contas administrativas em excesso, ou compartilhadas, sem saber quem fez o quê. Configurações padrão inseguras. Falta de atualizações de segurança. E programas utilitários poderosos, que podem alterar dados sem passar pelos controles das aplicações.

Os controles correspondentes. O endurecimento, em inglês hardening, é retirar do sistema tudo o que não é necessário: serviços, portas, contas e programas, e ajustar as configurações para o padrão seguro. A organização define uma configuração de referência, configuration baseline, e verifica se os servidores seguem essa referência. A gestão de atualizações, patch management, garante que as correções de segurança sejam testadas e aplicadas num prazo definido conforme a gravidade. O acesso privilegiado, privileged access, fica restrito a poucas pessoas, com contas nominais e com registro de tudo o que fazem. E os registros do sistema, os logs, são protegidos contra alteração, inclusive pelos próprios administradores.

O auditor costuma pedir a lista de contas administrativas e comparar com quem realmente precisa. Também compara a configuração real de uma amostra de servidores com a configuração de referência, e verifica o tempo médio entre a publicação de uma correção crítica e a sua aplicação.

Por fim, a virtualização. Com ela, um único servidor físico roda vários servidores virtuais, as máquinas virtuais, em inglês virtual machines. Quem faz isso é o hipervisor, hypervisor, uma camada de software entre o hardware e as máquinas virtuais. As vantagens são economia, flexibilidade e facilidade de criar e recuperar servidores.

Os riscos da virtualização que a prova cobra são três. Primeiro, o hipervisor vira um ponto único de falha e de ataque: quem compromete o hipervisor alcança todas as máquinas virtuais dele. Por isso o acesso à console de administração do hipervisor é dos mais sensíveis do ambiente. Segundo, a proliferação descontrolada de máquinas virtuais, porque criar uma é fácil, e máquinas esquecidas ficam sem atualização. Terceiro, máquinas virtuais de níveis de sensibilidade diferentes no mesmo servidor físico, sem isolamento adequado.

Os contêineres, containers, são uma forma mais leve de virtualização, que compartilha o sistema operacional entre aplicações. Eles aparecem de novo na seção sobre tecnologias novas.

Vamos fixar com três perguntas.

Pergunta um: qual é a regra mais segura para configurar um firewall? Pense. Negar tudo por padrão e liberar só o necessário.

Pergunta dois: como se chama retirar de um servidor os serviços, portas e contas desnecessários? Pense. Endurecimento, em inglês hardening.

Pergunta três: na virtualização, qual componente, se comprometido, dá acesso a todas as máquinas virtuais? Pense. O hipervisor, hypervisor.

Na próxima seção: aplicações, bancos de dados e o ciclo de desenvolvimento de sistemas.

## Resumo

- Hardware: inventário de ativos (asset inventory), manutenção preventiva, gestão de capacidade (capacity management), relatórios de disponibilidade e problemas, descarte seguro com apagamento ou destruição.
- Redes: local (local area network) e de longa distância (wide area network). Modelo O.S.I. em sete camadas; a internet usa TCP/IP.
- Equipamentos: switch (rede local), roteador (router, entre redes), firewall (filtra tráfego), balanceador de carga (load balancer).
- Firewall: negar tudo por padrão; revisar regras; mudança de regra pela gestão de mudanças.
- Segmentação de rede (network segmentation) e zona desmilitarizada (D.M.Z.) para servidores expostos à internet. Acesso remoto por V.P.N.; redes sem fio (wireless) com criptografia forte.
- Sistema operacional (operating system): endurecimento (hardening), configuração de referência (configuration baseline), gestão de atualizações (patch management), acesso privilegiado (privileged access) restrito e registrado, logs protegidos.
- Virtualização: máquinas virtuais (virtual machines) e hipervisor (hypervisor). Riscos: hipervisor como ponto único, proliferação de máquinas, mistura de sensibilidades sem isolamento.

## Quiz

### Qual é a regra-base mais segura para um firewall?
- [ ] Liberar tudo e bloquear o que der problema
- [x] Negar tudo por padrão e liberar só o necessário
- [ ] Liberar o tráfego interno e bloquear o externo
- [ ] Deixar as regras a critério de cada área
> O padrão de negação reduz a superfície de ataque.

### Onde devem ficar os servidores acessados pela internet, como o site da empresa?
- [ ] Na rede interna, junto com os usuários
- [x] Numa zona desmilitarizada (DMZ), separada da rede interna
- [ ] Em qualquer rede sem fio
- [ ] Fora de qualquer firewall
> A DMZ isola os serviços expostos, limitando o dano de uma invasão.

### Retirar serviços, portas e contas desnecessários de um servidor é:
- [ ] Virtualização
- [ ] Balanceamento de carga
- [x] Endurecimento (hardening)
- [ ] Gestão de capacidade
> Hardening reduz o que um atacante pode explorar.

### Qual verificação o auditor faz para avaliar a gestão de atualizações (patch management)?
- [ ] Contar quantos servidores existem
- [x] Medir o tempo entre a publicação de uma correção crítica e a sua aplicação
- [ ] Verificar a marca dos servidores
- [ ] Ler o diagrama de rede
> O prazo de aplicação, por gravidade, mostra se o processo funciona.

### Na virtualização, o maior risco concentrado está em:
- [ ] Cada máquina virtual isolada
- [x] O hipervisor (hypervisor)
- [ ] O teclado do servidor
- [ ] O balanceador de carga
> Quem compromete o hipervisor alcança todas as máquinas virtuais dele.

### Um disco de servidor vai ser descartado. O controle adequado é:
- [ ] Jogar o disco no lixo comum
- [ ] Formatar rapidamente
- [x] Apagar os dados de forma segura ou destruir o disco
- [ ] Doar o disco sem verificação
> A informação não pode sair junto com o equipamento.
