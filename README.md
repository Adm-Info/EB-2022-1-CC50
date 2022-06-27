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



## Licencia de uso
Este proyecto utiliza la [Licencia MIT](https://github.com/Adm-Info/EB-2022-1-CC50/blob/main/LICENSE).