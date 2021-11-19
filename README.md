# MORSE

## Descrição

Esta é uma aplicação simples para decifrar código Morse, desenvolvida  nos dias 18 e 19 de novembro, com o *framework Flask* e comunicação *web socket*. Para facilitar a comunicação, foi utilizada a bibioteca `socket.io javascript` e `Flask-SocketIO python`. Por simples, a interface do usuário também foi feita de forma básica, sem uso de *frameworks javascript* de prototipação e *design*. Apesar de ser limitado a `HTML`, `css` e `javascript` padrão, a *interface* gráfica é estética, flexível e responsiva, adaptando-se de forma fluida aos dispositivos móveis e os mais variados tamanhos e resoluções.

## Fluxo de funcionamento

Em uma janela de navegador, o usuário dispõe de apenas um input, que já se encontra em foco, no qual é instruído a digitar um código morse válido. Para auxiliar o trabalho do usuário, no canto superior esquerdo desta janela, encontra-se um botão de ajuda, que ao ser pressionado, exibirá a tabela de código morse.

Ao receber inputs do usuário, os dados são avaliados por expressão regular, de modo que um conjunto válido de pontos e trações é interpretado como código morse e separado para ser emitido para o backend Flask via web socket no momento em que o usuário pressionar ENTER.

Ao receber os dados, o python separa o texto em blocos de código morse, que são avaliados de acordo com um dicionário em forma de constante. Caso o bloco represente uma letra ou um número, este é reservado e então retornado em forma de palavra ou frase para o usuário. Este retorno é tratado de modo simples, sendo exibido em uma representação gráfica de um display virtual.

Nem todas as combinações de pontos e traços representam um código morse internacional. A combinação de quatro traços `----`, por exemplo não está prevista na [tabela padrão internacional](https://ethw.org/Morse_Code) e por isto é avaliada e tratada no *backend* com um [`ValueError`](https://docs.python.org/3/tutorial/errors.html) informativo

## Descrição da arquitetura

Como esta aplicação foi desenvolvida em dois dias e tem o objetivo único de traduzir o código para a leitura humana, sem fazer uso de banco de dados, a opção mais interessante foi manter a simplicidade de arquitetura, lançando mão do Flask, por exemplo, ao invés do Django e mantendo os scripts simples, claros, coesos e manuteníveis, de modo que um aumento de responsibilidade da aplicação seja perfeitamente possível sem grande esforço.

## O mundo real

No cenário atual, as aplicações precisam contar com grande disponibilidade e um cuidado especial deve ser investido para a escalabilidade. Nos dias de hoje, apesar de óbvio, é válido salientar que contar com uma estrutura própria é algo proibitivo. Não é viável dispor de equipamentos que exigem manutenção, profissionais dedicados, disponibilidade e hardware atualizado; por isto é necessário lançar mão de serviços de nuvem, que provêem de forma otimizada etc...

Seja qual for o conjunto de ferramentas e serviços escolhidos, é importante ter em mente sempre a otimização; por exemplo, escolhendo data centers de regiões estratégicas, diminuindo a latência de rede, otimizando o tamanho das mensagens, para que os usuários com restrição de dados e velocidade sejam menos afetados (uma realidade ainda presente em diversas partes do globo).
