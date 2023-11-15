from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from auth import create_access_token, hash_password
from database.crud import create_doctor

from schemas import (
    DoctorCreateInput,
    TokenData
)

doctor_router = APIRouter(prefix='/doctor')

@doctor_router.post('/', description='Create a new doctor')
async def doctor_create(doctor_input: DoctorCreateInput):
    try:
        doctor_input.password = hash_password(doctor_input.password)
        doctor = await create_doctor(doctor_input)
        token = create_access_token(data=TokenData(id=doctor.id, name=doctor.name))

        response = JSONResponse(content={'message': 'Sua conta foi criada com sucesso!'}, status_code=201)
        response.set_cookie("session", token, httponly=False, secure=True, samesite="none")
        return response
    except Exception:
        raise HTTPException(500, detail={"message": "Houve um erro ao criar seu usuário"})
    
@doctor_router.get('/', description='Get all tests')
async def get_tests():
    try:
        # Aqui retornaria todos os exames para o médico avaliar
        return {'message': 'ok'}
    except Exception:
        raise HTTPException(500, detail={"message": "Houve um erro ao retornar os exames"})
