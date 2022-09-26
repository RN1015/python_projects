import urlexpander
b = input("Ener URL: ")
if 'https://' in b:
    pass
else:
    b = 'https://www.' + b
a = urlexpander.expand(b)
if 'loclx' in a or 'ngrock' in a or 'sttp' in a:
    print("STOP!!! This might harm your privacy")
else:
    print("This is probably safe")

x = input()