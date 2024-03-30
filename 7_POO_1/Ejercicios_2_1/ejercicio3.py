def verificar_calificacion(nota1, nota2, nota3):
    prom = (nota1 + nota2 + nota3) / 3
    
    mensaje = "Reprobado"
    if (prom >= 6):
        mensaje = "Aprobado"
    
    return mensaje
