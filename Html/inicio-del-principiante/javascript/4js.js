//Diccionarios
let jugador = {
    nombre:"Alex",
    vida:10
};
console.log(jugador)
jugador.nombre = "Iluminax"
console.log(jugador)
const jugador2 = {
    nombre:jugador.nombre,
    vida:jugador.vida + 10
};
jugador.nombre = "Alex"
console.log()
console.log(jugador2)