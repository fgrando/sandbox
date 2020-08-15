const alunos = ['fernando', 'zeca', 'tonho']


console.log(alunos.length, alunos)

alunos[6] = 'last now' // nao da erro e adiciona o elemento
console.log(alunos.length, alunos)

alunos.push('jose')
console.log(alunos.length, alunos)

alunos.unshift('zezinho') // adiciona no comeco
console.log(alunos.length, alunos)

alunos.pop() // adiciona no comeco
console.log(alunos.length, alunos)

alunos.shift() // deleta começo
console.log(alunos.length, alunos)


console.log(alunos.slice(1,3)) // pega partes do array


function saudacao(nome = 'leke'){
    return `bom dia ${nome}`;
}

const saudacao2 = function(nome ='asdf') {
    return `bom dia ${nome}`;
}

const saudacao3 = (nome) => {
    return `bom dia ${nome}`;
}

saudacao(); // funciona
console.log(saudacao())
console.log(saudacao('tafa'))
console.log(saudacao2('tafa'))
console.log(saudacao3('tafa'))