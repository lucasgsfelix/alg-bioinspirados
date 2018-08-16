contador=0
while [ $contador -lt 100 ]; do 
	python algoritmoGenetico.py 1 saida1.txt
	let contador=contador+1;

done
