from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from auth import create_access_token, hash_password
from database.crud import create_patient

from schemas import (
    PatientCreateInput,
    TokenData
)

patient_router = APIRouter(prefix='/patient')


@patient_router.post('/', description='Create a new patient')
async def patient_create(patient_input: PatientCreateInput):
    try:
        patient_input.password = hash_password(patient_input.password)
        doctor = await create_patient(patient_input)
        token = create_access_token(
            data=TokenData(id=doctor.id, name=doctor.name))

        response = JSONResponse(
            content={'message': 'Sua conta foi criada com sucesso!'}, status_code=201)
        response.set_cookie("session", token, httponly=False,
                            secure=True, samesite="none")
        return response
    except Exception:
        raise HTTPException(
            500, content={"message": "Houve um erro ao criar seu usuário"})


@patient_router.get('/', description='Get all tests')
async def get_tests():
    try:
        # Aqui retornaria todos os exames que o paciente enviou
        return {'message': 'ok'}
    except Exception:
        raise HTTPException(
            500, detail={"message": "Houve um erro ao retornar os exames"})
