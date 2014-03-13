# -*- coding: utf-8 -*-
import requests
from lxml import etree
import webbrowser
from suds.client import Client
import webbrowser

linea = raw_input("Introduzca una linea: ")

cliente = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)

respuesta = cliente.service.GetStatusLinea('%s' % linea)

raiz = etree.fromstring(respuesta.encode("utf-8"))	
raiz2 = raiz[0][0]

tempuri = "{http://tempuri.org/}"
pretty = etree.tostring(raiz2, pretty_print=True)

indice = raiz2.find(tempuri+"GetStatusLineaResult")
ncochesact = indice.find(tempuri+"activos")
ncoches2 = ncochesact.text
frecok = indice.find(tempuri+"frec_bien")
frecok2 = frecok.text
incigrav = indice.find(tempuri+"graves")
incigrav2 = incigrav.text

print " "
print "Número de coches activos: %s" % ncoches2
print "Número de coches con frecuencia correcta: %s" % frecok2
print "Número de incidencias graves: %s" % incigrav2
print " "
print "Datos oficiales de TUSSAM."

# los que van bien de frecuencia y el número de incidencias graves de la línea.
#	raiz = etree.fromstring(respuesta.text.encode("utf-8"))	
	
#	city = raiz.find("city")
#	city.attrib["name"]
#	tempemin = raiz.find("temperature")
#	tempemin2 = round(float(tempemin.attrib["min"]),1)
#	tempemax = raiz.find("temperature")
#	tempemax2 = round(float(tempemax.attrib["max"]),1)
#	viento = raiz.find("wind/speed")
#	viento2 = round(float(viento.attrib["value"]),1)
#	direccion = raiz.find("wind/direction")
#	direccion2 = direccion.attrib["code"]
#	tempe_min.append(tempemin2)
#	tempe_max.append(tempemax2)
#	viento_vel.append(viento2)
#	viento_direc.append(direccion2)
	

#fichero = open('tiempo.html','w')
#fichero.write(tiempo)
#fichero.close()
#webbrowser.open("tiempo.html")	
