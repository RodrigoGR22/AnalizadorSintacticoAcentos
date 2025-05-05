# -*- coding: utf-8 -*-
import sys
import datetime
import re
from antlr4 import *

from antlr4.TokenStreamRewriter import TokenStreamRewriter

# --- Importación de Clases Generadas por ANTLR ---
try:
    from SpanishAccentLexer import SpanishAccentLexer
    from SpanishAccentParser import SpanishAccentParser
    from SpanishAccentListener import SpanishAccentListener
except ImportError:
    print("Error: No se encontraron los archivos generados por ANTLR (Lexer, Parser, Listener).")
    # ... (mensaje de error completo) ...
    sys.exit(1)

# --- Constantes y Diccionarios ---

# 1. Mapa para acentos diacríticos contextuales (preguntas/exclamaciones)
CONTEXT_ACCENT_MAP = {
    "que": "qué", "como": "cómo", "cuando": "cuándo",
    "donde": "dónde", "quien": "quién", "cuanto": "cuánto",
    "paso": "pasó",
}

FIXED_ACCENT_DICT = {
    "accion": "acción", "cancion": "canción", "corazon": "corazón", "razon": "razón",
    "nacion": "nación", "avion": "avión", "camion": "camión", "leccion": "lección",
    "sofa": "sofá", "mama": "mamá", "papa": "papá",  # OJO: papa (tubérculo) no lleva
    "cafe": "café", "bebe": "bebé",  # OJO: bebe (verbo beber) no lleva
    "compas": "compás", "interes": "interés", "autobus": "autobús", "jamas": "jamás",  # Agudas terminadas en -s
    "arbol": "árbol", "cesped": "césped", "carcel": "cárcel", "lider": "líder",
    "dolar": "dólar", "azucar": "azúcar", "caracter": "carácter",  # Graves no terminadas en n, s, vocal
    "platano": "plátano", "telefono": "teléfono", "pagina": "página", "musica": "música",
    "numero": "número", "ultimo": "último", "plastico": "plástico", "lagrima": "lágrima",
    "maquina": "máquina", "america": "américa", "mexico": "méxico", "sabado": "sábado",
    "miercoles": "miércoles", "oxigeno": "oxígeno", "gramatica": "gramática", "matematicas": "matemáticas",
    "articulo": "artículo", "periodico": "periódico",  # Esdrújulas (siempre llevan tilde)
    "compramelo": " cómpramelo", "diciendomelo": "diciéndomelo",  # Sobresdrújulas
    "ingles": "inglés", "frances": "francés", "pais": "país", "maiz": "maíz",  # Países/Gentilicios y otros
    "dia": "día", "rio": "río", "tio": "tío", "tia": "tía", "baul": "baúl",  # Hiatos a-i-u con tónica en i-u
    "raiz": "raíz", "oido": "oído", "frio": "frío", "grua": "grúa", "ataud": "ataúd",
    "sonreir": "sonreír", "reir": "reír",  # Verbos en infinitivo con hiato
    "policia": "policía", "filosofia": "filosofía", "biologia": "biología",  # Sustantivos con hiato -ía
    "imagen": "imagen",  # Singular SIN tilde
    "imagenes": "imágenes",  # Plural CON tilde
    "joven": "joven",  # Singular SIN tilde
    "jovenes": "jóvenes",  # Plural CON tilde
    "examen": "examen",  # Singular SIN tilde
    "examenes": "exámenes",  # Plural CON tilde
    "crimen": "crimen",  # Singular SIN tilde
    "crimenes": "crímenes",  # Plural CON tilde
    "origen": "origen",  # Singular SIN tilde
    "origenes": "orígenes",  # Plural CON tilde
    "regimen": "régimen",  # Singular CON tilde
    "regimenes": "regímenes",  # Plural CON tilde
    "especimen": "espécimen",  # Singular CON tilde
    "especimenes": "especímenes",  # Plural CON tilde
    "volumen": "volumen",  # Singular SIN tilde
    "volumenes": "volúmenes",  # Plural CON tilde

    # Verbos comunes (formas que llevan acento fijo)
    "esta": "está",  # Verbo estar (él/ella/usted presente)
    "estas": "estás",  # Verbo estar (tú presente) - OJO: puede confundirse con adj. demostrativo 'estas'
    "estabamos": "estábamos", "estabais": "estabais", "estaban": "estaban",  # Estar Imperfecto
    "habia": "había", "habias": "habías", "habiamos": "habíamos", "habiais": "habíais", "habian": "habían",
    # Haber Imperfecto
    "tenia": "tenía", "tenias": "tenías", "teniamos": "teníamos", "teniais": "teníais", "tenian": "tenían",
    # Tener Imperfecto
    "comia": "comía", "comias": "comías", "comiamos": "comíamos", "comiais": "comíais", "comian": "comían",
    # Comer Imperfecto
    "vivia": "vivía", "vivias": "vivías", "viviamos": "vivíamos", "viviais": "vivíais", "vivian": "vivían",
    # Vivir Imperfecto
    "iba": "iba", "ibas": "ibas", "ibamos": "íbamos", "ibais": "ibais", "iban": "iban",
    # Ir Imperfecto (OJO: sólo 'íbamos')
    "veia": "veía", "veias": "veías", "veiamos": "veíamos", "veiais": "veíais", "veian": "veían",  # Ver Imperfecto
    "seria": "sería", "serias": "serías", "seriamos": "seríamos", "seriais": "seríais", "serian": "serían",
    # Ser Condicional
    "haria": "haría", "harias": "harías", "hariamos": "haríamos", "hariais": "haríais", "harian": "harían",
    # Hacer Condicional
    "podria": "podría", "podrias": "podrías", "podriamos": "podríamos", "podriais": "podríais", "podrian": "podrían",
    # Poder Condicional
    "comeria": "comería", "comerias": "comerías", "comeriamos": "comeríamos", "comeriais": "comeríais",
    "comerian": "comerían",  # Comer Condicional
    "viviria": "viviría", "vivirias": "vivirías", "viviriamos": "viviríamos", "viviriais": "viviríais",
    "vivirian": "vivirían",  # Vivir Condicional
    "compro": "compró", "vendo": "vendió", "salio": "salió", "entro": "entró", "hablo": "habló",
    # Pretérito Indefinido (él/ella/usted)
    "comio": "comió", "vivio": "vivió", "estudio": "estudió", "gano": "ganó", "perdio": "perdió",
    "subio": "subió", "bajo": "bajó", "corrio": "corrió", "abrio": "abrió", "cerro": "cerró",
    "sera": "será", "estara": "estará", "hara": "hará", "ira": "irá", "vera": "verá",  # Futuro Simple (él/ella/usted)
    "comera": "comerá", "vivira": "vivirá", "hablara": "hablará", "tendra": "tendrá", "podra": "podrá",
    "estes": "estés", "des": "dés",  # Presente subjuntivo (tú) - OJO: dé/de es diacrítico
    "vayas": "vayas", "sepas": "sepas",
    # Otros subjuntivos (tú) - Sin tilde usualmente, 'dés' y 'estés' son excepciones
    # OJO: Formas de vosotros en subjuntivo SÍ llevan tilde si son esdrújulas: estéis, deis (no), sepáis, vayáis
    "esteis": "estéis", "sepais": "sepáis", "vayais": "vayáis",
    "se": "sé",  # Verbo saber (yo presente) / Ser (imperativo tú) - Diacrítico

    # Adverbios comunes
    "tambien": "también", "ademas": "además", "aqui": "aquí", "alli": "allí", "alla": "allá",
    "asi": "así", "jamas": "jamás", "despues": "después", "quizas": "quizás", "ojala": "ojalá",
    "detras": "detrás",
    # Adverbios en -mente (conservan tilde si el adjetivo base la tenía)
    "rapidamente": "rápidamente", "facilmente": "fácilmente", "dificilmente": "difícilmente",
    "unicamente": "únicamente", "logicamente": "lógicamente", "practicamente": "prácticamente",
    "ultimamente": "últimamente", "habilmente": "hábilmente", "debilmente": "débilmente",
    " cortesmente": "cortésmente",

    # Adjetivos comunes
    "util": "útil", "inutil": "inútil", "facil": "fácil", "dificil": "difícil",
    "habil": "hábil", "debil": "débil", "rapido": "rápido", "ultimo": "último",
    "logico": "lógico", "practico": "práctico", "comun": "común",  # OJO: comunes no lleva
    "simpatico": "simpático", "antipatico": "antipático", "timido": "tímido",
    "penultimo": "penúltimo", "antepenultimo": "antepenúltimo",

    # Interrogativos / Exclamativos (SIEMPRE llevan tilde en pregunta/exclamación directa o indirecta)
    "que": "qué", "quien": "quién", "quienes": "quiénes",
    "cual": "cuál", "cuales": "cuáles",
    "cuando": "cuándo",
    "cuanto": "cuánto", "cuanta": "cuánta", "cuantos": "cuántos", "cuantas": "cuántas",
    "como": "cómo",
    "donde": "dónde", "adonde": "adónde",  # OJO: donde/adonde (relativos) no llevan

    # Acentos Diacríticos (para diferenciar palabras homófonas)
    "el": "él",  # el (artículo) vs él (pronombre personal) - Usar con precaución
    "tu": "tú",  # tu (posesivo) vs tú (pronombre personal) - Usar con precaución
    "mi": "mí",  # mi (posesivo/nota musical) vs mí (pronombre personal) - Usar con precaución
    "te": "té",  # te (pronombre) vs té (bebida)
    "mas": "más",  # mas (conjunción adversativa, equivale a 'pero') vs más (adverbio de cantidad)
    "si": "sí",  # si (conjunción condicional/nota musical) vs sí (adverbio de afirmación/pronombre reflexivo)
    "de": "dé",  # de (preposición) vs dé (verbo dar, subjuntivo/imperativo)
    # "se": "sé"      # se (pronombre) vs sé (verbo saber/ser) - Ya incluido en verbos
    # "solo": "sólo" # solo (adjetivo 'alone') vs sólo (adverbio 'only') - RAE desaconseja tildar el adverbio desde 2010
    # "este", "ese", "aquel", etc. -> Ya no se tildan como pronombres desde 2010
}


# --- Fin del Diccionario Ampliado ---


class AccentAdderListener(SpanishAccentListener):
    """ Listener para añadir acentos CONTEXTUALES (qué, cómo...) """
    def __init__(self, tokens: CommonTokenStream):
        self.rewriter = TokenStreamRewriter(tokens)

    def _add_accent_if_needed(self, token):
        original_word = token.text.lower()
        if original_word in CONTEXT_ACCENT_MAP:
            accented_word = CONTEXT_ACCENT_MAP[original_word]
            if token.text[0].isupper():
                 accented_word = accented_word.capitalize()
            self.rewriter.replaceSingleToken(token, accented_word)

    def enterInterrogative_word(self, ctx: SpanishAccentParser.Interrogative_wordContext):
        self._add_accent_if_needed(ctx.start)

    def enterExclamative_word(self, ctx: SpanishAccentParser.Exclamative_wordContext):
        self._add_accent_if_needed(ctx.start)


# --- Función para añadir acentos fijos (reintroducida) ---
def add_fixed_accents(text, accent_dict):
    """ Aplica correcciones de acentos fijos basadas en un diccionario. """
    corrected_parts = []
    parts = re.split(r'(\W+)', text) # Divide manteniendo delimitadores

    for part in parts:
        if part and re.match(r'\w+', part): # Si es una palabra
            word_lower = part.lower()
            if word_lower in accent_dict:
                corrected_word = accent_dict[word_lower]
                # Preservar capitalización
                if part.istitle():
                    corrected_parts.append(corrected_word.capitalize())
                elif part.isupper():
                    corrected_parts.append(corrected_word.upper())
                else:
                    corrected_parts.append(corrected_word)
            else:
                corrected_parts.append(part) # Mantener palabra original
        elif part:
             corrected_parts.append(part) # Mantener delimitador

    return "".join(corrected_parts)
# --- Fin de la Función ---


# --- Función Principal (main) ---
def main():
    # ... (Obtener e imprimir fecha/hora actual) ...
    try:
        cst_offset = datetime.timedelta(hours=-6)
        cst_tz = datetime.timezone(cst_offset, name="CST")
        now = datetime.datetime.now(cst_tz)
    except Exception:
        now = datetime.datetime.now() # Fallback
    print("Corrector de Acentos Simplificado (Español)") # Título ajustado
    print("Escribe una frase (o 'salir' para terminar):")

    while True:
        try:
            input_str = input("> ")
            if input_str.lower() == 'salir':
                break
            if not input_str.strip():
                continue

            # === PASO 1: Análisis Sintáctico (Limitado) y Acentos Contextuales ===
            input_stream = InputStream(input_str)
            lexer = SpanishAccentLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = SpanishAccentParser(token_stream)
            parser.removeErrorListeners()
            tree = parser.prog()
            listener = AccentAdderListener(token_stream) # Usa CONTEXT_ACCENT_MAP
            walker = ParseTreeWalker()
            walker.walk(listener, tree)

            # Obtener texto después del Paso 1 (usando el workaround)
            output_after_step1 = ""
            try:
                token_stream.fill()
                num_tokens = len(token_stream.tokens)
                if num_tokens > 0:
                    start_index = 0
                    stop_index = num_tokens - 1
                    output_after_step1 = listener.rewriter.getText("default", start_index, stop_index)
                else:
                    output_after_step1 = ""
            except Exception as e_gettext:
                 print(f"Error durante la llamada a getText: {e_gettext}")
                 output_after_step1 = "[Error]" # Continuar con el texto original en caso de error? O el vacío?

            # === PASO 2: Corrección Léxica de Acentos Fijos ===
            final_output = add_fixed_accents(output_after_step1, FIXED_ACCENT_DICT)

            # === Impresión del Resultado Final ===
            print(f"Resultado: {final_output}")

        except EOFError:
            print("\nSaliendo...")
            break
        except Exception as e:
            print(f"Error procesando la entrada: {e}")
            print("  (La gramática/lógica puede tener errores o limitaciones)")
            # import traceback; traceback.print_exc()

if __name__ == '__main__':
    main()