from sqlalchemy.orm import Session
from typing import List
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


from sqlalchemy.orm.session import Session


class RepositorioPedido():

    def __init__(self, session: Session) -> None:
        self.session = session


    def gravar_pedido(self, pedido: schemas.Pedido):
        pass


    def buscar_por_id(self, id: int):
        pass


    
    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int):
        pass


    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int):
        pass