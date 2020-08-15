
////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////
// FUNCAO
// normal
function saudacao(nome = 'nome_default'){
    return `bom dia ${nome}`;
}

// funcao anonima (arrow function)
const saudacao2 = (nome) => {
    return `bom dia ${nome}`;
}

const saudacao3 = (nome) => `bom dia ${nome}`;

console.log(saudacao())
console.log(saudacao2('tafa'))
console.log(saudacao3('bye'))
////////////////////////////////////////////////////////////////

// objeto: const ou let
const meu_array = [1,2,4]
meu_array.push('fernando')
console.log(meu_array) // permite adicionar, mas nao mudar onde array aponta

let outro_array = [1,3]
outro_array='bom'
console.log(outro_array)// let deixa ok

////////////////////////////////////////////////////////////////
// OBJETOS {}

const Person = {
    nome: 'Luiz',
    idade: 1,
    fala(){ 
        console.log(`oi galera:${this.nome}`);
    },
    envelhece(){
        this.idade++;
    }
};



const p1 = Person
p1.fala()

console.log(p1)





////////////////////////////////////////////////////////////////