const Modalidade = require("../models/modalidade");


module.exports.list = () => {
    return Modalidade.find().distinct('nome').exec(); // Using distinct to get unique names
};
