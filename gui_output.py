import customtkinter as ctk
import config
import platform
import os
from PIL import Image, ImageTk

def Gui_Output():
    """
    Función para crear la interfaz gráfica de usuario (GUI) para la salida de datos.
    """

    variables = config.get_variables()
    output_dir = config.get_output_dir()

    root = ctk.CTk()
    ctk.set_appearance_mode("dark")
    root.title("Idealista Finder")
    root.geometry("1080x720")
    root.resizable(False, False)
    root.configure(bg="#000000")

    icon_image = Image.open("data/idealista_logo.png")
    icon_photo = ImageTk.PhotoImage(icon_image)
    root.iconphoto(False, icon_photo)

    def abrir_analisis_datos():
        """
        Función para abrir el análisis de datos.
        """
        ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis de Datos/Análisis de Datos | {variables['Ciudad']}. {variables['Habitaciones']} Personas.csv"
        
        if platform.system() == "Windows":
            os.startfile(ruta)
        elif platform.system() == "Darwin":  # macOS
            os.system(f"open '{ruta}'")
        else:  # Linux
            os.system(f"xdg-open '{ruta}'")

    def abrir_analisis_economico():
        """
        Función para abrir el análisis económico.
        """
        def abrir_diagrama_barras_precio():
            """
            Función para abrir el diagrama de barras.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Barras/Diagrama de Barras - Precio | {variables['Ciudad']}.png"
            
            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")
        
        def abrir_diagrama_barras_precio_persona():
            """
            Función para abrir el diagrama de barras - precio por persona.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Barras/Diagrama de Barras - Precio por Persona | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_diagrama_barras_precio_tamano():
            """
            Función para abrir el diagrama de barras - precio por tamaño.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Barras/Diagrama de Barras - Precio por Tamaño | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_diagrama_barras_tamano():
            """
            Función para abrir el diagrama de barras - tamaño.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Barras/Diagrama de Barras - Tamaño | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_diagrama_cajas_precio():
            """
            Función para abrir el diagrama de cajas - precio.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Cajas/Diagrama de Cajas - Precio | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_diagrama_cajas_precio_persona():
            """
            Función para abrir el diagrama de cajas - precio por persona.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Cajas/Diagrama de Cajas - Precio por Persona | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_diagrama_cajas_precio_tamano():
            """
            Función para abrir el diagrama de cajas - precio por tamaño.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Cajas/Diagrama de Cajas - Precio por Tamaño | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_diagrama_cajas_tamano():
            """
            Función para abrir el diagrama de cajas - tamaño.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Cajas/Diagrama de Cajas - Tamaño | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_diagrama_lineas_precio():
            """
            Función para abrir el diagrama de líneas - precio.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Líneas/Diagrama de Líneas - Precio | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_diagrama_lineas_precio_persona():
            """
            Función para abrir el diagrama de líneas - precio por persona.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Líneas/Diagrama de Líneas - Precio por Persona | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_diagrama_lineas_precio_tamano():
            """
            Función para abrir el diagrama de líneas - tamaño.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Líneas/Diagrama de Líneas - Precio por Tamaño | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_diagrama_lineas_tamano():
            """
            Función para abrir el diagrama de líneas - tamaño.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Diagrama de Líneas/Diagrama de Líneas - Tamaño | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_histogramas_precio():
            """
            Función para abrir el histograma - precio.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Histogramas/Histograma - Precio | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_histogramas_precio_persona():
            """
            Función para abrir el histograma - precio por persona.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Histogramas/Histograma - Precio por Persona | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_histogramas_precio_tamano():
            """
            Función para abrir el histograma - precio por tamaño.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Histogramas/Histograma - Precio por Tamaño | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        def abrir_histogramas_tamano():
            """
            Función para abrir el histograma - tamaño.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Histogramas/Histograma - Tamaño | {variables['Ciudad']}.png"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")
        
        def abrir_medidas_descriptivas():
            """
            Función para abrir las medidas descriptivas.
            """
            ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Económico/Medidas Descriptivas/Medidas Descriptivas | {variables['Ciudad']}.txt"

            if platform.system() == "Windows":
                os.startfile(ruta)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{ruta}'")
            else:  # Linux
                os.system(f"xdg-open '{ruta}'")

        popup = ctk.CTkToplevel(root)
        popup.title("Análisis Económico")
        popup.geometry("1000x400")
        popup.resizable(False, False)
        popup.grab_set()

        result_frame1 = ctk.CTkFrame(popup, width=200, height=400, corner_radius=0, fg_color="#d6a9c5")
        result_frame1.place(x=0, y=0)

        result_frame1_label_title = ctk.CTkLabel(result_frame1, text="Diagramas de Barras", font=("Montserrat-Bold", 14), text_color="#000000", anchor="center", width=150, height=50)
        result_frame1_label_title.place(x=25, y=10)

        result_frame1_button1 = ctk.CTkButton(result_frame1, text="Precio", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_barras_precio)
        result_frame1_button1.place(x=25, y=71.875)

        result_frame1_button2 = ctk.CTkButton(result_frame1, text="Precio Por Persona", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_barras_precio_persona)
        result_frame1_button2.place(x=25, y=159.375)

        result_frame1_button3 = ctk.CTkButton(result_frame1, text="Precio por Tamaño", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_barras_precio_tamano)
        result_frame1_button3.place(x=25, y=246.875)

        result_frame1_button4 = ctk.CTkButton(result_frame1, text="Tamaño", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_barras_tamano)
        result_frame1_button4.place(x=25, y=334.375)

        result_frame2 = ctk.CTkFrame(popup, width=200, height=400, corner_radius=0, fg_color="#d6a9c5")
        result_frame2.place(x=200, y=0)

        result_frame2_label_title = ctk.CTkLabel(result_frame2, text="Diagramas de Cajas", font=("Montserrat-Bold", 14), text_color="#000000", anchor="center", width=150, height=50)
        result_frame2_label_title.place(x=25, y=10)

        result_frame2_button1 = ctk.CTkButton(result_frame2, text="Precio", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_cajas_precio)
        result_frame2_button1.place(x=25, y=71.875)

        result_frame2_button2 = ctk.CTkButton(result_frame2, text="Precio Por Persona", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_cajas_precio_persona)
        result_frame2_button2.place(x=25, y=159.375)

        result_frame2_button3 = ctk.CTkButton(result_frame2, text="Precio por Tamaño", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_cajas_precio_tamano)
        result_frame2_button3.place(x=25, y=246.875)

        result_frame2_button4 = ctk.CTkButton(result_frame2 , text="Tamaño", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_cajas_tamano)
        result_frame2_button4.place(x=25, y=334.375)

        result_frame3 = ctk.CTkFrame(popup, width=200, height=400, corner_radius=0, fg_color="#d6a9c5")
        result_frame3.place(x=400, y=0)

        result_frame3_label_title = ctk.CTkLabel(result_frame3, text="Diagramas de Líneas", font=("Montserrat-Bold", 14), text_color="#000000", anchor="center", width=150, height=50)
        result_frame3_label_title.place(x=25, y=10)

        result_frame3_button1 = ctk.CTkButton(result_frame3, text="Precio", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_lineas_precio)
        result_frame3_button1.place(x=25, y=71.875)

        result_frame3_button2 = ctk.CTkButton(result_frame3, text="Precio Por Persona", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_lineas_precio_persona)
        result_frame3_button2.place(x=25, y=159.375)

        result_frame3_button3 = ctk.CTkButton(result_frame3, text="Precio por Tamaño", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_lineas_precio_tamano)
        result_frame3_button3.place(x=25, y=246.875)

        result_frame3_button4 = ctk.CTkButton(result_frame3 , text="Tamaño", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_diagrama_lineas_tamano)
        result_frame3_button4.place(x=25, y=334.375)

        result_frame4 = ctk.CTkFrame(popup, width=200, height=400, corner_radius=0, fg_color="#d6a9c5")
        result_frame4.place(x=600, y=0)

        result_frame4_label_title = ctk.CTkLabel(result_frame4, text="Histogramas", font=("Montserrat-Bold", 14), text_color="#000000", anchor="center", width=150, height=50)
        result_frame4_label_title.place(x=25, y=10)

        result_frame4_button1 = ctk.CTkButton(result_frame4, text="Precio", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_histogramas_precio)
        result_frame4_button1.place(x=25, y=71.875)

        result_frame4_button2 = ctk.CTkButton(result_frame4, text="Precio Por Persona", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_histogramas_precio_persona)
        result_frame4_button2.place(x=25, y=159.375)

        result_frame4_button3 = ctk.CTkButton(result_frame4, text="Precio por Tamaño", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_histogramas_precio_tamano)
        result_frame4_button3.place(x=25, y=246.875)

        result_frame4_button4 = ctk.CTkButton(result_frame4 , text="Tamaño", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_histogramas_tamano)
        result_frame4_button4.place(x=25, y=334.375)

        result_frame5 = ctk.CTkFrame(popup, width=200, height=400, corner_radius=0, fg_color="#d6a9c5")
        result_frame5.place(x=800, y=0)

        result_frame5_label_title = ctk.CTkLabel(result_frame5, text="Medidas Descriptivas", font=("Montserrat-Bold", 14), text_color="#000000", anchor="center", width=100, height=50)
        result_frame5_label_title.place(x=25, y=10)

        result_frame5_button = ctk.CTkButton(result_frame5, text="Análisis", bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, width=150, height=43.75, command=abrir_medidas_descriptivas)
        result_frame5_button.place(x=25, y=71.875)


    def abrir_analisis_geografico():
        """
        Función para abrir el análisis geográfico.
        """

        ruta = f"{output_dir}/{variables['Ciudad']}. {variables['Habitaciones']} Personas/Análisis Geográfico/Análisis Geográfico | {variables['Ciudad']}. {variables['Habitaciones']} Personas.html"

        if platform.system() == "Windows":
            os.startfile(ruta)
        elif platform.system() == "Darwin":  # macOS
            os.system(f"open '{ruta}'")
        else:  # Linux
            os.system(f"xdg-open '{ruta}'")

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

    necesary_arguments_frame1_entry = ctk.CTkEntry(necesary_arguments_frame1, width=300, height=46, placeholder_text=f"{variables['Ciudad']}",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    necesary_arguments_frame1_entry.place(x=210, y=23)

    necesary_arguments_frame2 = ctk.CTkFrame(necesary_arguments_frame, width=540, height=92, corner_radius=0, fg_color="#e4f486")
    necesary_arguments_frame2.place(x=0, y=172)

    necesary_arguments_frame2_label = ctk.CTkLabel(necesary_arguments_frame2,
                                                   text="País", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=92, anchor="center")
    necesary_arguments_frame2_label.place(x=0, y=0)

    necesary_arguments_frame2_entry = ctk.CTkEntry(necesary_arguments_frame2, width=300, height=46, placeholder_text=f"{variables['País']}",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    necesary_arguments_frame2_entry.place(x=210, y=23)

    necesary_arguments_frame3 = ctk.CTkFrame(necesary_arguments_frame, width=540, height=92, corner_radius=0, fg_color="#e4f486")
    necesary_arguments_frame3.place(x=0, y=264)

    necesary_arguments_frame3_label = ctk.CTkLabel(necesary_arguments_frame3,
                                                   text="Tipo de Operación", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=92, anchor="center")
    necesary_arguments_frame3_label.place(x=0, y=0)

    if variables['Tipo de Operación'] == "Alquiler":
        necesary_arguments_frame3_entry = ctk.CTkOptionMenu(necesary_arguments_frame3, width=300, height=46, values=["Alquiler", "Venta", "Compartir"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Operación'] == "Venta":
        necesary_arguments_frame3_entry = ctk.CTkOptionMenu(necesary_arguments_frame3, width=300, height=46, values=["Venta", "Alquiler", "Compartir"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Operación'] == "Compartir":
        necesary_arguments_frame3_entry = ctk.CTkOptionMenu(necesary_arguments_frame3, width=300, height=46, values=["Compartir", "Alquiler", "Venta"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    necesary_arguments_frame3_entry.place(x=210, y=23)


    necesary_arguments_frame4 = ctk.CTkFrame(necesary_arguments_frame, width=540, height=92, corner_radius=0, fg_color="#e4f486")
    necesary_arguments_frame4.place(x=0, y=356)

    if variables['Tipo de Propiedad'] == "Vivienda":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Vivienda", "Habitación", "Garajes", "Trasteros", "Oficinas", 
                                                                    "Locales o Naves", "Traspasos", "Terrenos", "Edificios", "Vacacional", "Obra Nueva"], 
                                                                    fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Propiedad'] == "Habitación":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Habitación", "Vivienda", "Garajes", "Trasteros", "Oficinas", 
                                                                    "Locales o Naves", "Traspasos", "Terrenos", "Edificios", "Vacacional", "Obra Nueva"], 
                                                                    fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Propiedad'] == "Garajes":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Garajes", "Vivienda", "Habitación", "Trasteros", "Oficinas",
                                                                     "Locales o Naves", "Traspasos", "Terrenos", "Edificios", "Vacacional", "Obra Nueva"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Propiedad'] == "Trasteros":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Trasteros", "Vivienda", "Habitación", "Garajes", "Oficinas", 
                                                                    "Locales o Naves", "Traspasos", "Terrenos", "Edificios", "Vacacional", "Obra Nueva"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Propiedad'] == "Oficinas":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Oficinas", "Vivienda", "Habitación", "Garajes", "Trasteros", "Locales o Naves", 
                                                                    "Traspasos", "Terrenos", "Edificios", "Vacacional", "Obra Nueva"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
        
    elif variables['Tipo de Propiedad'] == "Locales o Naves":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Locales o Naves", "Vivienda", "Habitación", "Garajes", "Trasteros", "Oficinas", 
                                                                    "Traspasos", "Terrenos", "Edificios", "Vacacional", "Obra Nueva"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Propiedad'] == "Traspasos":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Traspasos", "Vivienda", "Habitación", "Garajes", "Trasteros", "Oficinas", 
                                                                    "Locales o Naves", "Terrenos", "Edificios", "Vacacional", "Obra Nueva"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Propiedad'] == "Terrenos":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Terrenos", "Vivienda", "Habitación", "Garajes", "Trasteros", "Oficinas", 
                                                                    "Locales o Naves", "Traspasos", "Edificios", "Vacacional", "Obra Nueva"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Propiedad'] == "Edificios":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Edificios", "Vivienda", "Habitación", "Garajes", "Trasteros", "Oficinas", 
                                                                    "Locales o Naves", "Traspasos", "Terrenos", "Vacacional", "Obra Nueva"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Propiedad'] == "Vacacional":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Vacacional", "Vivienda", "Habitación", "Garajes", "Trasteros", "Oficinas", 
                                                                    "Locales o Naves", "Traspasos", "Terrenos", "Edificios", "Obra Nueva"], 
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    elif variables['Tipo de Propiedad'] == "Obra Nueva":
        necesary_arguments_frame4_entry = ctk.CTkOptionMenu(necesary_arguments_frame4, width=300, height=46, 
                                                            values=["Obra Nueva", "Vivienda", "Habitación", "Garajes", "Trasteros", "Oficinas", 
                                                                    "Locales o Naves", "Traspasos", "Terrenos", "Edificios", "Vacacional"], 
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

    if 'Radio de Búsqueda' in variables:
        necesary_arguments_frame5_entry = ctk.CTkEntry(necesary_arguments_frame5, width=300, height=46, placeholder_text=f"{variables['Radio de Búsqueda']}",
                                                       fg_color="#000000", placeholder_text_color="#ffffff")
    else:
        necesary_arguments_frame5_entry = ctk.CTkEntry(necesary_arguments_frame5, width=300, height=46, placeholder_text=f"",
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

    if 'Habitaciones' in variables:
        optional_arguments_frame1_entry = ctk.CTkEntry(optional_arguments_frame1, width=300, height=46, placeholder_text=variables["Habitaciones"],
                                                            fg_color="#000000", text_color="#ffffff")
    else:
        optional_arguments_frame1_entry = ctk.CTkEntry(optional_arguments_frame1, width=300, height=46, placeholder_text=f"",
                                                   fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame1_entry.place(x=210, y=5)


    optional_arguments_frame2 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame2.place(x=0, y=137.5)

    optional_arguments_frame2_label = ctk.CTkLabel(optional_arguments_frame2,
                                                   text="Baños", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame2_label.place(x=0, y=0)

    if 'Baños' in variables:
        optional_arguments_frame2_entry = ctk.CTkEntry(optional_arguments_frame2, width=300, height=46, placeholder_text=variables["Baños"],
                                                            fg_color="#000000", placeholder_text_color="#ffffff")
    elif variables['Baños'] == "Sin Baños":
        optional_arguments_frame2_entry = ctk.CTkEntry(optional_arguments_frame2, width=300, height=46, placeholder_text="",
                                                            fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame2_entry.place(x=210, y=5)


    optional_arguments_frame3 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame3.place(x=0, y=195)

    optional_arguments_frame3_label = ctk.CTkLabel(optional_arguments_frame3,
                                                   text="Precio Mínimo", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame3_label.place(x=0, y=0)

    if 'Precio Mínimo' in variables:
        optional_arguments_frame3_entry = ctk.CTkEntry(optional_arguments_frame3, width=300, height=46, placeholder_text=f"{variables['Precio Mínimo']}",
                                                       fg_color="#000000", placeholder_text_color="#ffffff")
    else:
        optional_arguments_frame3_entry = ctk.CTkEntry(optional_arguments_frame3, width=300, height=46, placeholder_text="",
                                                       fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame3_entry.place(x=210, y=5)


    optional_arguments_frame4 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame4.place(x=0, y=252.5)

    optional_arguments_frame4_label = ctk.CTkLabel(optional_arguments_frame4,
                                                   text="Precio Máximo", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame4_label.place(x=0, y=0)


    if 'Precio Máximo' in variables:
        optional_arguments_frame4_entry = ctk.CTkEntry(optional_arguments_frame4, width=300, height=46, placeholder_text=f"{variables['Precio Máximo']}",
                                                       fg_color="#000000", placeholder_text_color="#ffffff")
    else:
        optional_arguments_frame4_entry = ctk.CTkEntry(optional_arguments_frame4, width=300, height=46, placeholder_text="",
                                                       fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame4_entry.place(x=210, y=5)


    optional_arguments_frame5 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame5.place(x=0, y=310)

    optional_arguments_frame5_label = ctk.CTkLabel(optional_arguments_frame5,
                                                   text="Tamaño Mínimo", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame5_label.place(x=0, y=0)

    if 'Tamaño Mínimo' in variables:
        optional_arguments_frame5_entry = ctk.CTkEntry(optional_arguments_frame5, width=300, height=46, placeholder_text=f"{variables['Tamaño Mínimo']}",
                                                       fg_color="#000000", placeholder_text_color="#ffffff")
    else:
        optional_arguments_frame5_entry = ctk.CTkEntry(optional_arguments_frame5, width=300, height=46, placeholder_text="",
                                                       fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame5_entry.place(x=210, y=5)


    optional_arguments_frame6 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame6.place(x=0, y=367.5)

    optional_arguments_frame6_label = ctk.CTkLabel(optional_arguments_frame6,
                                                   text="Tamaño Máximo", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame6_label.place(x=0, y=0)

    if 'Tamaño Máximo' in variables:
        optional_arguments_frame6_entry = ctk.CTkEntry(optional_arguments_frame6, width=300, height=46, placeholder_text=f"{variables['Tamaño Máximo']}",
                                                       fg_color="#000000", placeholder_text_color="#ffffff")
    else:
        optional_arguments_frame6_entry = ctk.CTkEntry(optional_arguments_frame6, width=300, height=46, placeholder_text="",
                                                       fg_color="#000000", placeholder_text_color="#ffffff")
    optional_arguments_frame6_entry.place(x=210, y=5)


    optional_arguments_frame7 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame7.place(x=0, y=425)

    optional_arguments_frame7_label = ctk.CTkLabel(optional_arguments_frame7,
                                                   text="Ascensor", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame7_label.place(x=0, y=0)

    if 'Ascensor' in variables:
        if variables['Ascensor'] == "Con Ascensor":
            optional_arguments_frame7_entry = ctk.CTkOptionMenu(optional_arguments_frame7, width=300, height=46, values=["Con Ascensor","Seleccionar", "Sin Ascensor"],
                                                                fg_color="#000000", text_color="#ffffff", button_color="#000000")
        elif variables['Ascensor'] == "Sin Ascensor":
            optional_arguments_frame7_entry = ctk.CTkOptionMenu(optional_arguments_frame7, width=300, height=46, values=["Sin Ascensor","Seleccionar", "Con Ascensor"],
                                                                fg_color="#000000", text_color="#ffffff", button_color="#000000")
        elif variables['Ascensor'] == "Seleccionar":
            optional_arguments_frame7_entry = ctk.CTkOptionMenu(optional_arguments_frame7, width=300, height=46, values=["","Seleccionar", "Con Ascensor", "Sin Ascensor"],
                                                                fg_color="#000000", text_color="#ffffff", button_color="#000000")
    else:
        optional_arguments_frame7_entry = ctk.CTkOptionMenu(optional_arguments_frame7, width=300, height=46, values=["","Seleccionar", "Con Ascensor", "Sin Ascensor"],
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    optional_arguments_frame7_entry.place(x=210, y=5)


    optional_arguments_frame8 = ctk.CTkFrame(optional_arguments_frame, width=540, height=57.5, corner_radius=0, fg_color="#909b4f")
    optional_arguments_frame8.place(x=0, y=482.5)

    optional_arguments_frame8_label = ctk.CTkLabel(optional_arguments_frame8,
                                                   text="Garaje", font=("Montserrat-Bold", 16),
                                                   text_color="#000000", width=180, height=57.5, anchor="center")
    optional_arguments_frame8_label.place(x=0, y=0)

    if 'Garaje' in variables:
        if variables['Garaje'] == "Con Garaje":
            optional_arguments_frame8_entry = ctk.CTkOptionMenu(optional_arguments_frame8, width=300, height=46, values=["Con Garaje","Seleccionar", "Sin Garaje"],
                                                                fg_color="#000000", text_color="#ffffff", button_color="#000000")
        elif variables['Garaje'] == "Sin Garaje":
            optional_arguments_frame8_entry = ctk.CTkOptionMenu(optional_arguments_frame8, width=300, height=46, values=["Sin Garaje","Seleccionar", "Con Garaje"],
                                                                fg_color="#000000", text_color="#ffffff", button_color="#000000")
        elif variables['Garaje'] == "Seleccionar":
            optional_arguments_frame8_entry = ctk.CTkOptionMenu(optional_arguments_frame8, width=300, height=46, values=["","Seleccionar", "Con Garaje", "Sin Garaje"],
                                                                fg_color="#000000", text_color="#ffffff", button_color="#000000")
    else:
        optional_arguments_frame8_entry = ctk.CTkOptionMenu(optional_arguments_frame8, width=300, height=46, values=["","Seleccionar", "Con Garaje", "Sin Garaje"],
                                                            fg_color="#000000", text_color="#ffffff", button_color="#000000")
    optional_arguments_frame8_entry.place(x=210, y=5)

    ##################################################################################################################################################

    results_frame = ctk.CTkFrame(root, width=1080, height=180, corner_radius=0, fg_color="#d6a9c5")
    results_frame.place(x=0, y=540)

    title_results_frame = ctk.CTkFrame(results_frame, width=1080, height=80, corner_radius=0, fg_color="#d6a9c5")
    title_results_frame.place(x=0, y=0)

    title_results_label = ctk.CTkLabel(title_results_frame,
                                        text="Resultados de Búsqueda", font=("Montserrat-ExtraBold", 20),
                                        text_color="#000000", width=1080, height=80, anchor="center")
    title_results_label.place(x=0, y=0)

    results_frame1 = ctk.CTkFrame(results_frame, width=360, height=100, corner_radius=0, bg_color="#d6a9c5", fg_color="#d6a9c5")
    results_frame1.place(x=0, y=80)

    results_frame1_button = ctk.CTkButton(results_frame1, text="Análisis de Datos", height=50, width=180, 
                                          bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, command=abrir_analisis_datos)
    results_frame1_button.place(x=90, y=5)

    results_frame2 = ctk.CTkFrame(results_frame, width=360, height=100, corner_radius=0, bg_color="#d6a9c5", fg_color="#d6a9c5")
    results_frame2.place(x=360, y=80)

    results_frame2_button = ctk.CTkButton(results_frame2, text="Análisis Económico", height=50, width=180, 
                                          bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, command=abrir_analisis_economico)
    results_frame2_button.place(x=90, y=5)

    results_frame3 = ctk.CTkFrame(results_frame, width=360, height=100, corner_radius=0, bg_color="#d6a9c5", fg_color="#d6a9c5")
    results_frame3.place(x=720, y=80)

    results_frame3_button = ctk.CTkButton(results_frame3, text="Análisis Geográfico", height=50, width=180, 
                                          bg_color="#d6a9c5", fg_color="#000000", corner_radius=5, command=abrir_analisis_geografico)
    results_frame3_button.place(x=90, y=5)

    root.mainloop()