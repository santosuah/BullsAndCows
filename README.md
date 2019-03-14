## Bulls and Cows

Implementación en Python del tradiconal juego Bulls and Cows en su versión númerica, mas conocidos comercialmente una modificación de este como Mastermind. La interfaz es la terminal.
La longitud de clave y el número máximo de iteraciones se configuran en `config.py`, por defecto la longitud de clave es 4 y el mnúmero máximo de iteraciones son 11.

### Ejemplo de uso

Nos posicionamos en el directorio principal y ejecutamos `python3 src/bullsAndCows.py`
El formato de entrada para la calve son cuantro números del rango 0-9 separados por comas, sin que se repita ninguna.

```shell
python3 src/bullsAndCows.py

  ====================
  == Bulls and Cows ==
  ====================

  I        Guess        Bulls Cows
     +---+---+---+---+  +---+---+
  1  | 0 | 1 | 2 | 3 |  | 0 | 2 |
     +---+---+---+---+  +---+---+
  2  | 4 | 5 | 6 | 7 |  | 0 | 1 |
     +---+---+---+---+  +---+---+
  3  | 8 | 9 | 1 | 4 |  | 2 | 0 |
     +---+---+---+---+  +---+---+

  Input: 9,8,1,7
```

```shell
  ====================
  == Bulls and Cows ==
  ====================

  I        Guess        Bulls Cows
     +---+---+---+---+  +---+---+
  1  | 0 | 1 | 2 | 3 |  | 1 | 1 |
     +---+---+---+---+  +---+---+
  2  | 4 | 5 | 6 | 7 |  | 0 | 2 |
     +---+---+---+---+  +---+---+
  3  | 1 | 2 | 5 | 6 |  | 0 | 2 |
     +---+---+---+---+  +---+---+
  4  | 1 | 3 | 5 | 7 |  | 0 | 3 |
     +---+---+---+---+  +---+---+
  5  | 1 | 3 | 6 | 7 |  | 0 | 4 |
     +---+---+---+---+  +---+---+
  6  | 6 | 7 | 3 | 1 |  | 2 | 2 |
     +---+---+---+---+  +---+---+
  7  | 6 | 7 | 1 | 3 |  | 4 | 0 |
     +---+---+---+---+  +---+---+

  You win!
```

```shell
  ====================
  == Bulls and Cows ==
  ====================

  I        Guess        Bulls Cows
     +---+---+---+---+  +---+---+
  1  | 0 | 1 | 2 | 3 |  | 0 | 1 |
     +---+---+---+---+  +---+---+
  2  | 4 | 5 | 6 | 7 |  | 1 | 1 |
     +---+---+---+---+  +---+---+
  3  | 8 | 9 | 1 | 4 |  | 0 | 1 |
     +---+---+---+---+  +---+---+
  4  | 2 | 5 | 7 | 9 |  | 0 | 2 |
     +---+---+---+---+  +---+---+
  5  | 1 | 5 | 4 | 9 |  | 0 | 1 |
     +---+---+---+---+  +---+---+
  6  | 1 | 2 | 4 | 9 |  | 1 | 0 |
     +---+---+---+---+  +---+---+
  7  | 1 | 2 | 4 | 8 |  | 2 | 0 |
     +---+---+---+---+  +---+---+
  8  | 1 | 2 | 7 | 8 |  | 2 | 0 |
     +---+---+---+---+  +---+---+
  9  | 0 | 3 | 7 | 8 |  | 1 | 0 |
     +---+---+---+---+  +---+---+
  10 | 0 | 3 | 7 | 4 |  | 0 | 0 |
     +---+---+---+---+  +---+---+
  11 | 0 | 3 | 2 | 4 |  | 0 | 1 |
     +---+---+---+---+  +---+---+

  You lost!

  Secret key: 5268
```

### Modulos utilizados de la biblioteca estándar
- os
- random
- sys
