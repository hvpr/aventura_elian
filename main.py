def hacer_pregunta(pregunta, opciones, respuesta_correcta):
    print(pregunta)
    for i, opcion in enumerate(opciones):
        print(f"{chr(65 + i)}) {opcion}")
    
    while True:
        respuesta = input("Tu respuesta (A/B/C/D): ").upper()
        if respuesta in ['A', 'B', 'C', 'D']:
            return respuesta == respuesta_correcta
        else:
            print("Por favor, ingresa A, B, C o D.")

def jugar_capitulo(numero, titulo, texto, pregunta, opciones, respuesta_correcta, recompensa):
    print(f"\nCapítulo {numero}: {titulo}")
    print(texto)
    
    if hacer_pregunta(pregunta, opciones, respuesta_correcta):
        print(f"¡Correcto! {recompensa}")
        return True
    else:
        print("Incorrecto. Inténtalo de nuevo.")
        return False

def juego_aventura_elian():
    print("Bienvenido a la aventura de Elian en busca del 'Libro de la Sabiduría'")
    
    capitulos = [
        {
            "numero": 1,
            "titulo": "La Revelación de Tertuliano",
            "texto": "Elian llega a la biblioteca de la ciudad, donde se encuentra con un anciano sabio que le habla sobre la importancia de los grandes pensadores.",
            "pregunta": "¿Qué figura histórica se menciona como un renovador de la prosa latina y que recibió su formación en escuelas clásicas?",
            "opciones": ["San Juan Cristóstomo", "Tertuliano", "San Agustín", "Orígenes"],
            "respuesta_correcta": "B",
            "recompensa": "El anciano te entrega un mapa que te guiará a la siguiente etapa de tu viaje."
        },
        {
            "numero": 2,
            "titulo": "La Didascalia Apostólica",
            "texto": "Siguiendo el mapa, Elian llega a un monasterio donde los monjes estudian la Didascalia Apostólica. Uno de los monjes le plantea un dilema:",
            "pregunta": "¿Qué recomendación se hace en la Didascalia Apostólica respecto a los libros paganos?",
            "opciones": ["Se deben estudiar para entender la cultura.", "Se deben evitar completamente.", "Se pueden leer si se interpretan correctamente.", "Son necesarios para la educación cristiana."],
            "respuesta_correcta": "B",
            "recompensa": "El monje te revela un pasaje secreto que te llevará a la siguiente parte de tu aventura."
        },
        {
            "numero": 3,
            "titulo": "El Maestro y sus Alumnos",
            "texto": "Elian se encuentra en una escuela donde un maestro le enseña sobre la educación hebrea. El maestro le pregunta:",
            "pregunta": "¿Cuál es el máximo número de alumnos que se recomienda que un maestro tenga según las enseñanzas hebreas?",
            "opciones": ["10", "25", "50", "100"],
            "respuesta_correcta": "B",
            "recompensa": "El maestro te otorga un amuleto que te dará sabiduría en momentos de necesidad."
        },
        {
            "numero": 4,
            "titulo": "El Encuentro con la Didascalia",
            "texto": "Elian continúa su viaje y se encuentra con un grupo de eruditos que discuten sobre la Didascalia Apostólica. Uno de ellos le pregunta:",
            "pregunta": "¿Qué documento pedagógico del siglo III se menciona en el texto?",
            "opciones": ["La Biblia", "La Didascalia Apostólica", "La Tora", "El Talmud"],
            "respuesta_correcta": "B",
            "recompensa": "Los eruditos te ofrecen un libro antiguo que contiene fragmentos del conocimiento perdido."
        },
        {
            "numero": 5,
            "titulo": "La Influencia de la Retórica",
            "texto": "Finalmente, Elian llega a una plaza donde se celebra un debate sobre la educación. Un orador le pregunta:",
            "pregunta": "¿Qué aspecto de la educación cristiana se destaca en el siglo IV según el documento?",
            "opciones": ["La creación de escuelas exclusivamente cristianas.", "La influencia de la retórica clásica en la enseñanza.", "La prohibición total de la literatura pagana.", "La enseñanza de la Biblia como único texto."],
            "respuesta_correcta": "B",
            "recompensa": "El orador te revela la ubicación del 'Libro de la Sabiduría'."
        }
    ]
    
    for capitulo in capitulos:
        while not jugar_capitulo(**capitulo):
            pass
    
    print("\n¡Felicidades! Has completado tu búsqueda y encontrado el 'Libro de la Sabiduría'. Tu conocimiento sobre la pedagogía cristiana y la historia antigua te ha guiado exitosamente en tu aventura.")

# Ejecuta el juego
juego_aventura_elian()
