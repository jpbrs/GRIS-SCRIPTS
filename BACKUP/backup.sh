#!/bin/bash


DIRETORIO_ORIGEM="/home/joao/Desktop/biblioteca_teste_python_jpbrs/" 
DIRETORIO_DESTINO="/home/joao/Desktop/BACKUP/BackupDiretoriobiblioteca_teste_python_jpbrs/"



cria_backup(){

	BACKUP=`date +%Y%m%d`.tgz

	tar -czpf ${DIRETORIO_DESTINO}${BACKUP} ${DIRETORIO_ORIGEM}

	echo "Seu backup foi realizado com sucesso";

	for i in `ls $DIRETORIO_DESTINO*.tgz`
	do
		DATA_I=`echo $i | cut -d. -f 1 | rev | cut -c1-8 | rev`
		DIAS=`date -d "-3 days" "+%Y%m%d"`


		if [[ $DATA_I -le $DIAS ]]
		then
			rm $i
		fi
	done

}

cria_backup




