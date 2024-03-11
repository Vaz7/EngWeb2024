var express = require('express');
var router = express.Router();
var axios = require('axios')

/* GET home page. */
router.get('/', function(req, res){
  var d = new Date().toISOString().substring(0, 16)
  res.render('index', {title: 'Gestão de compositores',data:d});
});


router.get('/compositores', function(req, res){
  var d = new Date().toISOString().substring(0, 16)
  axios.get('http://localhost:3000/compositores')
                    .then(resposta => {
                      res.render('listaComps', {title: 'Lista de compositores',lista: resposta.data,data: d});
                    })
                    .catch( erro => {
                      res.render('error',{erro,message:'Erro ao recuperar os compostitores.'})
                    })
});

router.get('/compositores/registo', function(req, res){
  var d = new Date().toISOString().substring(0, 16)
  res.render('registoComp', {data: d});
});

router.get('/compositores/:id', function(req, res){
  var d = new Date().toISOString().substring(0, 16)
  axios.get('http://localhost:3000/compositores/' + req.params.id)
                    .then(resposta => {
                      res.render('compositor', {title: 'Consulta de compositor',compositor: resposta.data,data: d});
                    })
                    .catch( erro => {
                      res.render('error',{erro,message:'Erro ao recuperar o aluno.'})
                    })
});


router.get('/compositores/delete/:id', function(req, res) {
  const composerId = req.params.id; // Extract composer ID from URL parameters

  axios.delete('http://localhost:3000/compositores/' + composerId)
    .then(response => {
      const d = new Date(); // Assuming 'd' is your date variable
      res.render('compositor', { title: 'Consulta de compositor', compositor: response.data, data: d });
    })
    .catch(error => {
      console.error('Error deleting composer:', error);
      res.render('error', { erro: error.response.data, message: 'Erro ao recuperar o compositor.' });
    });
});



router.get('/compositores/edit/:id', function(req, res) {
  const composerId = req.params.id; // Extract composer ID from URL parameters
  var d = new Date().toISOString().substring(0, 16)

  axios.get('http://localhost:3000/compositores/' + composerId)
  .then(resposta => {
    res.render('compositorEdit', { title: 'Edição de compositor', compositor: resposta.data, data: d });
  })
  .catch( erro => {
    res.render('error', { erro: error.response.data, message: 'Erro ao editar o compositor.' });
  });
});




router.post('/compositores/edit/:id', function(req, res) {
  var d = new Date().toISOString().substring(0, 16)
  const composerId = req.params.id; // Extract composer ID from URL parameters
    if(req.body){
        axios.put('http://localhost:3000/compositores/' + composerId, req.body)
        .then(resposta => {
          res.render('compositor', {title: 'Consulta de compositor',compositor: resposta.data,data: d});
        })
        .catch( erro => {
          res.render('error', { erro: error.response.data, message: 'Erro ao editar o compositor.' });    
        })

    } else {
      res.render('error', { erro: error.response.data, message: 'Erro ao editar o compositor.' });    
    }
});



//posts
router.post('/compositores/registo',function(req,res){
  var d = new Date().toISOString().substring(0, 16)
  console.log(JSON.stringify(req.body))
  axios.post('http://localhost:3000/compositores',req.body)
  .then(resposta => {
    res.render('confirmRegisto',{info: req.body,data:d,title:"Registo de compositor com sucesso."})
  })
  .catch( erro => {
    res.render('error',{erro,message:'Erro ao gravar um compositor novo.'})
  })
});


module.exports = router;