"""
Funciones usadas en la app dash
"""
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Función para obtener el sentimiento de un texto
def obtener_sentimiento(texto):
    analyzer = SentimentIntensityAnalyzer()
        return analyzer.polarity_scores(texto)["compound"]
