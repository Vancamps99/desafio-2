from .models import Tarea, SubTarea

# Función para recuperar todas las tareas y sus subtareas que no están eliminadas
def recupera_tareas_y_sub_tareas():
    # Obtener todas las tareas que no están eliminadas
    lista_tareas = Tarea.objects.filter(eliminada=False)
    arreglo_tareas_subtareas = []

    for tarea in lista_tareas:
        # Obtener todas las subtareas de la tarea actual que no están eliminadas
        sub_tareas = tarea.subtareas.filter(eliminada=False)
        dicc_tareas = {
            'tarea': tarea,
            'sub_tareas': sub_tareas
        }
        arreglo_tareas_subtareas.append(dicc_tareas)
            
    return arreglo_tareas_subtareas

# Función para crear una nueva tarea
def crear_nueva_tarea(pdescripcion='', peliminada=False):
    # Crear una instancia del modelo Tarea sin guardarla en la base de datos aún
    tarea = Tarea(descripcion=pdescripcion, eliminada=peliminada)
    
    # Imprimir el ID de la tarea antes de guardarla (debería ser None)
    print(tarea.id)  
    
    # Guardar la instancia en la base de datos
    tarea.save()
    
    # Imprimir el ID de la tarea después de guardarla (debería tener un valor)
    print(tarea.id) 
    
    return recupera_tareas_y_sub_tareas()

# Función para crear una nueva subtarea asociada a una tarea existente
def crear_sub_tarea(tarea_id, pdescripcion=''):
    # Obtener la tarea existente por su ID
    obj_tarea = Tarea.objects.get(id=tarea_id)
    
    # Crear una nueva instancia de SubTarea asociada con la tarea obtenida
    subtarea = SubTarea(descripcion=pdescripcion, eliminada=False, tarea=obj_tarea)
    
    # Guardar la subtarea en la base de datos
    subtarea.save()
    
    return recupera_tareas_y_sub_tareas()

# Función para eliminar lógicamente una tarea
def elimina_tarea(tarea_id):
    # Obtener la tarea por su ID
    obj_tarea = Tarea.objects.get(pk=tarea_id)
    
    # Marcar la tarea como eliminada
    obj_tarea.eliminada = True
    
    # Guardar los cambios en la base de datos
    obj_tarea.save() 
    
    return recupera_tareas_y_sub_tareas()

# Función para eliminar lógicamente una subtarea
def elimina_sub_tarea(subtarea_id):
    # Obtener la subtarea por su ID
    obj_subtarea = SubTarea.objects.get(pk=subtarea_id)
    
    # Marcar la subtarea como eliminada
    obj_subtarea.eliminada = True
    
    # Guardar los cambios en la base de datos
    obj_subtarea.save() 
    
    return recupera_tareas_y_sub_tareas()

# Función para imprimir en pantalla (definir más adelante)
def imprimir_en_pantalla():
    # Recuperar las tareas y subtareas
    arreglo_tareas_subtareas = recupera_tareas_y_sub_tareas()

    # Imprimir las tareas y sus subtareas
    for idx, dicc_tareas in enumerate(arreglo_tareas_subtareas, start=1):
        tarea = dicc_tareas['tarea']
        sub_tareas = dicc_tareas['sub_tareas']
        
        # Imprimir la tarea
        print(f"[{idx}] {tarea.descripcion}")
        
        # Imprimir las subtareas de la tarea
        for sub_idx, sub_tarea in enumerate(sub_tareas, start=1):
            print(f".... [{sub_tarea.id}] {sub_tarea.descripcion}")
