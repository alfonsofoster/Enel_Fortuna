import requests,locale, configparser, outlook_email
from datetime import date, timedelta, datetime
from pathlib import Path
import 

# https://www.cnd.com.pa/privado/descargar_archivo.php?nombre=preliminar_agosto2017_egef_fortuna.xls&tipo_informe=55&username=true&ano=2017&mes=Agosto&dia=24

config = configparser.ConfigParser()
config.read('config.ini')

usr = config['cnd.com.pa']['usr']
pwd = config['cnd.com.pa']['pwd']

cnd_url = 'https://www.cnd.com.pa/privado/descargar_archivo.php?'
nombre_archivo = date.today()
nombre_archivo_web = 'preliminar_'+ 'month_in_spanish' + nombre_archivo.strftime('%Y') + '_egef_fortuna.xls'

print(nombre_archivo_web)
peso_archivo = 0
dias_sin_archivos = 0
hoy_archivo = date.today()
while (peso_archivo < 1):
    ano, mes, dia = hoy_archivo.strftime("%Y"), 'month_in_spanish', hoy_archivo.strftime("%d")
    r = requests.get(cnd_url + 'nombre=' + nombre_archivo_web + '&tipo_informe=55&username=true&ano=' + ano + '&mes=' + mes + '&dia=' + dia,auth=(usr, pwd))
    peso_archivo = len(r.content) / 1024
    if peso_archivo < 1:
        print('No hay archivos para el dia: %s' % (hoy_archivo))        
        hoy_archivo = hoy_archivo - timedelta(1)
        dias_sin_archivos += 1
        if dias_sin_archivos > 10:
            print('No Hay Archivos en los 10 ultimos dias?... La Contrasena es la Correcta?... La Ruta ha cambiado?...Revisar el Sitio!')
            break
    else:
        print('Se encontro archivos para el dia: %s , el peso del archivo es: %.2f kb' % (hoy_archivo, peso_archivo))
        break

dia_en_archivo = hoy_archivo.strftime('%d%m%Y')
verificar_archivo_en_ruta = Path('C:\path\to\check\file\Preliminar_' + dia_en_archivo + '_egef_fortuna.xls')
if verificar_archivo_en_ruta.exists():
    print('Archivo existe!')

else:
    with open('C:\path\to\check\file\Preliminar_' + dia_en_archivo + '_egef_fortuna.xls', 'wb') as output:
        output.write(r.content)

    print('Archivo nuevo guardado!')
	outlook_email.send_email("Archivo nuevo guardado!")

print('Termino Todo el Script')

