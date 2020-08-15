const express = require('express')
const restful = require('node-restful')
const server = express()
const mongoose = restful.mongoose
const bodyParser = require('body-parser')
const cors = require('cors')



// Database
mongoose.Promise = global.Promise
mongoose.connect('mongodb://db/mydb') // o servico se chamara db (no docker-compose.yml) e ele vai conseguir resolver

// Middlewares
server.use(bodyParser.urlencoded({extended:true}))
server.use(bodyParser.json())
server.use(cors())


// ODM - mapeamento objeto documento 
const Client = restful.model('Client', {
    name : { type: String, required: true }
})

// Rest API
Client.methods(['get', 'post', 'put', 'delete'])
Client.updateOptions({new: true, runValidators: true})

// Routes
Client.register(server, '/clients')


// Start Server
server.listen(3000)



