/*
Primera parte:

Crear una función con tres parámetros que sean números que se suman entre sí.

Llamar a la función en el main y darle valores.
*/
console.log('Parte 1:')
const sumaTres = (n1,n2,n3) => 
{
    res = n1+n2+n3;
    return res
}

const suma = sumaTres(3,2,5);
console.log(suma); 

/*
Segunda parte:

Crear una clase coche.

Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.

Una función que incremente el número de puertas que tiene el coche.

Crear un objeto miCoche en el main y añadirle una puerta.

Mostrar el número de puertas que tiene el objeto.
*/
console.log('Parte 2:')
class Coche
{
    constructor(puertas = 4)
    {
        this.puertas = puertas;
    }   
    
    addPuerta(num)
    {
        this.puertas = this.puertas + Math.abs(num);
    }
}

Coche.prototype.verEstado = function()
{
    console.log(`Puertas: ${this.puertas}`);
}

const miCoche = new Coche();
miCoche.verEstado();
miCoche.addPuerta(1);
miCoche.verEstado();


