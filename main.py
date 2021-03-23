from Motor import Motor

motor = Motor()

while not motor.status_final():
    motor.pergunta()

print(f'O dispositivo de proteção do motor atuou por {motor.get_resultado()}.')
