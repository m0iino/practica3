import path from 'path';
import gateway from 'express-gateway';
import './user';
import './cliente';
import './restaurante';
import './repartidor';

gateway()
  .load(path.join(__dirname, 'config'))
  .run();
