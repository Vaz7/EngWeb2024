const express = require('express');
const router = express.Router();
const Modalidade = require("../controllers/modalidade");

router.get('/', function(req, res) {
  Modalidade.list()
    .then(data => {
      res.jsonp(data);
    })
    .catch(erro => res.jsonp({ error: erro }));
});

router.get('/:nome', function(req, res) {
  const sportName = req.params.nome;

  Modalidade.findOne({ 'desportos': { $exists: true, $elemMatch: { $eq: sportName } } })
    .then(modalidade => {
      if (!modalidade) {
        res.status(404).jsonp({ error: 'Sport not found' });
        return;
      }

      const people = modalidade.desportos.get(sportName);
      res.jsonp({ sport: sportName, people: people });
    })
    .catch(error => res.status(500).jsonp({ error: error.message }));
});
module.exports = router;
