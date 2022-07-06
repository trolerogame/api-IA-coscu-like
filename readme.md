# Api IA Cosculike

Este servicio está encargado de comprobar que al enviar una imagen este sea el famoso youtuber coscu.

## FUNCIONAMIENTO:

Está api tendrá una ruta de tipo "POST" en donde se podrá mandar la imagen a comprobar dentro del body de la petición, si no se le pasa la imagen y se hace la petición, este devolverá una respuesta con un status 500, y con un mensaje pidiendo la imagen.

En caso de mandar la imagen, tiene dos posibles respuestas con status 200 por parte de la api: "cocu" o "no cocu" en donde "cocu" se va a referir a qué la foto fue relacionado con coscu y "no coscu" el caso contrario.