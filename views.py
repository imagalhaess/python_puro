from models import Conta, engine, Bancos, Status
from sqlmodel import Session, select

def criar_conta(conta: Conta):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.banco == conta.banco)
        results = session.exec(statement).all()
        
        if results:
            print('Conta já existe')
            return
        
        session.add(conta)
        session.commit()

def listar_contas():
    with Session(engine) as session:
        statement = select(Conta)
        results = session.exec(statement).all()
    return results

def desativar_conta(id):
    with Session(engine) as session:
        statment = select(Conta).where(Conta.id == id)
        conta = session.exec(statment).first()
        if conta.valor > 0:
            raise ValueError('Conta com saldo positivo não pode ser desativada')
        conta.status = Status.INATIVO
        session.commit()

def transferir_saldo(id_conta_saida, id_conta_entrada, valor):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id == id_conta_saida)
        conta_saida = session.exec(statement).first()
        if conta_saida.valor < valor:
            raise ValueError('Saldo insuficiente')
        statement = select(Conta).where(Conta.id == id_conta_entrada)
        conta_entrada = session.exec(statement).first()

        if conta_saida.valor < valor:
            raise ValueError('Saldo insuficiente')
        
        conta_saida.valor -= valor
        conta_entrada.valor += valor
        session.commit()







#conta = Conta(valor=0, banco=Bancos.ITAU) # Debug para criar conta
#criar_conta(conta) # Debug para criar conta
#desativar_conta() # Debug para desativar conta
#transferir_saldo(2, 1, 100) # Debug para transferir saldo
#listar_contas() # Debug para listar contas