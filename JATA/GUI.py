from flet import *
import plotly.express as px
from flet.plotly_chart import PlotlyChart
from Red import Red
import random
import tkinter as tk
from tkinter import filedialog
import numpy as np



def ui(page: Page):
    datos=[0,0,0,0,0]
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"
    numeroEntradas = Text(value=datos[0], style="displaySmall",text_align="center",color="GREY800",weight="bold")
    numeroSalidas = Text(value=datos[1], style="displaySmall",text_align="center",color="GREY800",weight="bold")
    numeroPesos = Text(value=datos[2], style="displaySmall",text_align="center",color="GREY800",weight="bold")
    numeroUmbrales = Text(value=datos[3], style="displaySmall",text_align="center",color="GREY800",weight="bold")
    numeroPatrones = Text(value=datos[4], style="displaySmall",text_align="center",color="GREY800",weight="bold")
    #red = Red(tasaAprendizaje,iteraciones,funcionActivacion,errorPermitido)


    funcionActivacion=Dropdown(
        border_radius=5,
        scale=0.7,
        text_size=20,
        width=300,
        color=colors.GREY_800,
        border_color=colors.GREY_800,
        bgcolor=colors.WHITE,
        label="funcion de activacion",
        hint_text="Por favor seleccione",
        options=[
            dropdown.Option("Adalaine"),
            dropdown.Option("Perceptron",)
        ],
        autofocus=True
    )
    iteraciones = TextField(
        label="Seleccione el numero de iteraciones",
        border_radius=5,
        scale=0.65,
        text_size=20,
        width=340,
        color=colors.GREY_800,
        border_color=colors.GREY_800,
        bgcolor=colors.WHITE,
    )
    errorPermitido = TextField(
        label="Seleccione el error permitido",
        border_radius=5,
        scale=0.65,
        text_size=20,
        width=320,
        color=colors.GREY_800,
        border_color=colors.GREY_800,
        bgcolor=colors.WHITE,
    )
    tasaAprendizaje = TextField(
        label="Seleccione la rata de aprendizaje",
        border_radius=5,
        scale=0.65,
        text_size=20,
        width=340,
        color=colors.GREY_800,
        border_color=colors.GREY_800,
        bgcolor=colors.WHITE,
    )
    botonEntrenar=ElevatedButton(
        on_click= lambda e: entrenarRed(e),
        bgcolor=colors.GREEN_600,
        color="white",
        style=ButtonStyle(
            shape={
                MaterialState.HOVERED: RoundedRectangleBorder(radius=20),
                MaterialState.DEFAULT: RoundedRectangleBorder(radius=5),
            },
        ),
        content=Row(
            controls = [
                Icon(name=icons.UPDATE,
                size=20,
                ),
                Text(
                    "Entrenar",
                    size=15,
                    weight="bold"
                )
            ]
        )
    )

    simular=ElevatedButton(
        on_click= lambda e: entrenarRed(e),
        bgcolor=colors.GREEN_600,
        color="white",
        style=ButtonStyle(
            shape={
                MaterialState.HOVERED: RoundedRectangleBorder(radius=20),
                MaterialState.DEFAULT: RoundedRectangleBorder(radius=5),
            },
        ),
        content=Row(
            controls = [
                Icon(name=icons.PLAY_ARROW,
                size=20,
                ),
                Text(
                    "Simular",
                    size=15,
                    weight="bold"
                )
            ]
        )
    )

    df = px.data.gapminder().query("continent=='Oceania'")
    fig = px.line(df, x="year", y="lifeExp", color="country")
    red = Red(tasaAprendizaje,iteraciones,funcionActivacion,errorPermitido)

    def entrenarRed(e):

        red.patterns_according_to_interactions(funcionActivacion.value,float(tasaAprendizaje.value),float(errorPermitido.value),int(iteraciones.value))
        
    
    #Cargar Datos
    def cargarDatos(e: FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        if(selected_files != "Cancelled"):
            red.file_upload(selected_files.value)
            datos[0]=red.numeroEntradas
            numeroEntradas.value = (datos[0])
            numeroEntradas.update()
            datos[1]=red.numeroSalidas
            numeroSalidas.value = (datos[1])
            numeroSalidas.update()
            datos[2]=red.numeroSalidas * red.numeroEntradas
            numeroPesos.value = (datos[2])
            numeroPesos.update()
            datos[3]=red.numeroSalidas
            numeroUmbrales.value = (datos[3])
            numeroUmbrales.update()
            datos[4]=len(red.patrones[0])
            numeroPatrones.value = (datos[4])
            numeroPatrones.update()
        

    pick_files_dialog = FilePicker(on_result=cargarDatos)
    selected_files = Text()
    

    #
    subirDatos=ElevatedButton(
        bgcolor=colors.GREEN_600,
        color="white",
        style=ButtonStyle(
            shape={
                MaterialState.HOVERED: RoundedRectangleBorder(radius=20),
                MaterialState.DEFAULT: RoundedRectangleBorder(radius=5),
            },
        ),
        content=Row(
            controls = [
                Icon(name=icons.UPLOAD_FILE,
                size=20,
                ),
                Text(
                    "Subir datos",
                    size=15,
                    weight="bold"
                )
            ]
        ),
        on_click= lambda _: pick_files_dialog.pick_files(allow_multiple=True),
    )

    page.overlay.append(pick_files_dialog)
    # add controls on Page
    page.add(
        Row(
            controls=[
                Container(
                    expand=1,
                    bgcolor=colors.GREY_100,
                    height=800,
                    padding=padding.only(top=30, left=30),
                    content=Column(
                        scroll=True,
                        controls=[
                            Text("JATA", style="headlineMedium", color="GREY800",weight="bold"),
                            Text("Bienvenido aqui pordrás entrenar tu red neuronal con tan solo unos simples pasos.", style="bodySmall", color="GREY800"),
                            Container(
                                border=border.all(2, colors.GREY_300),
                                bgcolor=colors.WHITE,
                                width=1190,
                                height=200,
                                #margin=margin.only(right=20),
                                padding=padding.only(left=20,top=10),
                                border_radius=12,
                                content=Column(
                                    
                                    controls=[
                                        Text("Datos", style="headlineSmall", color="GREY800",weight="bold"),
                                        Text("Caracteristicas de los datos ingresados.", style="bodySmall",color="GREY800"),
                                        Row(
                                            alignment=alignment.top_left,
                                            controls=[
                                                Container(
                                                    #margin=margin.symmetric(horizontal=30, vertical=16),
                                                    border=border.all(2, colors.GREY_300),
                                                    border_radius = 12,
                                                    bgcolor=colors.WHITE,
                                                    padding=padding.only(left=30),
                                                    width=220,
                                                    height=100,
                                                    content=Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        controls=[
                                                            numeroEntradas,
                                                            Text("Numero de entradas", style="bodySmall",color="GREY800")
                                                        ],
                                                    ),
                                                ),
                                                Container(
                                                    #margin=margin.symmetric(horizontal=30, vertical=16),
                                                    border=border.all(2, colors.GREY_300),
                                                    border_radius = 12,
                                                    bgcolor=colors.WHITE,
                                                    padding=padding.only(left=30),
                                                    width=220,
                                                    height=100,
                                                    content=Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        controls=[
                                                            numeroSalidas,
                                                            Text("Numero de salidas", style="bodySmall",color="GREY800")
                                                        ],
                                                    ),
                                                ),
                                                Container(
                                                    #margin=margin.symmetric(horizontal=30, vertical=16),
                                                    border=border.all(2, colors.GREY_300),
                                                    border_radius = 12,
                                                    bgcolor=colors.WHITE,
                                                    padding=padding.only(left=30),
                                                    width=220,
                                                    height=100,
                                                    content=Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        controls=[
                                                            numeroPesos,
                                                            Text("Numero de Pesos", style="bodySmall",color="GREY800")
                                                        ],
                                                    ),
                                                ),
                                                Container(
                                                    #margin=margin.symmetric(horizontal=30, vertical=16),
                                                    border=border.all(2, colors.GREY_300),
                                                    border_radius = 12,
                                                    bgcolor=colors.WHITE,
                                                    padding=padding.only(left=30),
                                                    width=220,
                                                    height=100,
                                                    content=Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        controls=[
                                                            numeroUmbrales,
                                                            Text("Numero de umbrales", style="bodySmall",color="GREY800")
                                                        ],
                                                    ),
                                                ),
                                                Container(
                                                    #margin=margin.symmetric(horizontal=30, vertical=16),
                                                    border=border.all(2, colors.GREY_300),
                                                    border_radius = 12,
                                                    bgcolor=colors.WHITE,
                                                    margin=margin.only(right=30),
                                                    padding=padding.only(left=30),
                                                    width=220,
                                                    height=100,
                                                    content=Column(
                                                        alignment=MainAxisAlignment.CENTER,
                                                        controls=[
                                                            numeroPatrones,
                                                            Text("Numero patrones", style="bodySmall",color="GREY800")
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ),
                            Row(
                                controls=[
                                    Container(
                                        padding=padding.all(20),
                                        border=border.all(2, colors.GREY_300),
                                        border_radius = 12,
                                        bgcolor=colors.WHITE,
                                        height=420,

                                        #margin=margin.only(left=30,top=30),
                                        content=Column(
                                            controls=[
                                                Text("Parametros", style="headlineSmall", color="GREY800",weight="bold"),
                                                Text("Por favor selecciones los parametros que desea utilizar para el entrenamiento.", style="bodySmall", color="GREY800"),
                                                Row(
                                                    controls=[
                                                        Container(
                                                            margin=margin.only(top=10,left=-45),
                                                            height=70,
                                                            content=funcionActivacion
                                                        ),
                                                        Container(
                                                            margin=margin.only(top=4,left=-45),
                                                            height=70,
                                                            content=iteraciones
                                                        ),
                                                    ]
                                                ),
                                                Row(
                                                    controls=[
                                                        Container(
                                                            margin=margin.only(top=-15,left=-55),
                                                            height=70,
                                                            content=errorPermitido
                                                        ),
                                                        Container(
                                                            margin=margin.only(top=-15,left=-55),
                                                            height=70,
                                                            content=tasaAprendizaje
                                                        ),
                                                    ]
                                                ),
                                                Row(
                                                    controls=[
                                                        Container(
                                                            margin=margin.only(bottom=30,left=40),
                                                            height=40,
                                                            content=botonEntrenar
                                                        ),
                                                        Container(
                                                            margin=margin.only(bottom=30,left=150),
                                                            height=40,
                                                            content=subirDatos
                                                            
                                                        ),
                                                    ]
                                                ),selected_files
                                            ]
                                        )
                                    ),
                                    Container(
                                        padding=padding.all(20),
                                        border=border.all(2, colors.GREY_300),
                                        border_radius = 12,
                                        bgcolor=colors.WHITE,
                                        width=576,
                                        height=420,
                                        content=Column(
                                            controls=[
                                                Text("Salidas", style="headlineSmall", color="GREY800",weight="bold"),
                                                Text("Estos son las salidas actuales en comparacion con las esperadas.", style="bodySmall", color="GREY800"),
                                                Container(
                                                    width=510,
                                                    height=500,
                                                    margin=margin.only(top=-90),
                                                    padding=padding.all(20),
                                                    content=PlotlyChart(fig, expand=True)
                                                )
                                            ]
                                        )
                                    ),
                                ],
                            ),
                            Row(
                                controls=[
                                    Container(
                                        border=border.all(2, colors.GREY_300),
                                        bgcolor=colors.WHITE,
                                        width=1190,
                                        height=220,
                                        padding=padding.only(left=20,top=10),
                                        margin=margin.only(bottom=20),
                                        border_radius=12,
                                        content=Column(
                                            alignment=alignment.center,
                                            controls=[
                                                Container(
                                                    margin=margin.only(top=10),
                                                    content=Text("Resultados", style="headlineSmall", color="GREY800",weight="bold")
                                                ),
                                                Container(Text("Observe los resultados del entrenamiento.", style="bodySmall",color="GREY800")),
                                                
                                                Row(
                                                    controls=[
                                                    Container(
                                                        margin=margin.only(top=-60,left=1010),
                                                        padding=padding.only(bottom=20),
                                                        height=30,
                                                        content=simular
                                                        ),
                                                    ]
                                                ),
                                                Row(
                                                    alignment=alignment.center,
                                                    controls=[
                                                        Container(
                                                            margin=margin.symmetric(horizontal=70),
                                                            border=border.all(2, colors.GREY_300),
                                                            border_radius = 12,
                                                            bgcolor=colors.WHITE,
                                                            padding=padding.only(left=30),
                                                            width=220,
                                                            height=100,
                                                            content=Column(
                                                                alignment=MainAxisAlignment.CENTER,
                                                                controls=[
                                                                    Text(value=datos[0], style="displaySmall",text_align="center",color="GREY800"),
                                                                    Text("Iteracciones realizadas", style="bodySmall",color="GREY800")
                                                                ],
                                                            ),
                                                        ),
                                                        Container(
                                                            margin=margin.symmetric(horizontal=70),
                                                            border=border.all(2, colors.GREY_300),
                                                            border_radius = 12,
                                                            bgcolor=colors.WHITE,
                                                            padding=padding.only(left=30),
                                                            width=220,
                                                            height=100,
                                                            content=Column(
                                                                alignment=MainAxisAlignment.CENTER,
                                                                controls=[
                                                                    Text(value=datos[2], style="displaySmall",text_align="center",color="BLACK",weight="bold"),
                                                                    Text("Error final", style="bodySmall",color="BLACK")
                                                                ],
                                                            ),
                                                        ),
                                                        Container(
                                                            margin=margin.symmetric(horizontal=70),
                                                            border=border.all(2, colors.GREY_300),
                                                            border_radius = 12,
                                                            bgcolor=colors.WHITE,
                                                            padding=padding.only(left=30),
                                                            width=220,
                                                            height=100,
                                                            content=Column(
                                                                alignment=MainAxisAlignment.CENTER,
                                                                controls=[
                                                                    Text(value=datos[3], style="displaySmall",text_align="center",color="GREY900",weight="bold"),
                                                                    Text("RATA", style="bodySmall",color="GREY800")
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ]
                                        )
                                    ),
                                ]
                            )
                        ]
                    ),
                ),
            ]
        ), 
    )
app(target=ui)