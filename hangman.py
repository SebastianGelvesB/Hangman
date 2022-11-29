import random
import os


def read_data(filepath=".data/data.txt"):   # función para leer las palabras de la base de datos
    words = []                                   # creo una lista vacía para guardas las palabras leídas de la base de datos
    with open(filepath, "r", encoding="utf-8") as f: # abro el archivo (base de datos) en modo lectura y lo llamo f
        for line in f:
            words.append(line.strip().upper())   # guardo las palabras en mayusculas y eliminando los espacios (veticales o horizontales)
    return words                                 # retorno la lista de palabras


def run():
    data = read_data(filepath="./data/data.txt") # creo una lista usando la función de arriba.
    chosen_word = random.choice(data)                # escogo una palabra aleatoria de la lista con el método random.choice()
    chosen_word_list = [letter for letter in chosen_word] # hago una lista que contiene las letras de dicha palabra
    chosen_word_list_underscores = ["_"] * len(chosen_word_list) #hago una lista de underscores con la misma cantidad de letras que la palabra escogida
    letter_index_dict = {}                           # creo un diccionario vacío
    for idx, letter in enumerate(chosen_word):       # enumerate(chosen_word) crea tuplas del tipo (0,letra_0) , (1, letra_1 etc), ya que el método se aplica a un string
        if not letter_index_dict.get(letter):        # esto quiere decir, if letter_index_dict.get(letter) == False
            letter_index_dict[letter] = []           # es decir, si la llave no tiene valor asignado, le asigno una lista vacía
        letter_index_dict[letter].append(idx)        # el value de cada key es el índice idx, pero como este value es una lista tooca usar append.
                                                     # al final de esto me queda un diccionario con llaves las letras de la palabra y
                                                     #  valores una lista cuyo único item es el índice de dicha letra
    lives = 9
    input_letters=[]
    while True:                              # esto es lo mismo que While True is True, es para ejecutar para siempre el bloque de código de abajo
        os.system("clear")                           # con esto limpiamos la pantalla
        print("""
        |    ¡BIENVENID@ AL JUEGO DEL AHORCADO!    |

        |    ¡ADIVINA LA PALABRA!   |

        |    ¡SE MUY CUIDADOSO CON TUS INTENTOS, SOLO TIENES 8 VIDAS PARA ADIVINAR LA PALABRA!    |

        """)
        for element in chosen_word_list_underscores:
            print(element + " ", end="")             # imprimimos la lista de underscores que se va llenando con las letras correctas que dice el usuario 
        print("\n")

        print("Te quedan " + str(lives) + " vidas", "\n")    

        print("Has usado las letras: ", input_letters, "\n")  

        letter = input("Ingresa una letra: ").strip().upper()  #le pedimos la letra al usuario
        assert letter.isalpha(), "Solo puedes ingresar letras"  #creamos un assert en caso de que el usuario meta algo diferente  una letra
        input_letters.append(letter)
        if letter in chosen_word_list:              # si la letra está en la lista de las letras de nuestra palabra entonces hacemos
            for idx in letter_index_dict[letter]:   # itero sobre los indices
                chosen_word_list_underscores[idx] = letter # en la lista de underscores, reemplazo el underscore por la letra ingresada 
                                                           # por el usuario en la posición adecuada
            lives = lives
        else:
            lives-=1

       


        if "_" not in chosen_word_list_underscores: # si ya no hay undersocrs en la lista de underscores
            os.system("clear") #limpiamos
            print("¡Ganaste! La palabra era", chosen_word)
            break     # con esto rompemos el while puesto que ya terminamos el juego

        if lives==0:
            os.system("clear")
            print("PERDISTE! :(!!   CONSUMISTE TUS 8 VIDAS, LA PALABRA CORRECTA ERA ", chosen_word)
            break


if __name__ == '__main__':
    run()

# ¿Viendo la solución? No hay drama crack
# Python es mejor que JavaScript