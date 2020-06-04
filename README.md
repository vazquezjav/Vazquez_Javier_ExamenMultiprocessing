# Examen Computacion Paralela 
## MPI
**Comando :** $ mpiexec -n 10 python Vazquez_Javier_ExamenMPI..py
![Alt text](Imagenes/mpiexec.PNG?raw=true "Mpi Ejecucion")

Para MPI se dividio la lista de acuerdo al N numero de procesos, esto menos uno, ya que el procesos 0 o Master envia cada pedazo de la Matriz
a cada uno de los demas procesos o trabajadores, algo similar a lo que fuera un scatter, el procesos 0 quedara en espera de del resultado de 
uno de los procesos desde n-1. Para enviar los fragmentos de la lista se utiliza un bucle que nos ayudara a enviar la data a cada "proceso" 
por lo que se divio por rangos procurando que cada proceso trabaje con las mismas antidades de filas 
Para los trabajadores estan en espera hasta que reciban el fragmento de la matriz, ya recibido los datos se realiza el mismo proceso que en 
el secuencial contar los numeros que se encuentran entre un rango especifico. Una vez procesado todo esto se ele envia al proceso 0 (raiz)
el cual se encuentra en espera. Mediante un bucle recupera todos los reultados de los trabajadores uniendolos en una sola lista 
![Alt text](Imagenes/mpiCode.PNG?raw=true "Mpi Code")
## Multiprocessing
Para el multiprocessing tambien se realizo por lotes, mismo metodo que el secuencial a diferencia que todo esto se encuentra dentro de una clase multiprocessing, a esta clase se le pasa como parametro una cola la cual se va a encargar de recuperar el valor que retorna la funcion de contar los numeros entre un rango, en el main se une este valor que retorn la clase iterando la cola y agregando este valor a una lista final.
