var Comp = require("../models/compositores")


module.exports.list=()=>{
    return Comp.find()
    .sort({nome:1})
    .exec()
}

module.exports.findById = id =>{
    return Comp
    .findOne({_id : id})
    .exec()
}


module.exports.insert = comp => {
    console.log(comp)
    return Comp.create(comp)
}

// compositor - estrutura passada como argumento
module.exports.updateCompositor = (id, compositor) => {
    return Comp.updateOne({_id: id}, compositor)
}


module.exports.deleteCompositor = id => {
    return Comp.deleteOne({_id: id}).exec();
}


