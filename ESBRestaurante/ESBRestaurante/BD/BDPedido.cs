using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using ESBRestaurante.BD;
using System.Threading.Tasks;
using Flurl.Http;
using ESBRestaurante.Modelos;

namespace ESBRestaurante.BD
{
    public class BDPedido
    {
        public static Pedido listaPedidos = new Pedido()
        {
            Id = 1,
            Descripcion = "pedido 1",
            IdCliente = 1,
            IdRepartidor = 1,
            IdRestaurante = 1,
            Estado = 0
        };

        public Pedido obtenerPedido()
        {
            return listaPedidos;
        }

        public async Task agregarPedidoAsc(Pedido pedido_nuevo)
        {
            var response = await "http://localhost:62499/api/pedido/agregar".PostJsonAsync(pedido_nuevo);
        }
        public async Task<Pedido> obtenerPedidoAsc(int id)
        {
            var url = "http://localhost:62499/api/pedido/" + id.ToString();
            var response = await url.GetJsonAsync<Pedido>();
            return response;
        }
        public async Task actualizar(Pedido actual)
        {
            var response = await "http://localhost:62499/api/pedido/actualizar".PostJsonAsync(actual);
        }
    }
}
