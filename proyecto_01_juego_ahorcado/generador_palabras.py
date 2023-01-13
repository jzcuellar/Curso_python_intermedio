palabras = ["computadora", "tigre", "silla", "estufa", "reloj", "guitarra", 
            "sándwich", "televisión", "edificio", "mapa", "lápiz", "cama", 
            "mesa", "libro", "carro", "flor", "tren", "oso", "zanahoria", 
            "relámpago", "televisor", "vaca", "plátano", "bicicleta", "avión", 
            "murciélago", "bote", "mesa de dibujo", "sopa", "abeja", "pájaro", 
            "tren eléctrico", "vaso", "mesa de billar", "cebra", "vacaciones", 
            "pescado", "hormiga", "torre", "gato", "cuaderno", "reloj de sol", 
            "rana", "zapato", "cebra", "tijera", "árbol", "silla de oficina", 
            "luna", "caja", "perro", "vacaciones", "bala", "océano", "vacaciones", 
            "reloj de pulsera", "silla de ruedas", "bolsa", "lago", "caja de lápices", 
            "mesa de comedor", "abanico", "cuchillo", "tijeras de podar", "bolsa de viaje", 
            "cebra", "silla de playa", "lámpara", "lápiz labial", "regla", "plátano", 
            "mesa de noche", "reloj despertador", "abanico de techo", "carne", "caja de cerillas", 
            "cama de agua", "televisor", "helado", "pájaro tropical", "mesa de billar", 
            "silla de jardín", "vaso de agua", "lapicero", "reloj de bolsillo", "mesa de dibujo", 
            "silla de ruedas eléctrica", "tijeras de jardinería", "computadora portátil", 
            "reloj de pared", "caja de herramientas", "lámpara de escritorio", "televisor de pantalla plana",
            "abanico de techo","mesa de comedor de exterior","caja de arena para gatos","lápiz de color","cama de agua",
            "caja de juguetes","silla de jardín"]

def write():
    with open("./proyecto_01_juego_ahorcado/palabras.txt", "w", encoding="utf-8") as f:
        for name in palabras:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__ =='__main__':
    run()
