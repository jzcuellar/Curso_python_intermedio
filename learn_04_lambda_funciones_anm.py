# Solucion con lambda

is_palindrome = lambda string: string == string[::-1]

print(is_palindrome('ana'))

# Solucion con funcion def

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('ana'))