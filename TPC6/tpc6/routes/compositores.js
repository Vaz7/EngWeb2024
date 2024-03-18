var express = require('express');
var router = express.Router();
var Comp = require("../controllers/compositor")


/* GET home page. */
router.get('/', function(req, res){
  var d = new Date().toISOString().substring(0, 16)
  res.render('index', {title: 'Gestão de compositores',data:d});
});



router.get('/compositores', function(req, res) {
  var d = new Date().toISOString().substring(0, 16)
  Comp.list()
  .then(data => {
    console.log(data)
    // Render the view with the list of composers
    res.render('listaComps', {title: 'Lista de compositores',lista: data,data:d});
  })
  .catch(erro => {
    // Handle errors
    res.status(500).send('Error fetching composers: ' + erro);
  });
});

router.get('/compositores/registo', function(req, res){
  var d = new Date().toISOString().substring(0, 16)
  res.render('registoComp', {data: d});
});




router.get('/compositores/:id',function(req,res){
  Comp.findById(req.params.id)
  .then(data => res.jsonp(data))
  .catch(erro => res.jsonp(erro))
})









//delete
router.get('/compositores/delete/:id', function(req, res) {
  Comp.deleteCompositor(req.params.id)
  .then(data => res.jsonp(data))
  .catch(erro => res.jsonp(erro))
})






router.post('/compositores', function (req, res) {
  console.log(req.body)
  Comp.insert(req.body)
    .then(data => res.status(201).jsonp(data))
    .catch(erro => res.status(523).jsonp(erro))
});

//posts
router.post('/compositores/registo',function(req,res){
  var d = new Date().toISOString().substring(0, 16)
  //console.log(JSON.stringify(req.body))
  Comp.insert(req.body)
  .then(resposta => {
    res.render('confirmRegisto',{info: req.body,data:d,title:"Registo de compositor com sucesso."})
  })
  .catch( erro => {
    res.render('error',{erro,message:'Erro ao gravar um compositor novo.'})
  })
});





router.put('/compositores/:id', function(req, res) {
  Comp.updateCompositor(req.params.id, req.body)
    .then(data => res.jsonp(data))
    .catch(erro => res.jsonp(erro))
})



module.exports = router;
