from flet import *
import plotly.express as px
from flet.plotly_chart import PlotlyChart




def ui(page: Page):
    datos=[0,0,0,0,0]
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"

    def cargarDatos(_entradas,_salidas,_pesos,_umbrales,_patrones):
        entradas = _entradas
        salidas = _salidas
        pesos = _pesos
        umbrales= _umbrales
        patrones=_patrones
        datos = [entradas,salidas,pesos,umbrales,patrones]
        return datos
    
    def entrenarRed(e):
        return 0
    
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
    subirDatos=ElevatedButton(
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
                Icon(name=icons.UPLOAD_FILE,
                size=20,
                ),
                Text(
                    "Subir datos",
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
                                                            Text(value=datos[0], style="displaySmall",text_align="center",color="GREY800",weight="bold"),
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
                                                            Text(value=datos[1], style="displaySmall",text_align="center",color="GREY800",weight="bold"),
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
                                                            Text(value=datos[2], style="displaySmall",text_align="center",color="GREY800",weight="bold"),
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
                                                            Text(value=datos[3], style="displaySmall",text_align="center",color="GREY800",weight="bold"),
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
                                                            Text(value=datos[4], style="displaySmall",text_align="center",color="GREY800",weight="bold"),
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
                                                )
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