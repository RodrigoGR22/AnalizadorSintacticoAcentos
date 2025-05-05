// SpanishAccent.g4
grammar SpanishAccent;

// --- Reglas del Parser ---

// Punto de entrada: una secuencia de oraciones o frases
prog: (sentence | phrase)+ EOF;

// Una oración puede ser interrogativa, exclamativa o declarativa
sentence: (interrogative | exclamative | declarative) PUNCT_END?; // Permite puntuación final opcional

// Oración interrogativa (simplificada)
// Busca un patrón como '¿' palabra_interrogativa ... '?'
interrogative: INTERROG_OPEN interrogative_word (ANY_WORD | WS)+ INTERROG_CLOSE;

// Oración exclamativa (simplificada)
// Busca un patrón como '¡' palabra_exclamativa ... '!'
exclamative: EXCLAM_OPEN exclamative_word (ANY_WORD | WS)+ EXCLAM_CLOSE;

// Oración declarativa (muy simplificada: cualquier secuencia de palabras)
declarative: ANY_WORD (ANY_WORD | WS)+;

// Una frase suelta (no necesariamente una oración completa)
phrase: ANY_WORD (ANY_WORD | WS)*;

// Palabras clave que *podrían* llevar acento en preguntas/exclamaciones
interrogative_word: QUE | COMO | CUANDO | DONDE | QUIEN | CUANTO;
exclamative_word: QUE | COMO | CUANDO | DONDE | QUIEN | CUANTO; // Mismas palabras

// --- Reglas del Lexer ---

// Palabras clave (sin acento inicial, en minúsculas)
QUE:    [Qq] [Uu] [Ee];
COMO:   [Cc] [Oo] [Mm] [Oo];
CUANDO: [Cc] [Uu] [Aa] [Nn] [Dd] [Oo];
DONDE:  [Dd] [Oo] [Nn] [Dd] [Ee];
QUIEN:  [Qq] [Uu] [Ii] [Ee] [Nn];
CUANTO: [Cc] [Uu] [Aa] [Nn] [Tt] [Oo];

// Signos de puntuación
INTERROG_OPEN:  '¿';
INTERROG_CLOSE: '?';
EXCLAM_OPEN:    '¡';
EXCLAM_CLOSE:   '!';
PUNCT_END:      '.' | '?' | '!'; // Puntuación que puede terminar una oración

// Cualquier otra palabra (incluyendo las que ya tienen acento)
// Se usa [a-zA-Z] para simplificar, idealmente sería más específico para letras españolas
ANY_WORD:       [a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+;

// Espacio en blanco (se omite en el parser pero puede ser útil para reconstruir)
WS:             [ \t\r\n]+ -> channel(HIDDEN); // O skip si no lo necesitas en el listener