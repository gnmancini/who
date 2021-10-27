import os
import time
import dbus

def chequeo():
    loop = True
    while (loop):  
        result = os.popen('w | tail -n +3 | wc -l').read()
        #print(result)
        if int(result) >= 1 :
            print(result)
            intruder_message()
        time.sleep(60)

def intruder_message():
    bus = dbus.SessionBus()
    notify_object = bus.get_object('org.freedesktop.Notifications','/org/freedesktop/Notifications')
    notify_interface = dbus.Interface(notify_object,'org.freedesktop.Notifications')
    titulo = "IMPORTANT!!!"
    cuerpo = "There are more than one user logged in the system."
    tiempo = 10000 # milisegundos. Si especificamos 0, se espera a que el usuario lo cierre
    notify_id = notify_interface.Notify("DBus Test", 0, "gtk-ok", titulo, cuerpo, "", {}, tiempo)
 
    # Imprimimos el ID de esta notificacion
    #print ("El ID es: ", notify_id)

chequeo()
