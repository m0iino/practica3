import express from  'express';

let app = express();

app.get('/restaurante', (req, res, next) => {
    res.send(["pizzahut"])
})

app.listen(5000, () => {
    console.log('Server running on 5000');
})