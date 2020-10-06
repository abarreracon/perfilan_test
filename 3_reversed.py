"""
// Hacer un reversed string de una cadena
// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
// reverse('apple') === 'leppa'
// reverse('hello') === 'olleh'
// reverse('Greetings!') === '!sgniteerG'

"""
print("Escribe una palabra: ")
word = input()
reverse = word[::-1]
print(reverse)