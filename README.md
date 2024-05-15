 # 👋 Hola, soy Nicolas! Analsita de datos de Colombia 🇨🇴.
 
## ¡Bienvenido a mi proyecto! ¿Mucha lectura? Aqui te dejo los resultados:
[Video de resultados](https://www.youtube.com/watch?v=dCRVrCM1ABQ&ab_channel=NicolasSuarez)

# Bibliotecas Phython y herramientas de visualización de datos

 👋 Hola, soy Nicolas! Analsita de datos de Colombia 🇨🇴.
En este escenario vamos a estar revisando un caso de una empresa brasileña que tiene un problema con las entregas!
Vamos a averiguar por que?!

Utilizamos las siguietes librerias:

- 🐼 PANDAS
- 📏 MATPLOTLIP
- 🌊 SEABORN
- 💣 PLOTY
- 📝 REPORTLAB




[📨 Envíame un mail →](mailto:javinsuarez@gmail.com)

[🤙 Llámame →](tel:+573052621201)

[📝 My CV →](https://www.canva.com/design/DAF7qCO6_Ps/4bLraC9rscY7VLZ4nPdvmQ/view?utm_content=DAF7qCO6_Ps&utm_campaign=designshare&utm_medium=link&utm_source=editor)

## PANDAS 🐼
El notebook 📑 https://drive.google.com/file/d/16dNwyTIjXHQv_huVnkGJCt_lvacFNnfW/view?usp=drive_link

La data 📦 https://drive.google.com/file/d/1U4lal8Ztw1lQmukoZN2vDaFgPVc1DWuq/view?usp=drive_link

### La idea

---

- La ides es empezar a tener el ritmo de las librerias de python, que ayudan a modelar datos empezando por los mas faciles los CSV

### Problemas

---

- ⚠️ La idea era utilizar Jupter desde chorme pero se me dificulto entonces voy a utilizar VSC = Visual Studio Code, estoy mas familiarizado con esta: para colocar la ruta de la carpeta pongo una ‘r’ antes de la ruta para que entienda que es un path, todo se soluciono corrigiendo las rutas del PATH
⚠️ Hay otro problema, es que habia una ruta repetida, ademas se soluciono el problema con el motor ‘engine=openpyxl’

### Aprendizajes

---

📘 La funcion parsel_dates es nueva: asi que investigar un poco, creo que es un parametro del JOIN, otra cosa; el OS facilita mucho lo del PATH que normalemente es un poco engorroso

📘 Otro operador muy util es el .unique() que sirve para saber con que variable categorica podemos nos podemos familiarizar, valor.count() lo mismo y nos dice cuantas vecez esta repetida esa variable categorica

📘 Para seleccionar más de una columna, se necesita usar un doble corchete ([['column1', 'column2']]). si solo se queire una un solo corchete es suficiente o el df.nombre_de_Columna

📘El metodo .query es de los mas utiliz a la hora de hacer un dataframe mas especifico a nuestra necesidad

## SEABORN 🚢
### Aprendizajes:

---

📘 Percentil vs Porcentaje: el percentil es como se comporta un valor en una lista de valores ejemplo: si un estudiante esta en el percentil 90 de un examen quiere decir que esta sobre el 90% de las calificaciones. ¿como para que me servira esto? Aqui podemos sacar .mean para saber en que posicion esta el promedio. 

📘 Historiogramas: sirven para saber cuantas veces se repite un valor dentro de un grupo de valores. bins = cantidad de particiones en los que se agruparan los datos (en uso practico entre menos bins se usen mas agrupada se vera la grafica) 

📘 Variable **hue** :es uno de los parametros mas bellos a la hora de generar graficos ya que separa visualmente las variables categoricas

## RETOS

**⚠️ No logre hacer el ultimo grafico ya que queda muy pegado los estados y no es apreciable :’(** 

✅ Ya lo logre lo que hice fue cambiar el ,hue= ‘geolocation_state’ ☺️

## EX - PLOTY 💥

### Descargas

🌐[3_e_map_long_delays_by_state.html](https://drive.google.com/file/d/145uD3qPc-tRlp-o1beHy9aKi3kUCaA31/view?usp=sharing), 

🌐[3_d_evolution_delayed_orders_by_region.html](https://drive.google.com/file/d/18xuaHi__ckgdW_gEjahV4oihDaZ6PWWr/view?usp=sharing),

📒 [3_e_map_long_delays_by_state.py](https://drive.google.com/file/d/19y4feNV3QBuwNkRBJivcybT8Jacyq04t/view?usp=sharing)

 🌐[3_d_evolution_delayed_orders_by_quarter.html](https://drive.google.com/file/d/1juTG5_J3WKE6rNzYKYS3tMH02oonTz6Y/view?usp=sharing)

 📒[3_d_evolution_delayed_orders_by_region.py](https://drive.google.com/file/d/1uODWqVzMvm9LXVoQtVj-TJGr2zmEVRB_/view?usp=sharing)

## **Problemas**

⚠️ EL .iloc[cordenadas de los datos] Siempre me salva a la hora de hacer un print de un dato especifico, aunque, creo que se podria mejorar por medio de una función para no tener que buscar la coordenada del dato especifico 

⚠️ En el entregable 3_d, el nombre dice que es por .region, pero en la descripcion del scrip no menciona hacerlo con la region… ⁉️

## **Aprendizajes**

📘 Ploty es una herramienta que viene de un API que tiene una forma de escritura parecida a 🌊seaborn🌊

📘 siempre que utilices un groupby tienes que ponerle una operaciones sino el resultado sera <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000024FE56C5120>

📘 Para lograr hacer la escala de color hay que darse cuenta de que el tipo de dato de la columna color = ‘delay_status’ debe ser  un “int”


## Automatización del informe 🤖
# Descarga el informe:

👨🏻‍💻
`https://drive.google.com/uc?id=1VSubyPUWjCd05sg9cItFbVrtqli7yR90&export=download`

### ⚠️ Alertas ⚠️

⚠️Creo que este es el modulo que mas aprendizajes me va aportar ya que nunca he automatizado reportes

⚠️ No se como agregar imagenes a las dispostivas, por que no quiero exportarlas quiero traerlas directamente de python, utilizando ploty no me deja integrarlas:

✅ Se soluciono instalando el paquete kaleido globalmente

⚠️  Uno gran problema es que la unica manera de ver archivos en htlm es en el navegador, como no se mueven en el pdf, voy a agregar un enlace donde se puedan ver en HTLM la situación es que tengo problemas por que no se ve el enlace.

✅ Lo solucionamos con el posicionamiento del eje Y **(y_position = 100)** por que este es un gran tema, intentamos de todo mas de 2 horas intentando colocar un link 🫠🫠 la Y position es una variable muy importante.

### 🚨 Cosas que debes prestar atención 🚨

🚨 Dependiendo de que tanto porcentaje del reporte se quiere automatizar, se debe tener en cuenta varios aspectos:

1️⃣ Formato el reporte 

2️⃣Tienes todo lo que quieres agregar en el reportes ya programado?

3️⃣ Estan dentro del mismor documento python? (que ya veremos si es lo mejor)

4️⃣En que formato estan las imagenes 

5️⃣ DONDE ESTA LA INFORMACIÓN: se me complico mucho

### 📘 Aprendizajes 📘

📓 Prototipo_1: No cargaban las demas hojas ✅ Faltaba una coma en cada hoja del codigo. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e255b425-fa14-4ecc-88cb-03b1145af889/abf1a093-08d4-461c-bab1-a42a399cea61/4df403d5-c951-42cd-b351-3302218dd918.png)

📓 Prototipo_2: Primera imagen 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e255b425-fa14-4ecc-88cb-03b1145af889/fea97f35-6e74-4f99-94a5-d440968e24a0/Untitled.png)

📓 Prototipo_3

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e255b425-fa14-4ecc-88cb-03b1145af889/4da17076-43e0-4816-a70a-24f28005d03d/Untitled.png)

📓 Prototipo_ 4 ( no hago viz que se muevan para mostrarlas quietas) Agregamos link de descarga para moverlas & corregimos el eje_X para que salga mas adentro de la imagen

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e255b425-fa14-4ecc-88cb-03b1145af889/98cf5a71-92fc-49e0-a361-9a9d41e2de6c/Untitled.png)

📘 LAS HOJAS DE PDF TIENES QUE VERLAS COMO UN PLANO DONDE SE MUEVE TODO POR EJE_X Y EJE_Y, si contralos eso puedes poner cada cosa en su lugar para que se vea bien 

📘 **Usa barras diagonales inversas o dobles:** Dependiendo del sistema operativo que estés usando, es posible que necesites usar barras diagonales inversas (**`\`**) o barras diagonales dobles (**`\\`**) en lugar de barras diagonales normales (**`/`**) en la ruta de la imagen.

😊 Con esto terminamos la plantilla que queremos del informe 😊

# 🚧Conclusion de reporte

La creación de un modelo de reporte es importante pero la interpretación de la información esta relaciónada con un ser vivo en este caso un humano 🫀

[5_reporte_brasil_ia_consulting.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/e255b425-fa14-4ecc-88cb-03b1145af889/f07420a7-cc06-418b-bc74-39c997650846/5_reporte_brasil_ia_consulting.pdf)

Agrego el codigo de la automatización espero seguir trabajando para automatizar mas los reportes!!!
