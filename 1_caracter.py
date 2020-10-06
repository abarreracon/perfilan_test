"""
// Encontrar cual es el carácter que se repite más veces
// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"
"""
print("Escribe un texto: ")
s = input()

frequencies = [(c, s.count(c)) for c in set(s)]
print("frecuencias: ", frequencies)
most = max(frequencies, key=lambda x: x[1])[0]
print("Caracter mas repetido: ", most)


