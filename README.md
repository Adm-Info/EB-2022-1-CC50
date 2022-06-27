# Trabajo final

## Objetivo del proyecto
El objetivo del proyecto es realizar un análisis exploratorio de los datos. Se necesitará implementar la Carga del conjunto de datos, la inspección del conjunto de datos, implementar técnicas de preprocesamiento y limpieza de datos. 
Al culminar el proyecto se necesitará dar respuesta a distintas preguntas pre definidas, a partir de los datos procesados. 

## Participantes
* Anto Chávez, Carolain Marisol
* López Takahashi, Rodrigo Andrés

## Datos
Se cuenta con 2 conjuntos de datos, el primero es un archivo csv que contiene la información respecto a los videos que estuvieron en tendencia durante noviembre del 2017 y junio 2018 en India. El segundo archivo es un JSON que contiene las diferentes categorías de los videos. 

### Archivo csv (videos en tendencia): 
* video_id: Identificador único de los videos.
* trending_date: Fecha en el que el video fue tendencia.
* tittle: Titulo del video.
* channel_tittle: Nombre del canal que publicó el video.
* category_id: Identificador de la categoría a la que pertenece el video.
* publish_time: Fecha y Hora en la que se publicó el video. 
* tags: Etiquetas puestas en el video.
* views: Cantidad de vistas en la fecha de tendencia.
* likes: Cantidad de “me gusta” en la fecha de tendencia.
* dislikes: Catidad de “no me gusta” en la fecha de tendencia.
* comment_count: Cantidad de comentarios en la fecha de tendencia.
* thumbnail_link: link del thumbnail del video.
* comments_disabled: Estado de los comentarios en el video, activados o desactivados.
* ratings_disabled: Estado de visualización de “me gusta” y “no me gusta”, activados o desactivados.
* video_error_or_removed: Indica si el video ha sido removido o no. 
* description: Descripción del video.
* state: Nombre del estado en el que el video fue publicado. 
* lat: Latitud desde la que fue publicado el video.
* lon: Longitud desde la que fue publicado el video.
* geometry: Coordenadas del estado en el que el video fue publicado. 

### Archivo JSON (categorías): 
* kind: Tipo de información.
* etag: Link que incluye este tipo de categoría
* id: identificador de la categoría
* snippet: Información de la categoría. Contiene:
  * channelId: Identificador del canal.
  * title: Titulo del tipo de categoría
  * assignable: Booleano que indica si se puede asignar la categoría a un video. 

## Conclusiones
A partir de los gráficos observados anteriormente, hemos de concluir lo siguiente:

1.	¿Qué categorías de videos son las de mayor tendencia?
En primer lugar, según las categorías de Videos, los videos de entretenimiento son los que suelen estar con mayor frecuencia en tendencia, donde en el presente caso se contabilizaron 14766 veces que esta categoría estuvo en tendencia. Esto podría ser una información de gran interés para las marcas que deseen desarrollar campañas publicitarias de posicionamiento, ya que podrían colocar su publicidad en este tipo de videos, por ejemplo, y así tener una mayor probabilidad hacerse conocidas.
 
2.	¿Qué categorías de videos son los que más gustan? ¿Y las que menos gustan?
Las categorías con mayor cantidad consistente de likes son Gaming y Pets & Animals; mientras que con menor cantidad de "me gusta", son News & Politics, Travels & Events, Education, Shows, Autos & Vehicles, Entertainment y People & Blogs y con nula cantidad de “me gusta” son Action/Adventure, Anime/Animation, Classics, Documentary, Drama, Family, Foreign, Horror, Sci-Fi/Fantasy, Short Movies, Shorts, Thriller, Trailers y Videoblogging. Respecto a ello, podría observarse que es más conveniente, en la India, crear canales de Juegos o Mascotas y animales, ya que la cantidad de likes puede indicar un mayor sentido de comunidad o de empatía con el contenido observado. También serviría a marcas que buscan asociar su nombre a un youtuber en alguna de estas categorías, ya que podrían asociar el gusto por el video con un sentimiento positivo hacia la marca.

3.	¿Qué categorías de videos tienen la mejor proporción (ratio) de “Me gusta” / “No me gusta”?
Entendiéndose como mejor aquellas categorías con una ratio de "Me gusta / No me gusta" mayor, puesto que tendrán una mayor cantidad de “Me gusta” por cada “No me gusta”, se observa que las que tienen mejor ratio son Educación, con cerca de 45 me gusta por cada no me gusta y Mascotas & Animales, con cerca de 40 me gusta por cada no me gusta. Estas categorías, al igual que la categoría anterior, pueden servir para relacionar marcas con youtubers en dichas categorías, ya que los valores positivos del youtuber en alguna de dichas categorías podrían asociarse a la marca.

4.	¿Qué categorías de videos tienen la mejor proporción (ratio) de “Vistas” / “Comentarios”?
Entendiéndose como mejor aquellas categorías con una ratio de "Vistas / Comentarios" menor (pero mayor a 1), ya que significa que por cada vista hay mayores cantidades de comentarios, se observa que las categorías Pets & Animals y Science & Technology tienen un ratio más cercana entre sí, con 212 y 362 vistas por comentarios, respectivamente. Estas categorías podrían estar más relacionadas con crear comunidad, por lo que pueden ser útiles para marcas que quieran dar a conocer más sobre algún producto, ya que los usuarios que miran dichos videos tienen mayor interés en comunicarse con el yotuber, lo que podría facilitar que también hagan preguntas sobre la marca.

5.	¿Cómo ha cambiado el volumen de los videos en tendencia a lo largo del tiempo?
El volumen de los videos en tendencia en YouTube India ha disminuido durante el periodo de Noviembre 2017 a Junio 2018. Teniendo como pico máximo diciembre de 2017.

6.	¿Qué Canales de YouTube son tendencia más frecuentemente? ¿Y cuáles con menos frecuencia?
Los canales de YouTube India, que se encuentran en tendencia más frecuentemente en durante el periodo de noviembre 2017 a Junio 2018 son:
●	VikatanTV:  con 208 días en tendencia
●	SAB TV: con 207 días en tendencia
●	ETV Plus India: con 206 días en tendencia
●	etvteluguindia: con 205 días en tendencia
●	Study IQ education: con 203 días en tendencia
Los canales con menos frecuencia son aquellos canales que solo han tenido un video en tendencia durante el periodo de tiempo. Entre estos se encuentra:
●	JackieMT 2nd
●	Pakkatv
●	TeluguZ TV
●	Empty minds
●	Telugu Trending y muchos más


7.	¿En qué Estados se presenta el mayor número de “¿Vistas”, “Me gusta” y “No me gusta”?
Los estados que presentan mayor número de vistas son:
●	Andhra Pradesh
●	Uttar Pradesh
●	Himachal Pradesh
●	Puducherry
●	Bihar
Los estados que presentan mayor número de “Me gusta” son:
●	Andhra Pradesh
●	Himachal Pradesh
●	Madhya Pradesh
●	Andaman And Nicobar
●	Bihar
Los estados que presentan mayor número de “No me gusta” son: 
●	Andhra Pradesh
●	Madhya Pradesh
●	Himachal Pradesh
●	Bihar
●	Rajasthan


8.	¿Es factible predecir el número de “Vistas” o “Me gusta” o “No me gusta”?
Con los resultados encontrados por el modelo de regresión lineal en el caso vistas con un 74% de poder predecir correctamente, se puede llegar a entender a través de los coeficientes que si se aumenta un dislike en el video, hay una posibilidad de que el video aumente en 553 views y si se da un like en el video, hay una posibilidad que el video aumente en 14 views. 
En el caso de “Me gusta”, cuenta con una predicción de 81%. Se entiende por los coeficientes que si el video recibe un dislike hay una posibilidad que el video aumente en 6 likes y si hay una vista en el video hay 0.005390 de posibilidad que deje un like.  
Por último, en el caso de “No me gusta” con una predicción de 78%. Se entiende por los coeficientes que si se aumenta una vista en el video, hay 0.000507 de que dejen un dislike. También, si se da un like en el video hay una posibilidad de 0.015218 que se deje un dislike. 

Si es factible predecir el número de Vistas, Me gusta y no me gusta con este modelo y datos porque tienen un nivel de predicción aceptable.
9.	¿Los videos en tendencia son los que mayor cantidad de comentarios positivos reciben?
Con el dataset presente, no es posible saber qué tipo de comentario reciben los videos, es por eso que la pregunta no tiene respuesta. Para ello se requeriría que el dataset tuviera una etiqueta de tipo de comentario, o en todo caso, establecer palabras clave que sirvan para clasificar el comentario; sin embargo, ello excede a los objetivos del presente proyecto.



## Licencia de uso
Este proyecto utiliza la [Licencia MIT](https://github.com/Adm-Info/EB-2022-1-CC50/blob/main/LICENSE).
