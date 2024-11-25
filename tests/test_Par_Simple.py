import unittest
from app.scripts.par import es_par

class TestEsParConExcepciones(unittest.TestCase):
    def test_numero_par(self):
        self.assertTrue(es_par(4))  # 4 es par
        self.assertTrue(es_par(0))  # 0 es par
    
    def test_numero_impar(self):
        self.assertFalse(es_par(3))  # 3 es impar
        self.assertFalse(es_par(-1))  # -1 es impar
    
    def test_numeros_negativos(self):
        self.assertTrue(es_par(-2))  # -2 es par
        self.assertFalse(es_par(-3))  # -3 es impar
    
    def test_excepcion_tipo_incorrecto(self):
        with self.assertRaises(TypeError):  # "texto" no es válido
            es_par("texto")
        with self.assertRaises(TypeError):  # Una lista no es válida
            es_par([1, 2, 3])
    
    def test_float(self):
        self.assertFalse(es_par(3.5))  # 3.5 es impar
        self.assertTrue(es_par(4.0))  # 4.0 es considerado par porque es múltiplo de 2

if __name__ == "__main__":
    unittest.main()