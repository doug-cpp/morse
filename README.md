# MORSE

## Descrição

Esta é uma aplicação simples para decifrar [código Morse](https://ethw.org/Morse_Code), desenvolvida  nos dias 18 e 19 de novembro, com o [*framework Flask*](https://flask.palletsprojects.com/) e comunicação [*web socket*](https://html.spec.whatwg.org/multipage/web-sockets.html). Para facilitar a comunicação, foi utilizada a bibioteca [`socket.io javascript`](https://github.com/socketio/socket.io) e [`Flask-SocketIO python`](https://flask-socketio.readthedocs.io/en/latest/). Por simples, a interface do usuário também foi feita de forma básica, sem uso de *frameworks javascript* de prototipação e *design*. Apesar de ser limitado a `HTML`, `css` e `javascript` padrão, a *interface* gráfica é estética, flexível e responsiva, adaptando-se de forma fluida aos dispositivos móveis e os mais variados tamanhos e resoluções.

## Fluxo de funcionamento

Em uma janela de navegador, o usuário dispõe de apenas um input, que já se encontra em foco, no qual é instruído a digitar um código morse válido. Para auxiliar o trabalho do usuário, no canto superior esquerdo desta janela, encontra-se um botão de ajuda, que ao ser pressionado, exibirá a tabela de código morse.

Ao receber inputs do usuário, os dados são avaliados por [expressão regular](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions), de modo que um conjunto válido de pontos e traços é interpretado como código morse e separado para ser emitido para o *backend* [Python](https://www.python.org/) via *web socket* no momento em que o usuário pressionar `ENTER`.

Ao receber os dados, o *python* separa o texto em blocos de código morse, que são avaliados de acordo com um [dicionário constante](https://docs.python.org/3/tutorial/datastructures.html#dictionaries). Caso o bloco represente uma letra ou um número, este é reservado e então retornado em forma de palavra ou frase para o *frontend*. Este retorno é tratado de modo simples, sendo exibido em uma representação gráfica de um *display* virtual.

Nem todas as combinações de pontos e traços representam um código morse internacional. A combinação de quatro traços `----`, por exemplo não está prevista na [tabela padrão internacional](https://ethw.org/Morse_Code) e por isto é avaliada e tratada no *backend* com um [`ValueError`](https://docs.python.org/3/tutorial/errors.html#raising-exceptions) informativo.

## Descrição da arquitetura

### Código

Como esta aplicação foi desenvolvida em dois dias e tem o objetivo unidirecional de traduzir o código para a leitura humana, sem fazer uso de banco de dados, a opção mais interessante foi manter a simplicidade de arquitetura do código, lançando mão do *microframework Flask*, por exemplo, ao invés de frameworks mais robustos, como [Django](https://www.djangoproject.com/) e mantendo os *scripts* simples, claros, coesos, manuteníveis e separados por responsibilidade, de modo que o incremento de funcionalidades da aplicação seja perfeitamente possível sem grandes esforços.

Os testes unitários foram implementados para garantir o correto funcionamento da única inteligência da aplicação: o método tradudor.

Para servir as páginas especificadas por [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) e cuidar da comunicação entre as camadas, foi usado o [Green Unicorn - gunicorn](https://gunicorn.org/), que é um senso comum para aplicações python/web.

Para empacotar código e dependências, foi utilizado uma solução de [container Docker](https://www.docker.com/), que facilita a portabilidade de execução entre as plataformas.

### Infraestrutura

#### 1. Simples localmente

Da maneira em que a aplicação foi desenvolvida e empacotada, a mesma pode ser executada em um servidor local com uma configuração básica e um sistema operacional com o Docker instalado.

#### 2. Computação em nuvem

Para a implantação em nuvem, foi utilizado uma conta gratuita [Heroku](https://id.heroku.com), onde foi criada uma aplicação simples e implantado o container.

Por ser uma aplicação simples, ao usar a forma gratuita do Heroku, que funciona bem, porém de forma similar ao comportamento de hibernação das funções lambda.[^lambda]

## Acessando o sistema

A aplicação *web* pode ser acessada através do link: https://morse-douglas.herokuapp.com

É relevante notar o comportamento similar às funções lambda, citado no tópico anterior.[^lambda]

## Obtendo o sistema

Para testes e alterações locais, o sistema pode ser utilizado conforme instruções abaixo:

### Pré-requisitos

- Sistema operacional com compatível com o Docker;
- Docker instalado e configurado;
- Cliente git instalado e configurado.

### Instalação

Em um terminal, executa os comandos abaixo:

- `git clone git@github.com:doug-cpp/morse.git`
- `docker build -t morse-doug .`

### Execução

Em uma janela de terminal, execute o comando:

- `docker run -d --name morse-doug -p 8080:8080 morse-doug`
- Abra um navegador e acesse o link `http://localhost:8080`

---

## Arquitetura ideal

No cenário atual, as aplicações precisam contar com grande disponibilidade e um cuidado especial deve ser investido para a escalabilidade. Nos dias de hoje, apesar de óbvio, é válido salientar que contar com uma estrutura própria é algo proibitivo. Não é viável dispor de equipamentos que exigem manutenção, profissionais dedicados, disponibilidade e hardware atualizado; por isto é necessário lançar mão de serviços de nuvem, que provêem escalonamento automático do ambiente de hospedagem.

Ferramentas como o [Google App Engine](https://cloud.google.com/appengine) permitem o a criação de aplicativos altamente escalonáveis em uma plataforma totalmente gerenciada e sem servidor. Existem diversas ferramentas similares que permitem o escalonamento de aplicativos em pequena ou grande escala sem precisar se preocupar com o gerenciamento da infraestrutura.

Seja qual for o conjunto de ferramentas e serviços escolhidos, é importante ter em mente a otimização; por exemplo, escolhendo data centers de regiões estratégicas, diminuindo a latência de rede, otimizando o tamanho das mensagens, para que os usuários com restrições sejam menos afetados (uma realidade ainda presente em diversas partes do globo). Portanto, caso a aplicação seja usada por usuários finais, é necessário uma preocupação extra com dispositivos móveis, em que a maior parte dos usuários precisa lidar com a limitação de dados e velocidade de transferência, além de levar em consideração a distribuição de acessos, para que os usuários não se conectem em um só ponto.

Como processo de escalonamento, é essencial separar o monolito em conceitos de *frontend* e *backend*, para que o desenvolvimento de complexidade se torne independente e desacoplado, otimizando a manutenção do sistema.

Em alguns casos, é interessante usar o serviço RabbitMQ como message broker, para que caso o *backend* esteja *offline*, as mensagens não sejam perdidas (e ainda retorne o temido erro 500). Com o uso de serviços de mensageria, o fluxo prossegue de modo transparente e assim que o *backend* estiver operacional, as mensagens serão consumidas.

Outro ponto importante é a autenticação, forjada com mecanismos para evitar que [*bots*](https://pt.wikipedia.org/wiki/Bot) possam enviar milhares de requisições, controlando, por exemplo um número máximo de *inputs* por segundo de um mesmo usuário. O escalonamento do *backend* precisa de cuidado especial, pois enquanto o usuário requisita uma vez o *frontend* para usar a aplicação, o *backend* é requisitado várias, por exemplo, neste caso, a cada mensagem enviada.

Redis

Implementar o log detalhado para monitoramento de acessos e erros, separadamente, visando experiência de usuário,
CWV, LGPD,

Monitoramento via newrelic



log separado (aplicação) e um outro de usuários (quem entrou, quantas mensagens foram enviadas, dentre outras métricas para aprendizado contínuo de maquina)

LGPD - privacidade do usuário

Configuração de certificado SSL para prover conesão segura https para usuários (pré-requisito para ranqueamento). Poderemos até mesmo usar certificado grátis com a ferramenta let's encrypt.

Implementação de testes automatizados teste unitário e um processo de ci/cd com as ferramentas do gitlab

[^lambda]: A primeira invocação de uma função [Lambda](https://aws.amazon.com/pt/lambda/faqs/) pode ser artificialmente lenta. As invocações subsequentes não seguirão esta tendência. Este efeito é comum e até desejável, pois poupará recursos de uma máquina que está parada por inatividade. Se a mesma recebe requisições frequentes, ela responderá imediatamente, porém se está em estado de hibernação, apenas a primeira requisição servirá para que a máquina responda as próximas adequadamente.
