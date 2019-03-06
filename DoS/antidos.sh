#!/bin/bash

BLOCK_COUNT=1
BLOCK_IP=2

change(){
	BLOCK_COUNT=$((2+$BLOCK_COUNT))
	BLOCK_IP=$((2+BLOCK_IP))
	COUNT=`echo $IP_LIST | awk '{print $var}' var="${BLOCK_COUNT}"`
}


anti_dos(){
	IP_LIST=`netstat -an | grep :80 | awk {'print $5'} | cut -d: -f 1 | sort | uniq -c | sed -ne '2,10p' | sort -r`
	COUNT=`echo $IP_LIST | awk '{print $var}' var="${BLOCK_COUNT}"`

	while [[ $COUNT -ge 20 ]]; do
	 	echo -e "\nSeguinte IP BLOQUEADO:"
		IP_BLOQUEADO=`echo $IP_LIST | awk '{print $var}' var="${BLOCK_IP}"`
		echo $IP_BLOQUEADO
		echo "Pelo número de requisições:"
		echo $COUNT
		date "+%H:%M:%S %d-%m-%Y"
		iptables -I INPUT -s $IP_BLOQUEADO -j DROP
		
		change
	 done
	
	sleep 5
	echo -e "\nNenhuma tentativa de DoS foi detectada"
	echo -e "Valor máximo de requisições:"
	echo $COUNT
	date "+%H:%M:%S %d-%m-%Y"
	BLOCK_COUNT=1
	BLOCK_IP=2
	sleep 5


	anti_dos
}

anti_dos

