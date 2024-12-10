# Cifrado Hill 🔐

## Descripción del Proyecto
Una aplicación de escritorio en Python que implementa el método de Cifrado de Hill, un algoritmo de cifrado simétrico basado en álgebra lineal.

## 🚀 Características
- **Interfaz Gráfica Intuitiva**: Fácil de usar
- **Cifrado y Descifrado**: Procesa texto con una matriz clave 2x2
- **Método Algebraico**: Utiliza transformaciones matriciales
- **Manejo de Errores**: Validación de entrada y mensajes de error

## 📋 Requisitos
- Python 3.x
- Bibliotecas:
  - tkinter
  - numpy

### Pasos para Cifrar/Descifrar
1. Ingresa el texto
2. Introduce la clave (4 números separados por comas)
3. Selecciona el modo (Cifrar/Descifrar)
4. Presiona "Procesar"

## 🔍 Ejemplo
- **Texto**: HOLA
- **Clave**: 3,2,5,7
- **Modo**: Cifrar
- **Resultado**: Texto cifrado se mostrará en la interfaz

## ✨ Detalles Técnicos
- Conversión de texto: A=0, B=1, ..., Z=25
- Procesamiento por bloques de 2 caracteres
- Cifrado/descifrado mediante álgebra matricial
- Padding automático para longitudes impares

## ⚠️ Consideraciones
- Solo procesa letras mayúsculas
- Letras no alfabéticas son ignoradas
- Añade padding si la longitud es impar


## 📧 autor
- Juan José Zambrano Manzano
- 192327
- jjzambranom@ufpso.edu.co
