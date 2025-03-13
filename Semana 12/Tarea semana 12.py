#Creacion de matriz para almacenar los datos de la temperatura
#Primera dimencion: Ciudades (Quito,Guyllaquil,Cuenca)
#Segunda dimencion: Dias de ma semana (7 Dias)
#Tercera dimencion: semanas (4 semanas)
temperaturas = [
    {
        "ciudad": "Quito",
        "semana": [
            [  # Semana 1
                {"day": "lunes", "temp": 78},
                {"day": "martes", "temp": 70},
                {"day": "miercoles", "temp": 80},
                {"day": "jueves", "temp": 86},
                {"day": "viernes", "temp": 96},
                {"day": "sábado", "temp": 85},
                {"day": "domingo", "temp": 76},
            ],
            [  # Semana 2
                {"day": "lunes", "temp": 72},
                {"day": "martes", "temp": 50},
                {"day": "miercoles", "temp": 60},
                {"day": "jueves", "temp": 85},
                {"day": "viernes", "temp": 86},
                {"day": "sábado", "temp": 89},
                {"day": "domingo", "temp": 75},
            ],
            [  # Semana 3
                {"day": "lunes", "temp": 90},
                {"day": "martes", "temp": 78},
                {"day": "miercoles", "temp": 89},
                {"day": "jueves", "temp": 56},
                {"day": "viernes", "temp": 86},
                {"day": "sábado", "temp": 95},
                {"day": "domingo", "temp": 66},
            ],
            [  # Semana 4
                {"day": "lunes", "temp": 60},
                {"day": "martes", "temp": 74},
                {"day": "miercoles", "temp": 59},
                {"day": "jueves", "temp": 86},
                {"day": "viernes", "temp": 96},
                {"day": "sábado", "temp": 55},
                {"day": "domingo", "temp": 76},
            ],
        ],
    },
    {
        "ciudad": "Guayaquil",
        "semana": [
            [  # Semana 1
                {"day": "lunes", "temp": 78},
                {"day": "martes", "temp": 70},
                {"day": "miercoles", "temp": 80},
                {"day": "jueves", "temp": 86},
                {"day": "viernes", "temp": 96},
                {"day": "sábado", "temp": 85},
                {"day": "domingo", "temp": 76},
            ],
            [  # Semana 2
                {"day": "lunes", "temp": 72},
                {"day": "martes", "temp": 50},
                {"day": "miercoles", "temp": 60},
                {"day": "jueves", "temp": 85},
                {"day": "viernes", "temp": 86},
                {"day": "sábado", "temp": 89},
                {"day": "domingo", "temp": 75},
            ],
            [  # Semana 3
                {"day": "lunes", "temp": 90},
                {"day": "martes", "temp": 78},
                {"day": "miercoles", "temp": 89},
                {"day": "jueves", "temp": 56},
                {"day": "viernes", "temp": 86},
                {"day": "sábado", "temp": 95},
                {"day": "domingo", "temp": 66},
            ],
            [  # Semana 4
                {"day": "lunes", "temp": 60},
                {"day": "martes", "temp": 74},
                {"day": "miercoles", "temp": 59},
                {"day": "jueves", "temp": 86},
                {"day": "viernes", "temp": 96},
                {"day": "sábado", "temp": 55},
                {"day": "domingo", "temp": 76},
            ],
        ],
    },
    {
        "ciudad": "Cuenca",
        "semana": [
            [  # Semana 1
                {"day": "lunes", "temp": 78},
                {"day": "martes", "temp": 70},
                {"day": "miercoles", "temp": 80},
                {"day": "jueves", "temp": 86},
                {"day": "viernes", "temp": 96},
                {"day": "sábado", "temp": 85},
                {"day": "domingo", "temp": 76},
            ],
            [  # Semana 2
                {"day": "lunes", "temp": 72},
                {"day": "martes", "temp": 50},
                {"day": "miercoles", "temp": 60},
                {"day": "jueves", "temp": 85},
                {"day": "viernes", "temp": 86},
                {"day": "sábado", "temp": 89},
                {"day": "domingo", "temp": 75},
            ],
            [  # Semana 3
                {"day": "lunes", "temp": 90},
                {"day": "martes", "temp": 78},
                {"day": "miercoles", "temp": 89},
                {"day": "jueves", "temp": 56},
                {"day": "viernes", "temp": 86},
                {"day": "sábado", "temp": 95},
                {"day": "domingo", "temp": 66},
            ],
            [  # Semana 4
                {"day": "lunes", "temp": 60},
                {"day": "martes", "temp": 74},
                {"day": "miercoles", "temp": 59},
                {"day": "jueves", "temp": 86},
                {"day": "viernes", "temp": 96},
                {"day": "sábado", "temp": 55},
                {"day": "domingo", "temp": 76},
            ],
        ],
    },
]

for ciudad in temperaturas:
    print(f"Promedio de temperaturas en {ciudad['ciudad']}:")
    for semana_idx, semana in enumerate(ciudad['semana']):
        suma_temperaturas = sum(dia["temp"] for dia in semana)  # Corrección aquí
        promedio = suma_temperaturas / len(semana)  # Se calcula el promedio correctamente
        print(f"  Semana {semana_idx + 1}: {promedio:.2f} grados")  # Mensaje formateado correctamente
