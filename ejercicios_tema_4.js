/*
Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
*/

const numeroIf = 34;
var isPositivo = false;

if(numeroIf === 0){isPositivo = '0'}

else if(numeroIf > 0){isPositivo =true}

else{isPositivo = false}
console.log(isPositivo);

/*
Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
Incrementar el valor de la variable en uno cada vez que se ejecute.
Mostrarlo por pantalla cada vez que se ejecute.
*/

let numeroWhile = -2;

while(numeroWhile < 3)
{
    console.log(`El valor de numeroWhile es: ${numeroWhile}`);
    numeroWhile++
}

//Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.

let numeroWhile_2 = 1;
do
{   
    console.log(`numeroWhile_2: ${numeroWhile_2}`)
    numeroWhile_2 += 1;
    break
} 
while(numeroWhile_2 = 1);

//Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.

let numeroFor = 0;

for(let i=0;i <= 1000; i++)
{
    console.log(`numeroFor: ${numeroFor}`)
    
    if(numeroFor <=3){numeroFor++}
    
    else{break}
}

/*
Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.
*/

let estacion = "invierno";

switch(estacion)
{
    case 'verano':
        console.log(`Es ${estacion}`)
    break

    case 'invierno':
        console.log(`Es ${estacion}`)
    break
    
    case 'otono':
        console.log(`Es ${estacion}`)
    break

    case 'primavera':
        console.log(`Es ${estacion}`)
    break
}

