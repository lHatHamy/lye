# Bot con uso de Expresiones Regulares: Guajolotes Rosita

Durante la pandemia en mi localidad, la demanda de un platillo tradicional conocido como "guajolote" hizo que varios vendedores de comida se adaptaran al uso de nuevas tecnologías para realizar pedidos en linea. Telegram fue alguna de las mas usadas para realizar estos pedidos. Sin embargo, la toma de pedidos podría demorar debido a que aun siendo digital, se leía el mensaje de forma manual. Una forma de agilizar esto podría ser mediante una expresión regular que filtre los mensajes y pueda guardar la orden solamente.

## Uso de la expresión regular

A continuación mostraremos la expresión regular usada:

"([0-9]*\s[G|g]uajolote[s]?\s(de|con)\s?(pollo|salchicha|pierna|queso)\s?(y|con)*(\squeso|\ssalchicha|\spierna|\spollo)*)"

Mediante esta expresión podremos filtrar la orden de los clientes ignorando el resto del mensaje, tomando en cuenta 4 ingredientes y que de estos solo pueden escogerse hasta 2.  A continuación mostraremos algunos ejemplos ya aplicados en nuestro bot de telegram.

![rsbot1](https://github.com/lHatHamy/lye/assets/160956856/69c4f1af-571f-428c-b936-6fba3c0e8934)

En este ejemplo colocamos dos mensajes que cumplen las condiciones antes mencionadas. Cabe recalcar que en caso de querer realizar un pedido con cantidades, será necesario ingresar un caracter numerico para indicar la cantidad. En caso de no tenerlo se tomará en cuenta como solo uno.

![rsbot2](https://github.com/lHatHamy/lye/assets/160956856/858efec5-32c7-4b1a-b855-26bbfbc04086)

En este otro ejemplo mostramos dos casos de uso incorrecto, en los cuales la orden está mal redactada. También demostramos que gracias a nuestra expresión, solo es necesario que la orden esté escrita como lo pedimos; por lo que el resto de mensaje no importa como sea escrito.


## Conclusión

Mediante esta practica mostramos un pequeño ejemplo de como usar las expresiones regulares, asi como con una pequeña busqueda concreta podría no solo ayudarnos en la parte de automatas; sino que puede tener un aplicativo en aplicaciones de la vida diaria. Este proyecto podría tener una escalabilidad mayor a otras tiendas, por lo que demostramos que la utilidad de las expresiones no solo se queda a un nivel bajo en programación.


--Uriel Alberto Serrano González
--21200630
