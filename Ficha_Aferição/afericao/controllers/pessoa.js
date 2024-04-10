var Pessoa = require("../models/pessoa")


module.exports.list=()=>{
    return Pessoa.find()
    .exec()
}

module.exports.findById = id =>{
    return Pessoa
    .findOne({_id : id})
    .exec()
}

module.exports.create = (data) => {
    return Pessoa.create(data); // Assuming 'Pessoa' is your Mongoose model
};

module.exports.delete = (id) => {
    return Pessoa.deleteOne({ _id: id }).exec();
};

module.exports.update = (id, newData) => {
    return Pessoa.findByIdAndUpdate(id, newData, { new: true }).exec();
};
