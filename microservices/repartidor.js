import express from  'express';

let app = express();

app.get('/repartidor', (req, res, next) => {
    res.send(["pedro"])
})

app.listen(6000, () => {
    console.log('Server running on 6000');
})