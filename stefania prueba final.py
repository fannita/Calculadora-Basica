#productos = {modelo:[marca,pantalla,RAM, disco GB de DD, procesador,video]}

productos = {
'8475HD':['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD':['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD':['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD':['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD':['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD':['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD':['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD':['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
};

#stock = {modelo: [precio,stock]}
stock_marca= {
'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}

#funcion para stock de marca

def stock_marca(marca):
 total = 0;
for codigo, datos in productos.items():
    if(datos[1].lower() == marca.lower()):
        total += stock[codigo][1];
print(f"el stock total para '{marca}' es:{total}");

#funcion para busqueda de precio
def busqueda_de_precio(precio_maxiimo, precio_minimo):
   resultados = [];
for precio, datos in productos.items():
   precio_maximo = 350000
   precio_minimo = 24000
   if(precio <= precio_maximo and precio >= precio_minimo) and (stock[codigo][1] > 0):
      
   

#funcion para actualizar precio
def actualizar_precio(codigo, nuevo_precio):
   if (codigo in stock):
     stock[codigo][1] = nuevo_precio;
     return True;
   return False;



#menu programa principal
def main():
   while True:
    print("******MENU*******")
    print("1-Stock marca")
    print("2-Busqueda por precio")
    print("3-Actualizar precio")
    print("4-Salir")

opc = int(input("ingrese la opcion que desea"))

if(opc == 1):
    marca = input("ingrese stock de marca");
    stock_marca(marca);

elif(opc == 2):

   busqueda_de_precio = int(input("Busqueda de precio"));
   precio_minimo = float(input("ingrese el precio minimo"));
   precio_maximo = float(input("ingrese el precio maximo"));
   busqueda_de_precio(precio_maximo, precio_minimo);

print("No hay notebooks en ese rango de precios.”")

elif(opc == 3):
while True:
    codigo = input("ingrese el codigo del producto")
    try:
     nuevo_precio = int(input("ingrese el nuevo precio del producto"))
     if actualizar_precio(codigo, nuevo_precio);
      print("Precio actualizado")
     else:
      print("Desea atualizar otro precio(si/no)?")
      modelo_actualizar = float(input("ingrese el modelo a actualizar"))
    except ValueError:



    elif(opc == 4):
    salir = ("salir del programa");
    print("Programa Finalizado");
 

    else:
    print("Debe seleccionar una opción válida!!")

  #ejecutar programa
    if__name__ == "__main___":
    main();