from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_produtos, rotas_usuarios, rotas_pedidos


app = FastAPI()

#CORS
origins = ['http://localhost:3000',
           'https://myapp.vercel.com']
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

#produtos Rota

app.include_router(rotas_produtos.router)

#usuario Rota

app.include_router(rotas_usuarios.router)

#pedido Rota

app.include_router(rotas_pedidos.router)