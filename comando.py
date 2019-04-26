import win32api as wapi

teclas_possiveis = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    teclas_possiveis.append(char)

def comando():
    teclas_apertadas = []
    for tecla in teclas_possiveis:
        if wapi.GetAsyncKeyState(ord(tecla)):
            teclas_apertadas.append(tecla)

    return teclas_apertadas