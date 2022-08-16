/*
Crea una clase Persona con las siguientes variables:

La edad

El nombre

El teléfono

Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.

Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.

Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador.
*/

class Persona
{
    constructor(nombre,edad,telefono)
    {
        this.nombre = nombre;
        this.edad = edad;
        this.telefono = telefono;
    }
}

let nuevaPersona = new Persona('Pepe',89,'555-43-23-63');
console.log(nuevaPersona);


class Cliente extends Persona
{
    constructor(nombre,edad,telefono,credito)
    {
        super(nombre,edad,telefono);
        this.credito = credito;
    }
}

let nuevoCliente = new Cliente('Marta',46,'555-35-245-77',4000);
console.log(nuevoCliente);


class Trabajador extends Persona
{
    constructor(nombre,edad,telefono,salario)
    {
        super(nombre,edad,telefono);
        this.salario = salario;
    }
}

let nuevoTrabajador = new Trabajador('Pedro',20,'555-464-263',700);
console.log(nuevoTrabajador);
