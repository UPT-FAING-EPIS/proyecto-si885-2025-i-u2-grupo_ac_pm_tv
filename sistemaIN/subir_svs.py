from flask import Flask, request, render_template, redirect, flash
import pandas as pd
import pyodbc
import os

app = Flask(__name__)
app.secret_key = 'clave-secreta'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=serverproyectoin.database.windows.net;'
        'DATABASE=analisistesis;'
        'UID=proyectoin;'
        'PWD=#050.Ada0;'
    )

@app.route('/')
def index():
    return render_template('index.html') 
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No se envió ningún archivo.')
        return redirect('/')
    
    file = request.files['file']
    if file.filename == '':
        flash('Selecciona un archivo CSV válido.')
        return redirect('/')
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    try:
        df = pd.read_csv(filepath)

        if df.empty or df.columns.size == 0:
            flash('El archivo CSV está vacío o mal estructurado.')
            return redirect('/')

        conn = get_connection()
        cursor = conn.cursor()

        for _, row in df.iterrows():
            # Universidad
            cursor.execute("SELECT id_universidad FROM universidad WHERE nombre = ?", row['nombre_universidad'])
            result = cursor.fetchone()
            if result:
                id_uni = result[0]
            else:
                cursor.execute(
                    "INSERT INTO universidad (nombre, ubicacion, tipo) VALUES (?, ?, ?)",
                    row['nombre_universidad'], row['ubicacion_universidad'], row['tipo_universidad']
                )
                cursor.execute("SELECT @@IDENTITY")
                id_uni = int(cursor.fetchone()[0])

            # Archivo CSV
            cursor.execute("SELECT id_archivo FROM archivo_csv WHERE nombre_archivo = ?", row['nombre_archivo_csv'])
            result = cursor.fetchone()
            if result:
                id_archivo = result[0]
            else:
                cursor.execute(
                    "INSERT INTO archivo_csv (nombre_archivo, fecha_subida, ruta_archivo) VALUES (?, ?, ?)",
                    row['nombre_archivo_csv'], row['fecha_subida_csv'], row['ruta_archivo']
                )
                cursor.execute("SELECT @@IDENTITY")
                id_archivo = int(cursor.fetchone()[0])

            # Tesis
            cursor.execute("SELECT id_tesis FROM tesis WHERE titulo = ?", row['titulo'])
            result = cursor.fetchone()
            if result:
                id_tesis = result[0]
            else:
                cursor.execute(
                    "INSERT INTO tesis (ano_publicacion, categoria, id_universidad, titulo) VALUES (?, ?, ?, ?)",
                    row['ano_publicacion'], row['categoria_tesis'], id_uni, row['titulo']
                )
                cursor.execute("SELECT @@IDENTITY")
                id_tesis = int(cursor.fetchone()[0])

            # Tecnologías y categorías
            tecnologias = str(row['tecnologias']).split(';')
            categorias = str(row['categorias_tecnologia']).split(';')

            for tech, cat in zip(tecnologias, categorias):
                tech = tech.strip()
                cat = cat.strip()

                # Insertar categoría si no existe
                cursor.execute("SELECT id_categoria FROM categoria_tecnologia WHERE nombre = ?", cat)
                result = cursor.fetchone()
                if result:
                    id_cat = result[0]
                else:
                    cursor.execute("INSERT INTO categoria_tecnologia (nombre) VALUES (?)", cat)
                    cursor.execute("SELECT @@IDENTITY")
                    id_cat = int(cursor.fetchone()[0])

                # Insertar tecnología si no existe
                cursor.execute("SELECT id_tecnologia FROM tecnologia WHERE nombre = ?", tech)
                result = cursor.fetchone()
                if result:
                    id_tech = result[0]
                else:
                    cursor.execute(
                        "INSERT INTO tecnologia (nombre, id_categoria) VALUES (?, ?)",
                        tech, id_cat
                    )
                    cursor.execute("SELECT @@IDENTITY")
                    id_tech = int(cursor.fetchone()[0])

                # Relación tesis-tecnología
                cursor.execute(
                    "IF NOT EXISTS (SELECT 1 FROM tesis_tecnologia WHERE id_tesis = ? AND id_tecnologia = ?) "
                    "INSERT INTO tesis_tecnologia (id_tesis, id_tecnologia) VALUES (?, ?)",
                    id_tesis, id_tech, id_tesis, id_tech
                )

        conn.commit()
        cursor.close()
        conn.close()
        flash('Archivo cargado y datos insertados correctamente.')

    except Exception as e:
        flash(f'Error al procesar archivo: {e}')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
