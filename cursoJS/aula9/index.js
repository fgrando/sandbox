// var vs let

var nome = 'fernando'
var nome = 'luiz'
console.log(nome)


const someString = 'hello';
const otherString = "hello";
const anotherString = `hello`;
const number = 10;
const otherNumber = 12.3;
let anUndefinedVariable;
let aNullValue = null;
// undefined is not null...
const boolean = true;
const array = [1,2];

// primitive types dont have references, the others do:
let array_ref = array // created a reference, not a copy.
array_ref.push(3)


console.log(typeof someString, someString);
console.log(typeof otherNumber, otherNumber);
console.log(typeof anUndefinedVariable, anUndefinedVariable);
console.log(typeof aNullValue, aNullValue);
console.log(typeof boolean, boolean);
console.log(typeof array, array);
console.log(typeof array_ref, array_ref);

