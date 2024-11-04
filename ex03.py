def eh_positivo(numero: float):
    ele_eh_positivo = None
    if numero > 0:
        ele_eh_positivo = True
    else:
        ele_eh_positivo = False
    return ele_eh_positivo

print(eh_positivo(2))
print(eh_positivo(-50))