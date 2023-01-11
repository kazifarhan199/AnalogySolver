import numpy as np
import pandas as pd

def solve_analogy_problem(w1, w2, w3):
    """
        This function solves the analogy and returns top 10 picks for the answer
        The analogy will be of the type
            A {w1} to a {w2} as a {w3} is to a {?}

        INPUT:
            w1 - First word
            w2 - second word
            w3 - third word
        OUTPUT:
            results - A list of tuples where 1st element is the word and 2nd element is the confidance
                [(word, rating), (word, rating),....]
    """

    glove = pd.read_csv('glove.6B.100d.txt', sep=" ", quoting=3, header=None, index_col=0)

    def similarity(a, b):
        return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))

    try:
        g_w1 = glove.loc[w1].values
    except:
        return [f"Sorry we do not have the word {w1} in out word list", ]
    try:
        g_w2 = glove.loc[w2].values
    except:
        return [f"Sorry we do not have the word {w2} in out word list", ]
    try:
        g_w3 = glove.loc[w3].values
    except:
        return [f"Sorry we do not have the word {w3} in out word list", ]
    
    est = g_w2 -  g_w1 + g_w3

    val = np.array([similarity(est, value) for value in glove.values])

    results = []
    s = np.sort(val)[::-1]
    for i in range(5):
        v = s[i]
        results.append((glove.index[list(val).index(v)], v),)
    
    return results