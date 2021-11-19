# MORSE

## Descrição

Esta é uma aplicação simples para decifrar código Morse, desenvolvida  nos dias 18 e 19 de novembro, com o *framework Flask* e comunicação *web socket*. Para facilitar a comunicação, foi utilizada a bibioteca `socket.io javascript` e `Flask-SocketIO python`. Por simples, a interface do usuário também foi feita de forma básica, sem uso de *frameworks javascript* de prototipação e *design*. Apesar de ser limitado a `HTML`, `css` e `javascript` padrão, a *interface* gráfica é estética, flexível e responsiva, adaptando-se de forma fluida aos dispositivos móveis e os mais variados tamanhos e resoluções.

## Fluxo de funcionamento

Em uma janela de navegador, o usuário dispõe de apenas um input, que já se encontra em foco, no qual é instruído a digitar um código morse válido. Para auxiliar o trabalho do usuário, no canto superior esquerdo desta janela, encontra-se um botão de ajuda, que ao ser pressionado, exibirá a tabela de código morse.

Ao receber inputs do usuário, os dados são avaliados por expressão regular, de modo que um conjunto válido de pontos e trações é interpretado como código morse e separado para ser emitido para o backend Flask via web socket no momento em que o usuário pressionar ENTER.

Ao receber os dados, o python separa o texto em blocos de código morse, que são avaliados de acordo com um dicionário em forma de constante. Caso o bloco represente uma letra ou um número, este é reservado e então retornado em forma de palavra ou frase para o usuário. Este retorno é tratado de modo simples, sendo exibido em uma representação gráfica de um display virtual.

Nem todas as combinações de pontos e traços representam um código morse internacional. A combinação de quatro traços `----`, por exemplo não está prevista na [tabela padrão internacional](https://ethw.org/Morse_Code) e por isto é avaliada e tratada no *backend* com um [`ValueError`](https://docs.python.org/3/tutorial/errors.html) informativo
