/*
Para practicar la encapsulación:

Crear clase Persona.

Crear las variables privadas edad, nombre y telefono de la clase Persona.

Crear gets y sets de cada propiedad.

Crear un objeto persona en el main.

Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola.
*/

class Persona
{
    constructor(nombre,edad,telefono)
    {
        this.nombre = nombre;
        this.edad = edad;
        this.telefono = telefono;
    }
    
    setNombre(param){this.nombre = param;};
    setEdad(param){this.edad = param;};
    setTelefono(param){this.telefono = param;};

    getNombre(){return this.nombre;};
    getEdad(){return this.edad;};
    getTelefono(){return this.telefono;};
};

let juan = new Persona();

juan.setNombre('Juan');
juan.setEdad(35);
juan.setTelefono('555-35-25-88');

let nombreDeJuan = juan.getNombre();
let edadDeJuan = juan.getEdad();
let telefonoDeJuan = juan.getTelefono();

console.log(`La edad de ${nombreDeJuan} es ${edadDeJuan} y su telefono es ${telefonoDeJuan}.`);

