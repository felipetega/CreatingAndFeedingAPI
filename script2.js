/*
API e gerador de .json
Para rodar: node script2.js
Para acessar: http://localhost:3000/forms
*/
const express = require('express')
const server = express()
const forms = require('./src/data/forms.json')
const fs = require('fs')

//Dados
let respostaFinal = JSON.stringify({
  resposta1: 'Sim',
  resposta2: 'Sim',
  resposta3: 'Agora!!',
  resposta4: 'Testando testando',
  quantidadePositiva: 4,
  quantidadeNegativa: 0,
  quantidadeNaoAvaliada: 0
})

//Gerador .json
fs.writeFileSync('./src/data/forms.json', respostaFinal)

//Local e conteúdo API
server.get('/forms', (req, res) => {
  return res.json(forms)
})

//Porta 3000
server.listen(3000, () => {
  console.log('Servidor está funcionando...')
})
