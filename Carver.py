# File Carver - Recuperador de JPG - By sinn3778-ops
# Proyecto de forense digital para mi portafolio ético

def recuperar_fotos(archivo):
    with open(archivo, 'rb') as f:
        data = f.read()
    
    inicio = 0
    count = 0
    while True:
        # Busca cabecera JPG FF D8
        start = data.find(b'\xff\xd8', inicio)
        if start == -1:
            break
        # Busca final JPG FF D9
        end = data.find(b'\xff\xd9', start)
        if end == -1:
            break
        
        with open(f'recuperada_{count}.jpg', 'wb') as out:
            out.write(data[start:end+2])
        print(f"[+] Foto recuperada_{count}.jpg")
        count += 1
        inicio = end + 2

if __name__ == "__main__":
    print("Iniciando carver forense...")
    # Ejemplo: recuperar_fotos('imagen.raw')
