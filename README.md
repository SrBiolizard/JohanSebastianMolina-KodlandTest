<h1 align="center"> Bienvenid@ a mi test </h1>

Soy Johan Sebastian Molina y quiero que conozcas el clasico juego Space Invader en lenguaje de programación Python haciendo uso de la librería PyGame

![Captura de pantalla 2023-06-23 053647](https://github.com/SrBiolizard/JohanSebastianMolina-KodlandTest/assets/72704984/1f3c6081-3b0c-4b5f-8309-f04dfef432c0)

En este juego tendrás como objetivo no morir acumulando la mayor cantidad de puntos al dispararle a los enemigos
<h3>¿Cómo generar mas puntos?</h3>

Cuida tu barra de vida y sobre todo lo mas importante ¡Acaba con la mayor cantidad de enemigos posibles!
![Captura de pantalla 2023-06-23 054037](https://github.com/SrBiolizard/JohanSebastianMolina-KodlandTest/assets/72704984/13e8d81c-8ea7-4293-bf8d-061634731031)

El desplazamiento dentro del mapa es sencillo las flechas de tu teclado indican la dirección que tomarás
![2491500](https://github.com/SrBiolizard/JohanSebastianMolina-KodlandTest/assets/72704984/6ebe1f7e-6419-4afe-818f-74d87fb783e7)
Lo mas divertido es que puedes disparar con cualquier tecla permitiendo que puedas hacerlo muchas veces por segundo

\## 📁 Acceso al proyecto

**¿Y si juegas un poco antes de codificar?**

Debes descargar Python en tu sistema y algún entonrno de desarrollo para correr los programas facilmente o si prefieres cualquier editor de texto te permite ejecución desde consola

\## 🛠️ Abre y ejecuta el proyecto

Te recomiento empezar con tener esta versión de python o superior
![Captura de pantalla 2023-06-23 060809](https://github.com/SrBiolizard/JohanSebastianMolina-KodlandTest/assets/72704984/1561e263-9c9d-41d8-8a11-c55209546045)

¿No cuentas con un entorno de desarrollo que te facilite la compilación?
No te preocupes, puedes leer esta guía super facil, espero te sirva https://www.mclibre.org/consultar/python/otros/python-uso.html

Vamos a codificar un poco

el codigo se encuentra medianamente comentado, cuenta con 6 clases Enemigos,Jugador,Jefe,Explosion,Balas_enemigos,Balas y 5 metodos externos a esta clases
cada clase tiene sus metodos nombrados con el objetivo que pueda ser intuitivo conocer su funcionalidad.

La clase jugador me define atributos de la entidad jugador cuenta con los metodos para inicializarse, actualizarse y un tercer metodo disparar en proceso de mejora pensando en futuros desarrollos
La clase enemigo me defino atributos de las entidades enemigos, esta clase cuenta con los mismos metodos de jugador pero adaptadas
La clase jefe define atributos de una entidad que aparece cada cierta cantidad de enemigos muertos, esta cuenta con los mismos metodos y uno extra a favor de una futura implementación y darle atributos mejorados al jefe como super resistencia
Las dos clases de balas tanto la enemigo como jugador son muy similares, entre ellas cambian algunos parametros lo cuales permiten que hagan lo esperado
La clase explosión por ultimo se encarga de la animación cuando la nave recibe daño, esta toma una serie de fotografías las enlista y pintando una sobre la otra genera una animación

<h4 align="center">
:construction:Recuerda que hay dos funcionalidades con posible mejora ¡Vamos animate!:construction:
</h4>


