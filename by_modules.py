

import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming
m= np.array([
    [0,  5, 4, 10],
    [5,  0, 8,  5],
    [4,  8, 0,  3],
    [10, 5, 3,  0]
])
p,s = solve_tsp_dynamic_programming(m)
print(p,s)