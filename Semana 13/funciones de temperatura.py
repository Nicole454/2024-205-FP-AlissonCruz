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
def calcular_temperatura_promedio(temperatura):
    promedio = {}

    for ciudad in temperatura:
        total_temperatura = 0
        total_dias = 0

        for semana in temperatura[ciudad]["semanas"]:
            for dia in semana:
                total_temperatura += dia["temp"]
                total_dias += 1

        if total_dias > 0:
            promedio_ciudad = total_temperatura / total_dias
            promedio[ciudad] = round(promedio_ciudad, 2)

    return promedio

datos_temperatura = {
    "Quito": {
        "semanas": [
            [{"temp": 18}, {"temp": 20}, {"temp": 19}, {"temp": 21}],
            [{"temp": 22}, {"temp": 19}, {"temp": 20}, {"temp": 18}]
        ]
    },
    "Guayaquil": {
        "semanas": [
            [{"temp": 30}, {"temp": 32}, {"temp": 31}, {"temp": 29}],
            [{"temp": 28}, {"temp": 30}, {"temp": 29}, {"temp": 31}]
        ]
    },
    "Cuenca": {
        "semanas": [
            [{"temp": 25}, {"temp": 26}, {"temp": 24}, {"temp": 23}],
            [{"temp": 22}, {"temp": 21}, {"temp": 20}, {"temp": 19}]
        ]
    }
}

resultado = calcular_temperatura_promedio(datos_temperatura)
print(resultado)

