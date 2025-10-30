import sys
import os
# Agregar el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sum import sumar

def test_sumar_positivos():
    assert sumar(2, 3) == 5

def test_sumar_negativos_y_positivos():
    assert sumar(-1, 4) == 3

def test_sumar_cero():
    assert sumar(0, 0) == 0

if __name__ == "__main__":
    test_sumar_positivos()
    test_sumar_negativos_y_positivos()
    test_sumar_cero()
    print("¡Todos los tests pasaron!")