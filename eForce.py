import math
import matplotlib.pyplot as plt

def calcular_fuerza(q1, q2, x2, y2):
    # Constante de Coulomb (N·m²/C²)
    k = 9 * (10**9)
    
    # Vector de posición de Q2 respecto a Q1 (que está en el origen)
    dx = x2
    dy = y2
    r = math.sqrt(dx**2 + dy**2)

    if r == 0:
        raise ValueError("Las cargas no pueden estar en la misma posición (división por cero).")
    
    # Magnitud de la fuerza (Ley de Coulomb)
    magnitud = k * abs(q1 * q2) / r**2

    # Dirección: vector unitario
    ux = dx / r
    uy = dy / r

    # Dirección del vector de fuerza (repulsión o atracción)
    signo = 1 if q1 * q2 > 0 else -1

    fx = signo * magnitud * ux
    fy = signo * magnitud * uy

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
