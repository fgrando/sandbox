
let num1 = 10;
let num2 = 2.55544332;

console.log(num1 + num2)

console.log(num1.toString() + num2)

console.log(num1.toString(2))

console.log(num2.toFixed(3))

console.log(Number.isInteger(num2))

num1 = 0.7
num2 = 0.1

num1 += num2
num1 += num2
num1 += num2

console.log(num1)

console.log(Number(num1.toFixed(2)))

console.log(`floor: ${Math.floor(num1)}`)
console.log(`ceil: ${Math.ceil(num1)}`)
console.log(`round: ${Math.round(num1)}`)
console.log(Math.ceil(num1))

console.log(`max: ${Math.max(1,2,43,4,6,7,8,9)}`)
console.log(`rand: ${Math.random()}`)

console.log(100/0)