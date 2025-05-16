dispositivos = [
    {
        "id_dispositivo": 1,
        "nombre": "Habitacion principal",
        "tipo": "Luz interior",
        "estado": "Apagado"
    },
    {
        "id_dispositivo": 2,
        "nombre": "Jardin",
        "tipo": "Luz exterior",
        "estado": "Apagado"
    }
]

def listar_dispositivos():
    return dispositivos

def agregar_dispositivo(nombre_dispositivo, tipo, estado):
    if not nombre_dispositivo or not tipo or not estado:
        return "Error: Debes ingresar un nombre, tipo y estado."

    nuevo_dispositivo = {
        "id_dispositivo":  max([d["id_dispositivo"] for d in dispositivos]) + 1,
        "nombre": nombre_dispositivo,
        "tipo": tipo,
        "estado": estado
    }
    
    dispositivos.append(nuevo_dispositivo)
    return (f"Se agregó el dispositivo: {nombre_dispositivo}.")

def buscar_dispositivo(nombre_dispositivo):
    if not dispositivos:
        return "No se encontraron dispositivos."
    for d in dispositivos:
        if d["nombre"].lower() == nombre_dispositivo.lower():
            return (f"Dispositivo encontrado: ID: {d['id_dispositivo']} - {d['nombre']} ({d['tipo']}) - Estado: {d["estado"]}")

def editar_dispositivo(nombre_original, nuevo_nombre, nuevo_tipo, nuevo_estado):
    for d in dispositivos:
        if d["nombre"].lower() == nombre_original.lower():
            if nuevo_nombre:
                d["nombre"] = nuevo_nombre
            if nuevo_tipo:
                d["tipo"] = nuevo_tipo
            if nuevo_estado:
                d["estado"] = nuevo_estado
            return f"Dispositivo actualizado: ID: {d['id_dispositivo']} - {d['nombre']} ({d['tipo']}) - Estado: {d['estado']}"
    return "Dispositivo no encontrado."
        
def eliminar_dispositivo(nombre_dispositivo):
    if not dispositivos:
        return "No se encontraron dispositivos."
    for d in dispositivos:
        if d["nombre"].lower() == nombre_dispositivo.lower():
            dispositivos.remove(d)
            return (f"Dispositivo eliminado: ID: {nombre_dispositivo}")

