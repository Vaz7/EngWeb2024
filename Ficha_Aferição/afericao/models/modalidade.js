var express = require('express');
var router = express.Router();
const mongoose = require('mongoose');

const ModalidadeSchema = new mongoose.Schema({
    desportos: {
        type: Map,
        of: [String]
    }
}, { versionKey: false });

const Modalidade = mongoose.model('Desporto', ModalidadeSchema);

module.exports = Modalidade;
