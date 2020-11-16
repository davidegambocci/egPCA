from typing import List, Callable
import numpy as np


#
def sum_of_squares(x: List[float]) -> float:
    """Esempio di funzione: somma di quadrati"""
    return sum([x_i **2 for x_i in x])


#
def df(f: Callable, x: List[float], h=0.001) -> List[float]:
    """In output: la derivata della funzione f nel punto/vettore x"""
    
    df_value = []
    for ind in range(len(x)):
        w = [x_i + h * (x.index(x_i) == ind) for x_i in x]
        dfdi = (f(w) - f(x)) / h
        df_value.append(dfdi)
    
    return df_value



# fixme: il vettore iniziale x deve essere un random start: lo mando dall'esterno?
def gradient_descend(f: Callable, x: List[float], step=0.01, epochs=1000) -> List[float]:
    """Gradient Descend"""

    for _ in range(epochs):
        dx = df(f, x)
        x = [x[i] + step * dx[i] for i in range(len(x))]

    return x  


# --- Test
assert sum_of_squares([3, 4]) == 25
np.testing.assert_almost_equal(df(sum_of_squares, [3, 4]), [6, 8], decimal=3)
np.testing.assert_almost_equal(df(sum_of_squares, [25, 27]), [50, 54], decimal=3)
np.testing.assert_almost_equal(gradient_descend(sum_of_squares, [25, 27, -15], step=-0.01), [0, 0, 0], decimal=3)