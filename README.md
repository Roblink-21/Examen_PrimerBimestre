# Examen_PrimerBimestre

Intrucciones:

Implementar los scripts necesarios de acuerdo a la arquitectura propuesta.

Crear un repositorio de github donde se implemente mediante scripts de python cada numeral de la arquitectura de ingesta de datos. Los scripts deben llamarse “n.py” donde “n” es el # de script correspondiente. El readme del repositorio debe ser explicativo, es decir en sus palabras deben indicar cada script o proceso de forma general.

Subir el link de github al aula virtual. NO puede hacer cambios en el repositorio posterior a la hora límite.

Cualquier similitud en los comentarios del código serán considerados copia.

# Estudiante
Nombre: Roberth Pincha

# Desarrollo

- Primer ejercicio

Es necesario implementar las keys para hacer uso de los datos de twitter

![api](https://user-images.githubusercontent.com/58041699/127724373-d89526fe-eadd-47ba-9696-32ac5f798a0a.JPG)

Se estructura los metadatos

![estructura](https://user-images.githubusercontent.com/58041699/127724409-bda4b6b8-256b-47c8-b996-634a541e9ed5.JPG)

Se hace el enlace con la BD CouchDB y junto a ello creamos las BD's

![couch](https://user-images.githubusercontent.com/58041699/127724448-53e980b5-2024-4bef-b0cf-54f8c12e5628.JPG)

Usando el comando de stream podemos recoger datos de una determinada ubicacion

![localia](https://user-images.githubusercontent.com/58041699/127724474-7e4fa637-a4f8-449f-bbda-a9903ab94915.JPG)

# Evidencias 1

![Captura](https://user-images.githubusercontent.com/58041699/127724523-742764d8-5f6c-47b9-b781-5a26da9d0e01.JPG)

![Captura4](https://user-images.githubusercontent.com/58041699/127724539-f67c3890-ea1c-45aa-b502-3016856dbb88.JPG)



- Segundo Ejercicio

El segundo ejercicio es similar al anterior, la unica diferencia radica en el comando para recabar los datos. El comando "Track" nos ayuda a encontrar un elemento en especifico

![Captura4](https://user-images.githubusercontent.com/58041699/127724604-1bbfb374-7bfd-4a26-8fed-a5d305bedebc.JPG)

# Evidencias 2

![Captura](https://user-images.githubusercontent.com/58041699/127724631-5afce066-1ed9-44c6-b40f-8dc19dd57784.JPG)

![Captura2](https://user-images.githubusercontent.com/58041699/127724641-61fab770-7451-4071-bc99-d82460e8b718.JPG)

![Captura3](https://user-images.githubusercontent.com/58041699/127724648-ff9d4cdc-4523-429d-8a2f-148b7f2b6dec.JPG)


- Tercer Ejercicio



- Cuarto Ejercicio

Es necesario importar unas librerias para usar las api de facebook

![Captura3](https://user-images.githubusercontent.com/58041699/127724697-ce5776af-d56f-40fc-9c22-0e305e6fc866.JPG)

Se hace la coneccion con la BD y al mismo tiempo la seleccionamos

![Captura4](https://user-images.githubusercontent.com/58041699/127724706-755fc0cf-65af-49f5-9fc8-12645423de5a.JPG)

En esta parte del codigo empieza la formacion de la estructura json que sera formada a traves de ciertos parametros como titulo, likes, reacciones o comentarios. Ademas es necesario establecer una coneccion con una pagina de facebook, es necesario ser muy especificos en el nombre para conseguirlo

![Captura](https://user-images.githubusercontent.com/58041699/127724788-2aaa5734-0ab7-4ebf-b008-75f8cfe64e97.JPG)


![Captura5](https://user-images.githubusercontent.com/58041699/127724750-79ed2f93-aeea-4746-a7ca-f03597e911c7.JPG)

#Evidencia 4

![Captura2](https://user-images.githubusercontent.com/58041699/127724802-518d8ba7-8de3-45ab-b169-2948029305de.JPG)

![Captura6](https://user-images.githubusercontent.com/58041699/127724803-b4926ace-5588-4abb-b6b3-e621bb4b54a4.JPG)


- Quinto ejercicio
  
  El siguiente script es desarrollado en una linea de comandos de la cual solo se recogen los csv de las cuentas de tiktok
  
  ![Captura2](https://user-images.githubusercontent.com/58041699/127724845-94bd6fc2-375c-4c40-b35f-1be9cde9d644.JPG)

  Ademas, se creo una carpeta contenedora para guardarlo y posteriormente usarlas para enviar estos datos a sql lite
  
  ![Captura](https://user-images.githubusercontent.com/58041699/127724865-6a478968-ec19-4ce4-9322-28b8f2f4ecfb.JPG)
  
  ![Captura3](https://user-images.githubusercontent.com/58041699/127724887-07de9c85-795b-4c15-93d3-e8a3e7c7b583.JPG)
  
  - Proceso SQL LITE
  
  Para ello debemos importar las librerias pandas y sql.
  Ademas se debe mencionar la base de datos para hacer la coneccion con nuestro SQL LITE
  
  ![Captura4](https://user-images.githubusercontent.com/58041699/127724907-e4cf708a-24a1-4f89-9c05-3c93db3d4cfc.JPG)
  
  ![Captura5](https://user-images.githubusercontent.com/58041699/127724934-a8fc877d-4af2-4ea9-a146-088c361dad0b.JPG)

  Por ultimo, junto a la nueva bd creada en sql, enviamos los datos de csv
  
  ![Captura6](https://user-images.githubusercontent.com/58041699/127724964-60aacbbb-9b18-429a-9d0d-86375f3e1948.JPG)
  
  # Evidencia 5
  
  ![Captura7](https://user-images.githubusercontent.com/58041699/127725009-f6cfdb0b-9bd9-467a-81b6-a1a89f236443.JPG)





  
  










