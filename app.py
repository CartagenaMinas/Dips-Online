######################## Importar Librerias ##############################
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import mplstereonet





######################### Funciones #################################
def load_data(uploaded_file):#Funcion para cargar datos
    if uploaded_file is not None:#si uplode es diferente entonces
        try:#intento
            df = pd.read_csv(uploaded_file, sep=separador)
        except UnicodeDecodeError as e:#SALTA ERROR
            st.error(f"error loading log.las: {e}")
    else:
        pass




###################### SiderBar ########################################
st.sidebar.markdown('# Exploración de data CSV (Modelo de Bloques y Taladros de exploración)')
st.sidebar.write('Para usar esta app escoja un archivo en formato CSV para la exploración de datos.')
separador=st.sidebar.selectbox(
'¿Cuál es el separador del CSV?',
(',',";",'/',' '))
uploadedfile = st.sidebar.file_uploader(' ', type=['.csv'])#PARA CARGAR MI ARCHIVO
st.sidebar.title('Menú de opciones')
options = st.sidebar.radio('Seleccione una página:', 
    ['Menú principal', 'Tablas de datos','Graficos'])
df = load_data(uploadedfile)#LO QUE CARGO LO METO A LA FUNCION






#################### Lista de Menus ###################
if options == 'Menú principal':
    pass

elif options == 'Tablas de datos':
    pass

elif options == 'Graficos':
    pass

import numpy as np

pweb = """<a href='http://www.idlmining.com/' target="_blank">http://www.idlmining.com/</a>"""
st.title('Estereo Mining - Version 0.1.3')
st.write('## La aplicación está diseñada para el análisis interactivo de datos geológicos basados en la Proyeccion estereografica. La aplicacion es capaz de muchas aplicaciones y está diseñado tanto para el usuario novato como para el usuario experimentado de la proyección estereográfica que desea utilizar herramientas gratuitas basadas en librerías de Python')
st.write('### Created by Cristian Cartagena Matos')
st.write(f'\nSi quieres saber mas sobre programación, el código o inteligencia artificial visita nuestra pagina web : {pweb}.', unsafe_allow_html=True)
#st.write('### Si quieres saber mas sobre programación, el código o inteligencia artificial visita nuestra pagina web ')



import matplotlib.pyplot as plt
import mplstereonet

fig = plt.figure()

# Make an "equal area" (a.k.a. "Schmidt") stereonet
# (Lambert Azimuthal Equal Area Projection)
ax1 = fig.add_subplot(1,2,1, projection='equal_area_stereonet')

# Make an "equal angle" (a.k.a. "Wulff" or "True") stereonet
# (Stereographic projection)
ax2 = fig.add_subplot(1,2,2, projection='equal_angle_stereonet')

# Plot the same thing on both
for ax in [ax1, ax2]:
    ax.grid(True)
    ax.set_azimuth_ticklabels([])
    ax.plane(315, 20)
    ax.line([20, 30, 40], [110, 265, 170])

ax1.set_title('Equal Area (a.k.a. "Schmidt")')
ax2.set_title('Equal Angle (a.k.a. "Wulff")')

# Make the subplots fit a bit more compactly (purely cosmetic)
fig.subplots_adjust(hspace=0, wspace=0.05, left=0.01, bottom=0.1, right=0.99)

fig.suptitle('Comparison of Equal Area and Equal Angle Stereonets\n'
             'Same Data Plotted on Both', y=0.1)
plt.show()
st.pyplot(fig)








fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='stereonet')

strike, dip = 315, 30
ax.plane(strike, dip, 'g-', linewidth=2)
ax.pole(strike, dip, 'g^', markersize=18)
ax.rake(strike, dip, -25)
ax.grid()
st.pyplot(fig2)
