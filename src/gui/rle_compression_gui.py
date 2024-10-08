import sys
import os

# Get the absolute path of the project root
# Obtén la ruta absoluta de la raíz del proyecto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add the project root path to sys.path
# Agrega la ruta raíz del proyecto al sys.path
sys.path.append(project_root)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from src.functionalities.rle_compression import (
    rle_encode, 
    rle_decode, 
    RLECompressionNoneError, 
    RLECompressionIntegerError, 
    RLECompressionListError, 
    RLECompressionDictError, 
    RLECompressionNegativeValueError, 
    RLECompressionZeroCountError
)

# Clase para la pantalla de bienvenida
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Etiqueta de bienvenida
        welcome_label = Label(
            text="Welcome to the Text Compressor and Decompressor!",
            color=(1, 1, 1, 1),
            font_size=24,
            halign='center',
            valign='middle'
        )
        welcome_label.bind(size=welcome_label.setter('text_size'))  # Centrar el texto
        layout.add_widget(welcome_label)

        # Botón para iniciar la compresión/descompresión
        start_button = Button(
            text="Start",
            background_color=(0.7, 0.7, 0.7, 1),  # Gris claro
            color=(0, 0, 0, 1),                   # Texto negro
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5}
        )
        start_button.bind(on_press=self.go_to_compression)
        layout.add_widget(start_button)

        self.add_widget(layout)
    
    def go_to_compression(self, instance):
        # Cambiar a la pantalla de compresión
        self.manager.current = 'compression_screen'

# Clase para la pantalla de compresión/descompresión
class CompressionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label for text input (title for the input section)
        self.label_input = Label(text='Enter the text of the desired option: ', color=(1, 1, 1, 1), font_size=18)
        self.layout.add_widget(self.label_input)

        # Text input field
        self.text_input = TextInput(
            multiline=False, 
            background_color=(0.9, 0.9, 0.9, 1),  # Fondo gris claro
            foreground_color=(0, 0, 0, 1),         # Texto negro
            size_hint=(1, None),
            height=40
        )
        self.layout.add_widget(self.text_input)

        # Compress button with light gray background and black text
        self.compress_button = Button(
            text='Compress', 
            background_color=(0.7, 0.7, 0.7, 1),  # Gris claro
            color=(0, 0, 0, 1),                    # Texto negro
            size_hint=(1, None),
            height=50
        )
        self.compress_button.bind(on_press=self.compress_text)
        self.layout.add_widget(self.compress_button)

        # Label to display the compressed result
        self.compressed_label = Label(text='Compressed result:', color=(1, 1, 1, 1), font_size=16)
        self.layout.add_widget(self.compressed_label)

        # Label for the compressed output (display area)
        self.compressed_output = Label(
            text='', 
            size_hint_y=None, 
            height=40, 
            color=(1, 1, 1, 1),                    # Texto blanco
            text_size=(Window.width - 20, None),
            halign='left',
            valign='middle'
        )
        self.compressed_output.bind(size=self.compressed_output.setter('text_size'))
        self.layout.add_widget(self.compressed_output)

        # Decompress button with light gray background and black text
        self.decompress_button = Button(
            text='Decompress', 
            background_color=(0.7, 0.7, 0.7, 1),  # Gris claro
            color=(0, 0, 0, 1),                    # Texto negro
            size_hint=(1, None),
            height=50
        )
        self.decompress_button.bind(on_press=self.decompress_text)
        self.layout.add_widget(self.decompress_button)

        # Label to display the decompressed result
        self.decompressed_label = Label(text='Decompressed result:', color=(1, 1, 1, 1), font_size=16)
        self.layout.add_widget(self.decompressed_label)

        # Label for the decompressed output (display area)
        self.decompressed_output = Label(
            text='', 
            size_hint_y=None, 
            height=40, 
            color=(1, 1, 1, 1),                    # Texto blanco
            text_size=(Window.width - 20, None),
            halign='left',
            valign='middle'
        )
        self.decompressed_output.bind(size=self.decompressed_output.setter('text_size'))
        self.layout.add_widget(self.decompressed_output)

        # Error message label
        self.error_label = Label(text='', color=(1, 0, 0, 1), size_hint_y=None, height=40, font_size=14)  # Texto rojo para errores
        self.layout.add_widget(self.error_label)

        self.add_widget(self.layout)

    def compress_text(self, instance):
        try:
            input_text = self.text_input.text
            compressed_text = rle_encode(input_text)  # Usa la función de compresión
            self.compressed_output.text = compressed_text
            self.decompressed_output.text = ''       # Limpiar la salida descomprimida
            self.error_label.text = ''              # Limpiar el mensaje de error si no hay errores
        except (RLECompressionNoneError, RLECompressionIntegerError, RLECompressionListError, RLECompressionDictError) as e:
            self.error_label.text = f"Compression error: {str(e)}"  # Mostrar el mensaje de error

    def decompress_text(self, instance):
        try:
            compressed_text = self.compressed_output.text
            decompressed_text = rle_decode(compressed_text)  # Usa la función de descompresión
            self.decompressed_output.text = decompressed_text
            self.error_label.text = ''  # Limpiar el mensaje de error si no hay errores
        except (RLECompressionNoneError, RLECompressionIntegerError, RLECompressionNegativeValueError, RLECompressionZeroCountError) as e:
            self.error_label.text = f"Decompression error: {str(e)}"  # Mostrar el mensaje de error

# Clase principal de la aplicación
class RLECompressionApp(App):
    def build(self):
        # Set the background color to a dark gray (close to black)
        # Establecer el color de fondo a gris oscuro (cercano a negro)
        Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Fondo gris oscuro

        # Crea el administrador de pantallas con una transición suave
        self.screen_manager = ScreenManager(transition=FadeTransition())

        # Añade la pantalla de bienvenida
        self.screen_manager.add_widget(WelcomeScreen(name='welcome_screen'))

        # Añade la pantalla de compresión/descompresión
        self.screen_manager.add_widget(CompressionScreen(name='compression_screen'))

        # Establece la pantalla de inicio por defecto
        self.screen_manager.current = 'welcome_screen'

        return self.screen_manager

if __name__ == '__main__':
    # Set the window title and logo before the app starts
    # Establecer el título y el logo de la ventana antes de iniciar la app
    Window.title = "TEXT COMPRESSOR"
    Window.icon = "C:/Workspace/Clean Code/text-compressor/LogoTextCompressor.png"

    RLECompressionApp().run()
