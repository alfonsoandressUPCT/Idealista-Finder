import customtkinter as ctk
from dotenv import load_dotenv
from gui_output_historical import Gui_Output_Historical
import requests
import os
import config
import platform
from PIL import Image, ImageTk

load_dotenv()
variables = None

def GuiInput():
    """
    Función para recoger datos de entrada a través de una interfaz gráfica.
    """
    root = ctk.CTk()
    ctk.set_appearance_mode("dark")
    root.title("Idealista Finder")
    root.geometry("1080x720")
    root.resizable(False, False)
    root.configure(bg="#000000")

    icon_image = Image.open("data/idealista_logo.png")
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon_photo)

    global variables

    def abrir_copyright():
        """
        Función para abrir la ventana de copyright.
        """
        copyright_window = ctk.CTkToplevel(root)
        copyright_window.title("Copyright")
        copyright_window.geometry("500x50")
        copyright_window.resizable(False, False)
        copyright_window.grab_set()

        copyright_frame = ctk.CTkFrame(copyright_window, width=500, height=50, corner_radius=0, fg_color="#e4f486")
        copyright_frame.place(x=0, y=0)

        label = ctk.CTkLabel(copyright_frame, text="© Copyright. Idealista Finder - Alfonso Andrés", font=("Montserrat-Bold", 20), 
                            text_color="#000000", anchor="center")
        label.place(x=10, y=10)

    def abrir_instrucciones():
        """
        Función para abrir las instrucciones HTML usando un iframe de tkinterweb.
        """

        instrucciones_window = ctk.CTkToplevel(root)
        instrucciones_window.title("Instrucciones de Uso")
        instrucciones_window.geometry("900x600")
        instrucciones_window.resizable(True, True)
        instrucciones_window.grab_set()
        
        try:
            from tkinterweb import HtmlFrame
            
            # Crear frame HTML
            frame = HtmlFrame(instrucciones_window, width=880, height=580, messages_enabled = False)
            frame.pack(fill="both", expand=True, padx=10, pady=10)
            
            # Leer y convertir el archivo Markdown
            with open("instrucciones.md", "r", encoding="utf-8") as file:
                markdown_text = file.read()
            
            import markdown
            html_content = markdown.markdown(markdown_text)
            
            # Añadir estilos CSS para fuente más grande
            html_con_estilos = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    body {{
                        font-family: Montserrat, sans-serif;
                        font-size: 16px; /* Fuente base más grande */
                        line-height: 1.6;
                        padding: 15px;
                        background-color: #e4f486;
                    }}
                    h1 {{
                        font-family: Montserrat-ExtraBold, sans-serif;
                        font-size: 28px; /* Encabezado grande */
                        color: #000000;
                        margin-top: 20px;
                        margin-bottom: 15px;
                    }}
                    h2 {{
                        font-family: Montserrat-Bold, sans-serif;
                        font-size: 24px; /* Encabezado mediano */
                        color: #000000;
                        margin-top: 18px;
                        margin-bottom: 12px;
                    }}
                    h3 {{
                        font-family: Montserrat-Bold, sans-serif;
                        font-size: 20px; /* Encabezado pequeño */
                        color: #000000;
                        margin-top: 15px;
                        margin-bottom: 10px;
                    }}
                    p {{
                        margin-bottom: 15px;
                    }}
                    ul, ol {{
                        margin-left: 25px;
                        margin-bottom: 15px;
                    }}
                    li {{
                        margin-bottom: 8px;
                    }}
                    strong {{
                        font-weight: bold;
                    }}
                </style>
            </head>
            <body>
                {html_content}
            </body>
            </html>
            """
            
            # Cargar el contenido HTML con estilos
            frame.load_html(html_con_estilos)
        
        except ImportError:
            # Fallback si no está instalado tkinterweb
            import webbrowser
            import tempfile
            import os
            
            with open("instrucciones.md", "r", encoding="utf-8") as file:
                markdown_text = file.read()
            
            import markdown
            html_content = markdown.markdown(markdown_text)
            
            # Crear HTML con fuente más grande
            html_documento = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Instrucciones de Uso</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        font-size: 16px;
                        line-height: 1.6;
                        padding: 20px;
                        max-width: 900px;
                        margin: 0 auto;
                    }}
                    h1 {{ font-size: 28px; color: #2c3e50; }}
                    h2 {{ font-size: 24px; color: #2980b9; }}
                    h3 {{ font-size: 20px; color: #16a085; }}
                </style>
            </head>
            <body>
                {html_content}
            </body>
            </html>
            """
            
            # Crear archivo temporal y abrirlo en el navegador
            temp = tempfile.NamedTemporaryFile(delete=False, suffix='.html', mode='w', encoding='utf-8')
            temp.write(html_documento)
            temp.close()
            
            webbrowser.open('file://' + os.path.abspath(temp.name))
            
            # Mostrar mensaje en la ventana
            label = ctk.CTkLabel(
                instrucciones_window, 
                text="Las instrucciones se han abierto en tu navegador web",
                font=("Montserrat-Bold", 14)
            )
            label.pack(expand=True)

    def necessary_directories():
            """
            Función para crear los directorios necesarios.
            """
            sistema = platform.system()

            if sistema == "Windows":
                base_dir = os.getenv("APPDATA", os.path.expanduser("~\\AppData\\Roaming"))
            elif sistema == "Darwin":  # macOS
                base_dir = os.path.expanduser("~/Library/Application Support")
            elif sistema == "Linux":
                base_dir = os.getenv("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
            else:
                base_dir = os.path.expanduser("~")

            # Carpeta base de la app
            app_dir = os.path.join(base_dir, "Idealista Finder") # Carpeta de la aplicación            
            os.makedirs(app_dir, exist_ok=True) # Crear carpeta de la aplicación

            output_dir = os.path.join(app_dir, "output") # Carpeta de salida
            config.set_output_dir(output_dir) # Guardar la carpeta de salida en config

    def reset_historial():
        """
        Función para restablecer el historial de búsquedas.
        """

        necessary_directories()

        output_dir = config.get_output_dir()

        with open(f"{output_dir}/Historial.txt", "w", encoding="utf-8") as file:
            file.write("")


    def abrir_historial():
        """
        Función para abrir el historial de búsquedas.
        """

        def cerrar_ventanas():
            """
            Función para cerrar las ventanas.
            """
            historial_window.destroy()
            root.destroy()

        historial_window = ctk.CTkToplevel(root)
        historial_window.title("Historial de Búsquedas")
        historial_window.geometry("400x600")
        historial_window.resizable(False, False)
        historial_window.grab_set()

        historical_window_title_frame = ctk.CTkFrame(historial_window, fg_color="#e4f486", corner_radius=0, width=400, height=100)
        historical_window_title_frame.place(x=0, y=0)

        historical_window_title_label = ctk.CTkLabel(historical_window_title_frame, text="Historial de Búsquedas", font=("Montserrat-Bold", 24), text_color="#000000", width=400, height=50)
        historical_window_title_label.place(x=5, y=25)

        historial_window_scroll_frame = ctk.CTkScrollableFrame(historial_window, fg_color="#e4f486", corner_radius=0, width=400)
        historial_window_scroll_frame.place(x=0, y=100, relwidth=1, relheight=1)

        necessary_directories()

        output_dir = config.get_output_dir()

        historial_rutas = list()

        with open(f"{output_dir}/Historial.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            historial_rutas.append(line[:-1] + "/")

        for ruta in historial_rutas:
            
            datos_dict = {}
            with open(ruta + "Datos Utilizados para la Búsqueda.txt", "r", encoding="utf-8") as file:
                for linea in file:
                    if ':' in linea:
                        clave, valor = linea.split(':', 1)  # separar solo en la primera ':'
                        datos_dict[clave.strip()] = valor.strip()

            texto = f"{datos_dict['Ciudad']}. {datos_dict['Habitaciones']} Personas"

            historial_window_scroll_frame_button = ctk.CTkButton(historial_window_scroll_frame, text=texto, text_color="#ffffff", fg_color="#000000", 
                                                                width=350, height=50, corner_radius=5, command=lambda: [cerrar_ventanas(), Gui_Output_Historical(datos_dict, output_dir)])
            historial_window_scroll_frame_button.pack(pady=15, anchor="center")

    def validacion_argumentos():
        """
        Función para validar los argumentos de entrada.
        """

        def create_directories(variables):
            """
            Función para crear los directorios necesarios.
            """
            
            necessary_directories()

            output_dir = config.get_output_dir()
            
            os.makedirs(output_dir, exist_ok=True) # Crear carpeta de salida

            os.makedirs(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas", exist_ok=True)

            os.makedirs(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis de Datos", exist_ok=True)

            os.makedirs(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico", exist_ok=True)

            os.makedirs(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Barras", exist_ok=True)
            os.makedirs(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Cajas", exist_ok=True)
            os.makedirs(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Líneas", exist_ok=True)
            os.makedirs(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Histogramas", exist_ok=True)
            os.makedirs(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Medidas Descriptivas", exist_ok=True)

            os.makedirs(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Geográfico", exist_ok=True)

            with open(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Datos Utilizados para la Búsqueda.txt", "w") as f:
                    for key, value in variables.items():
                        f.write(f"{key}: {value}\n")

            with open(f"{output_dir}/Historial.txt", "a") as f:
                f.write(f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas\n")


        def ventana_emergente(error_message):
            """
            Función para mostrar una ventana emergente con un mensaje de error.
            """
            popup = ctk.CTkToplevel(root)
            popup.title("Error")
            popup.geometry("300x100")
            popup.resizable(False, False)
            popup.grab_set() 

            label = ctk.CTkLabel(popup, text=error_message, width=300, height=50, font=("Montserrat-Bold", 12), text_color="#FF0000", anchor="center")
            label.place(x=0, y=0)

            button = ctk.CTkButton(popup, text="Aceptar", command=popup.destroy, anchor="center", width=100, height=30, fg_color="#FF0000", text_color="#FFFFFF")
            button.place(x=100, y=50)
        
        def validar_ciudad(ciudad: str) -> bool:
            """
            Función para validar la ciudad introducida
            """
            url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={os.getenv('OPENWEATHERMAP_API_KEY')}"
            respuesta = requests.get(url)

            return respuesta.status_code == 200
        
        def validar_pais(nombre_pais: str) -> bool:
            """
            Función para validar el país introducido
            """
            url = f"https://restcountries.com/v3.1/name/{nombre_pais}"
            r = requests.get(url)

            return r.status_code == 200 and bool(r.json())
        

        necesary_parameters = {
            "Ciudad": necesary_arguments_frame1_entry.get(),
            "País": necesary_arguments_frame2_entry.get(),
            "Tipo de Operación": necesary_arguments_frame3_entry.get(),
            "Tipo de Propiedad": necesary_arguments_frame4_entry.get(),
            "Radio de Búsqueda": necesary_arguments_frame5_entry.get()
        }

        ciudad = necesary_parameters["Ciudad"]
        if validar_ciudad(ciudad):
            pass
        else:
            ventana_emergente("Error al introducir la ciudad.")
            return

        pais = necesary_parameters["País"]
        if validar_pais(pais):
            pass
        else:
            ventana_emergente("Error al introducir el país.")
            return

        radio_busqueda = necesary_parameters["Radio de Búsqueda"]
        if radio_busqueda == "" or int(radio_busqueda) <= 0 or int(radio_busqueda) > 10000:
            ventana_emergente("Error al introducir el radio de búsqueda.")
            return

        optional_parameters = {
            "Habitaciones": optional_arguments_frame1_entry.get(),
            "Baños": optional_arguments_frame2_entry.get(),
            "Precio Mínimo": optional_arguments_frame3_entry.get(),
            "Precio Máximo": optional_arguments_frame4_entry.get(),
            "Tamaño Mínimo": optional_arguments_frame5_entry.get(),
            "Tamaño Máximo": optional_arguments_frame6_entry.get(),
            "Ascensor": optional_arguments_frame7_entry.get(),
            "Garaje": optional_arguments_frame8_entry.get()
        }

        habitaciones = optional_parameters["Habitaciones"]
        if habitaciones == "" or float(habitaciones) < 0:
            ventana_emergente("Error al introducir el número de habitaciones.")
            return

        baños = optional_parameters["Baños"]
        if baños == "":
            pass
        else:
            if float(baños) < 0:
                ventana_emergente("Error al introducir el número de baños.")
                return

        precio_minimo = optional_parameters["Precio Mínimo"]
        if precio_minimo == "":
            pass
        else:
            if float(precio_minimo) < 0:
                ventana_emergente("Error al introducir el precio mínimo.")
                return

        precio_maximo = optional_parameters["Precio Máximo"]
        if precio_maximo == "":
            pass
        else:
            if float(precio_maximo) < 0:
                ventana_emergente("Error al introducir el precio máximo.")
                return

        tamaño_minimo = optional_parameters["Tamaño Mínimo"]
        if tamaño_minimo == "":
            pass
        else:
            if float(tamaño_minimo) < 0:
                ventana_emergente("Error al introducir el tamaño mínimo.")
                return

        tamaño_maximo = optional_parameters["Tamaño Máximo"]
        if tamaño_maximo == "":
            pass
        else:
            if float(tamaño_maximo) < 0:
                ventana_emergente("Error al introducir el tamaño máximo.")
                return

        global variables

        variables = {**optional_parameters, **necesary_parameters} # Unir variables necesarias y opcionales

        create_directories(variables)

        config.set_variables(variables)  # Guardamos las variables en config

        root.quit()
        root.destroy()

    ##################################################################################################################################################

    necesary_arguments_frame = ctk.CTkFrame(root, width=540, height=540, corner_radius=0, fg_color="#e4f486")
    necesary_arguments_frame.place(x=0, y=0)

    title_necessary_arguments_frame = ctk.CTkFrame(necesary_arguments_frame, width=540, height=80, corner_radius=0, fg_color="#e4f486")
    title_necessary_arguments_frame.place(x=0, y=0)

    title_necessary_arguments_label = ctk.CTkLabel(title_necessary_arguments_frame,
                                                   text="Parámetros Necesarios", font=("Montserrat-ExtraBold", 20),
                                                   text_color="#000000", width=540, height=80, anchor="center")
    title_necessary_arguments_label.place(x=0, y=0)

    necesary_arguments_frame1 = ctk.CTkFrame(necesary_arguments_frame, width=540, height=92, corner_radius=0, fg_color="#e4f486")
    necesary_arguments_frame1.place(x=0, y=80)

    necesary_arguments_frame1_label = ctk.CTkLabel(necesary_arguments_frame1,
                                                   text="Ciudad", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=92, anchor="center")
    necesary_arguments_frame1_label.place(x=0, y=0)

    necesary_arguments_frame1_entry = ctk.CTkEntry(necesary_arguments_frame1, width=300, height=46, placeholder_text="Introduzca la ciudad",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    necesary_arguments_frame1_entry.place(x=210, y=23)

    necesary_arguments_frame2 = ctk.CTkFrame(necesary_arguments_frame, width=540, height=92, corner_radius=0, fg_color="#e4f486")
    necesary_arguments_frame2.place(x=0, y=172)

    necesary_arguments_frame2_label = ctk.CTkLabel(necesary_arguments_frame2,
                                                   text="País", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=92, anchor="center")
    necesary_arguments_frame2_label.place(x=0, y=0)

    necesary_arguments_frame2_entry = ctk.CTkEntry(necesary_arguments_frame2, width=300, height=46, placeholder_text="Introduzca el país",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    necesary_arguments_frame2_entry.place(x=210, y=23)

    necesary_arguments_frame3 = ctk.CTkFrame(necesary_arguments_frame, width=540, height=92, corner_radius=0, fg_color="#e4f486")
    necesary_arguments_frame3.place(x=0, y=264)

    necesary_arguments_frame3_label = ctk.CTkLabel(necesary_arguments_frame3,
                                                   text="Tipo de Operación", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=92, anchor="center")
    necesary_arguments_frame3_label.place(x=0, y=0)

    necesary_arguments_frame3_entry = ctk.CTkOptionMenu(necesary_arguments_frame3, width=300, height=46, values=["Venta", "Alquiler", "Compartir"], 
                                                        fg_color="#000000", text_color="#ffffff", button_color="#000000")
    necesary_arguments_frame3_entry.place(x=210, y=23)

    necesary_arguments_frame4 = ctk.CTkFrame(necesary_arguments_frame, width=540, height=92, corner_radius=0, fg_color="#e4f486")
    necesary_arguments_frame4.place(x=0, y=356)

    necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                        values=["Vivienda", "Habitación", "Garajes", "Trasteros", "Oficinas", "Locales o Naves", "Traspasos", 
                                                                "Terrenos", "Edificios", "Vacacional", "Obra Nueva"], 
                                                        fg_color="#000000", text_color="#ffffff", button_color="#000000")
    necesary_arguments_frame4_entry.place(x=210, y=23)

    necesary_arguments_frame4_label = ctk.CTkLabel(necesary_arguments_frame4,
                                                   text="Tipo de Propiedad", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=92, anchor="center")
    necesary_arguments_frame4_label.place(x=0, y=0)

    necesary_arguments_frame5 = ctk.CTkFrame(necesary_arguments_frame, width=540, height=92, corner_radius=0, fg_color="#e4f486")
    necesary_arguments_frame5.place(x=0, y=448)

    necesary_arguments_frame5_label = ctk.CTkLabel(necesary_arguments_frame5,
                                                   text=f"Radio de Búsqueda", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=92, anchor="center")
    necesary_arguments_frame5_label.place(x=0, y=0)

    necesary_arguments_frame5_entry = ctk.CTkEntry(necesary_arguments_frame5, width=300, height=46, placeholder_text="Introduzca el radio de búsqueda (0-10000 m)",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    necesary_arguments_frame5_entry.place(x=210, y=23)

    ##################################################################################################################################################
    
    optional_arguments_frame = ctk.CTkFrame(root, width=540, height=540, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame.place(x=540, y=0)

    title_optional_arguments_frame = ctk.CTkFrame(optional_arguments_frame, width=540, height=80, corner_radius=0, fg_color="#909b4f")
    title_optional_arguments_frame.place(x=0, y=0)

    title_optional_arguments_label = ctk.CTkLabel(title_optional_arguments_frame,
                                                   text="Parámetros Opcionales", font=("Montserrat-ExtraBold", 20),
                                                   text_color="#000000", width=540, height=80, anchor="center")
    title_optional_arguments_label.place(x=0, y=0)

    optional_arguments_frame1 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame1.place(x=0, y=80)

    optional_arguments_frame1_label = ctk.CTkLabel(optional_arguments_frame1,
                                                   text="Habitaciones", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame1_label.place(x=0, y=0)

    optional_arguments_frame1_entry = ctk.CTkEntry(optional_arguments_frame1, width=300, height=46, placeholder_text="Introduzca el número (exacto) de habitaciones",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame1_entry.place(x=210, y=5)

    optional_arguments_frame2 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame2.place(x=0, y=137.5)

    optional_arguments_frame2_label = ctk.CTkLabel(optional_arguments_frame2,
                                                   text="Baños", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame2_label.place(x=0, y=0)

    optional_arguments_frame2_entry = ctk.CTkEntry(optional_arguments_frame2, width=300, height=46, placeholder_text="Introduzca el número mínimo de baños",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame2_entry.place(x=210, y=5)

    optional_arguments_frame3 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame3.place(x=0, y=195)

    optional_arguments_frame3_label = ctk.CTkLabel(optional_arguments_frame3,
                                                   text="Precio Mínimo", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame3_label.place(x=0, y=0)

    optional_arguments_frame3_entry = ctk.CTkEntry(optional_arguments_frame3, width=300, height=46, placeholder_text="Introduzca el precio mínimo (€)",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame3_entry.place(x=210, y=5)

    optional_arguments_frame4 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame4.place(x=0, y=252.5)

    optional_arguments_frame4_label = ctk.CTkLabel(optional_arguments_frame4,
                                                   text="Precio Máximo", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame4_label.place(x=0, y=0)

    optional_arguments_frame4_entry = ctk.CTkEntry(optional_arguments_frame4, width=300, height=46, placeholder_text="Introduzca el precio máximo (€)",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame4_entry.place(x=210, y=5)

    optional_arguments_frame5 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame5.place(x=0, y=310)

    optional_arguments_frame5_label = ctk.CTkLabel(optional_arguments_frame5,
                                                   text="Tamaño Mínimo", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame5_label.place(x=0, y=0)

    optional_arguments_frame5_entry = ctk.CTkEntry(optional_arguments_frame5, width=300, height=46, placeholder_text="Introduzca el tamaño mínimo (m²)",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame5_entry.place(x=210, y=5)

    optional_arguments_frame6 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame6.place(x=0, y=367.5)

    optional_arguments_frame6_label = ctk.CTkLabel(optional_arguments_frame6,
                                                   text="Tamaño Máximo", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame6_label.place(x=0, y=0)

    optional_arguments_frame6_entry = ctk.CTkEntry(optional_arguments_frame6, width=300, height=46, placeholder_text="Introduzca el tamaño máximo (m²)",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame6_entry.place(x=210, y=5)

    optional_arguments_frame7 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame7.place(x=0, y=425)

    optional_arguments_frame7_label = ctk.CTkLabel(optional_arguments_frame7,
                                                   text="Ascensor", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame7_label.place(x=0, y=0)

    optional_arguments_frame7_entry = ctk.CTkOptionMenu(optional_arguments_frame7, width=300, height=46, values=["Seleccionar", "Con Ascensor", "Sin Ascensor"],
                                                        fg_color="#000000", text_color="#ffffff", button_color="#000000")
    optional_arguments_frame7_entry.place(x=210, y=5)

    optional_arguments_frame8 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame8.place(x=0, y=482.5)

    optional_arguments_frame8_label = ctk.CTkLabel(optional_arguments_frame8,
                                                   text="Garaje", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame8_label.place(x=0, y=0)

    optional_arguments_frame8_entry = ctk.CTkOptionMenu(optional_arguments_frame8, width=300, height=46, values=["Seleccionar", "Con Garaje", "Sin Garaje"],
                                                        fg_color="#000000", text_color="#ffffff", button_color="#000000")
    optional_arguments_frame8_entry.place(x=210, y=5)

    ##################################################################################################################################################

    search_frame = ctk.CTkFrame(root, width=1080, height=180, corner_radius=0, fg_color="#d6a9c5")
    search_frame.place(x=0, y=540)

    title_search_frame = ctk.CTkFrame(search_frame, width=1080, height=80, corner_radius=0, fg_color="#d6a9c5")
    title_search_frame.place(x=0, y=0)

    title_search_label = ctk.CTkLabel(title_search_frame,
                                        text="Realizar Búsqueda", font=("Montserrat-ExtraBold", 20),
                                        text_color="#000000", width=1080, height=80, anchor="center")
    title_search_label.place(x=0, y=0)

    title_search_frame_bottom = ctk.CTkButton(search_frame, text="Buscar", font=("Montserrat-Bold", 16), 
                                              text_color="#FFFFFF", width=80, height=50, corner_radius=5, fg_color="#000000",
                                              command=validacion_argumentos)
    title_search_frame_bottom.place(x=500, y=80)

    instructions_search_frame_buttom = ctk.CTkButton(search_frame, text="Instrucciones", font=("Montserrat-Bold", 14),
                                         text_color="#FFFFFF", width=250, height=30, corner_radius=5, fg_color="#000000", command=abrir_instrucciones)
    instructions_search_frame_buttom.place(x=825, y=110)

    copyright_search_frame_buttom = ctk.CTkButton(search_frame, text="Copyright. Derechos de Autor", font=("Montserrat-Bold", 14),
                                      text_color="#FFFFFF", width=250, height=30, corner_radius=5, fg_color="#000000", command=abrir_copyright)
    copyright_search_frame_buttom.place(x=825, y=145)

    historical_search_frame_buttom = ctk.CTkButton(search_frame, text="Historial de Búsquedas", font=("Montserrat-Bold", 14),
                                      text_color="#FFFFFF", width=250, height=30, corner_radius=5, fg_color="#000000", command=abrir_historial)
    historical_search_frame_buttom.place(x=825, y=75)

    reset_historical_search_frame_buttom = ctk.CTkButton(search_frame, text="Restablecer Historial", font=("Montserrat-Bold", 14),
                                      text_color="#FFFFFF", width=250, height=30, corner_radius=5, fg_color="#000000", command=reset_historial)
    reset_historical_search_frame_buttom.place(x=825, y=40)

    root.mainloop()

    return