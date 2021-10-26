#!/usr/bin/env python
 
import dbus
 
# Inicializando el bus de tipo session (se comunica entre aplicaciones)
bus = dbus.SessionBus()
 
# Se obtiene el objeto Notifications (es el encargado de las notificaciones)
notify_object = bus.get_object('org.freedesktop.Notifications','/org/freedesktop/Notifications')
 
# Se obtiene una interface del tipo Notificatios
notify_interface = dbus.Interface(notify_object,'org.freedesktop.Notifications')
 
# Finalmente lanzamos la notificacion
# Nota: el gtk-ok muestra un icono de ok en el mensaje, puede ser cualquier otro
# como gtk-cut (muestra una tijera), gtk-connect (una conexion), etc.
titulo = "Mensaje de prueba"
cuerpo = "Este es un mensaje enviado desde Python con dbus"
tiempo = 10000 # milisegundos. Si especificamos 0, se espera a que el usuario lo cierre
notify_id = notify_interface.Notify("DBus Test", 0, "gtk-ok", titulo, cuerpo, "", {}, tiempo)
 
# Imprimimos el ID de esta notificacion
print ("El ID es: ", notify_id)
