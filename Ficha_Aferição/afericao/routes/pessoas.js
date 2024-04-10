var express = require('express');
var router = express.Router();
var Pessoa = require("../controllers/pessoa")


router.get('/pessoas', function(req, res) {
    Pessoa.list()
      .then(data => {
        res.jsonp(data); // Sending data directly without wrapping it
      })
      .catch(erro => res.jsonp({ error: erro })); // Handling errors, if any
});


router.post('/pessoas', function(req, res) {
  // Extract data for new Pessoa from request body
  const pessoaData = req.body;

  // Call controller method to create new Pessoa
  Pessoa.create(pessoaData)
      .then(newPessoa => {
          // Send response with the newly created Pessoa
          res.status(201).jsonp(newPessoa);
      })
      .catch(error => {
          // Send error response if creation fails
          res.status(500).jsonp({ error: 'Failed to create Pessoa' });
      });
});

router.delete('/pessoas/:id', function(req, res) {
  const pessoaId = req.params.id;

  // Call controller method to delete the Pessoa
  Pessoa.delete(pessoaId)
      .then(() => {
          // Send success response
          res.status(204).send();
      })
      .catch(error => {
          // Send error response if deletion fails
          res.status(500).json({ error: 'Failed to delete Pessoa' });
      });
});

// Route to update a Pessoa
router.put('/pessoas/:id', function(req, res) {
  const pessoaId = req.params.id;
  const newData = req.body;

  // Call controller method to update the Pessoa
  Pessoa.update(pessoaId, newData)
      .then(updatedPessoa => {
          // Check if Pessoa was found and updated
          if (!updatedPessoa) {
              return res.status(404).json({ error: 'Pessoa not found' });
          }
          // Send success response with updated Pessoa
          res.json(updatedPessoa);
      })
      .catch(error => {
          // Send error response if update fails
          res.status(500).json({ error: 'Failed to update Pessoa' });
      });
});


module.exports = router;
