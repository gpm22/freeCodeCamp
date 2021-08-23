def add_time(start, duration, week_day = None):

  inicio = start.split()
  tempo_inicial = inicio[0].split(':')
  hora_inicial = int(tempo_inicial[0])
  minuto_inicial = int(tempo_inicial[1])
  fase = inicio[1]


  if fase == 'PM': hora_inicial = hora_inicial + 12

  duracao = duration.split(':')

  hora_duracao = int(duracao[0])

  minuto_duracao = int(duracao[1])

  minutos = minuto_inicial + minuto_duracao

 

  hora_extra = 0
  if minutos >= 60:
   
    hora_extra = int(minutos/60)
    minutos = minutos - 60

  horas_adicionais = hora_duracao + hora_extra
  dias = 0
  if horas_adicionais >= 24:
    dias = int(horas_adicionais/24)
    horas_adicionais = horas_adicionais - dias*24

  nova_hora = hora_inicial + horas_adicionais


  if nova_hora >= 24:
    dias = dias + 1
    nova_hora = nova_hora - 24

  nova_fase = 'AM'
  if nova_hora > 12:
    nova_hora = nova_hora - 12
    nova_fase = 'PM'


  if nova_hora == 12: nova_fase = 'PM'
  if nova_hora == 0 : nova_hora = 12; nova_fase = 'AM'

  if minutos < 10: minutos = '0'+str(minutos)
  else: minutos = str(minutos)

  new_time = str(nova_hora)+':'+minutos + ' '+nova_fase

  dias_da_semana = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

  if week_day:
    week_day = week_day[0].upper() +  week_day[1:].lower()
    
    digit_day = dias_da_semana.index(week_day)

    dias_p = dias % 7

    new_digit_day = digit_day + dias_p

    if new_digit_day > 6: new_digit_day = new_digit_day - 7

    new_week_day = dias_da_semana[new_digit_day]

    new_time = new_time + ', ' + new_week_day

  if dias == 1:
    new_time = new_time + ' (next day)'
  elif dias> 1:
    new_time = new_time + ' (' + str(dias) + ' days later)'

  

  return new_time