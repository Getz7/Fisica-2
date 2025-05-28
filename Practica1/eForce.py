# Importamos las librerías necesarias
import math                 # Para operaciones matemáticas como raíz cuadrada
import matplotlib.pyplot as plt   # Para graficar el sistema


def calcular_fuerza(q1, q2, x2, y2):
    # Constante de Coulomb (N·m²/C²)
    k = 9 * (10**9)
    

    # Coordenadas relativas: diferencia de posición entre Q2 y Q1
    dx = x2      # Q1 está en el origen, así que dx = x2 - 0
    dy = y2  
    r = math.sqrt(dx**2 + dy**2)  # Distancia entre las cargas

    # Verifica que las cargas no estén en el mismo punto
    if r == 0:
        raise ValueError("Las cargas no pueden estar en la misma posición (división por cero).")
    
    # Magnitud de la fuerza (sin dirección todavía)
    magnitud = k * abs(q1 * q2) / r**2

   # Calculamos el vector unitario (dirección del vector)
    ux = dx / r  # componente x del vector unitario
    uy = dy / r  # componente y del vector unitario


    # Determina si la fuerza es de repulsión (+) o atracción (-)
    signo = 1 if q1 * q2 > 0 else -1  # Si los signos son iguales: repulsión (positivo)

    fx = signo * magnitud * ux
    fy = signo * magnitud * uy

     # Devolvemos el vector fuerza como dos componentes
    return fx, fy

def graficar(q1, q2, x2, y2, fx, fy):
    plt.figure(figsize=(6, 6))
    plt.scatter(0, 0, color='blue', label='Q1 (en el origen)')
    plt.scatter(x2, y2, color='green', label='Q2')
    plt.quiver(x2, y2, fx, fy, angles='xy', scale_units='xy', scale=1e-6, color='red', label='Fuerza sobre Q2')
    plt.xlim(x2 - 10, x2 + 10)
    plt.ylim(y2 - 10, y2 + 10)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Fuerza eléctrica entre dos cargas')
    plt.grid(True)
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def main():
    print("Cálculo de Fuerza Eléctrica entre dos cargas puntuales")
    try:
        #Toma de datos
        q1 = float(input("Ingresa el valor de la carga Q1 (Coulombs): "))
        q2 = float(input("Ingresa el valor de la carga Q2 (Coulombs): "))
        x2 = float(input("Ingresa la coordenada x de Q2 (en metros): "))
        y2 = float(input("Ingresa la coordenada y de Q2 (en metros): "))
        
        fx, fy = calcular_fuerza(q1, q2, x2, y2)
        print(f"\nVector de Fuerza sobre Q2: F = ({fx:.2e}, {fy:.2e}) N")
        
        graficar(q1, q2, x2, y2, fx, fy)
        
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
