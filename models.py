from sqlmodel import Field, SQLModel, create_engine
from enum import Enum
class Bancos(Enum):
    NUBANK = "Nubank"
    SANTANDER = "Santander"
    BRADESCO = "Bradesco"
    ITAU = "Itaú"
    CAIXA = "Caixa"
    BANCO_DO_BRASIL = "Banco do Brasil"

class Status(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"

class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    valor: float
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)
  
sqlite_name_file = "database.db"
sqlite_url = f"sqlite:///{sqlite_name_file}"

engine = create_engine(sqlite_url, echo=True)

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    