# Api IA Cosculike

Este servicio está encargado de comprobar que al enviar una imagen este sea el famoso youtuber coscu.

## FUNCIONAMIENTO:

Está api tendrá una ruta de tipo "POST" en donde se podrá mandar la imagen a comprobar dentro del body de la petición


### Respuesta negativa

si no se le pasa la imagen y se hace la petición, este devolverá una respuesta con un status 500, y con un mensaje pidiendo la imagen.

```json
    {
        "error":"text"
    }
```


### Respuesta Positiva

En caso de mandar la imagen, enviara un status 200 y enviara un json con el atributo "isCoscu"; Dependiendo de si la imagen es coscu o no devolvera un true o un false

```json
    {
        "isCoscu": true || false // dependera de si la imagen coincide con coscu o no
    }
```