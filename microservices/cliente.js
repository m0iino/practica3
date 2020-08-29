import express from  'express';

let app = express();

app.get('/cliente', (req, res, next) => {
    res.send(["cristian","mishell"])
})

app.listen(4000, () => {
    console.log('Server running on 4000');
})