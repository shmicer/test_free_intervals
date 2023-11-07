from datetime import datetime, timedelta


start_time = datetime.strptime('09:00', '%H:%M')
end_time = datetime.strptime('21:00', '%H:%M')

busy = [
    {'start': '10:30',
     'stop': '10:50'},
    {'start': '18:40',
     'stop': '18:50'},
    {'start': '14:40',
     'stop': '15:50'},
    {'start': '16:40',
     'stop': '17:20'},
    {'start': '20:05',
     'stop': '20:20'}
]

# Отсортируем список по времени

busy.sort(key=lambda x: x['start'])


def make_30_minute_intervals(start, stop, busy_list, free_intervals=None):

    # Изменяем формат занятых интервалов на datetime
    busy_datetime_format = [(datetime.strptime(interval['start'], '%H:%M'),
                             datetime.strptime(interval['stop'], '%H:%M')) for interval in busy_list]

    if free_intervals is None:
        free_intervals = []
    current_time = start

    # Проверяем свободные интервалы в 30 минут на пересечение с занятыми и при наличии добавляем их в список

    for busy_start, busy_stop in busy_datetime_format:
        if current_time < busy_start:
            while current_time + timedelta(minutes=30) <= busy_start:
                free_intervals.append({'start': current_time.strftime('%H:%M'),
                                       'stop': (current_time + timedelta(minutes=30)).strftime('%H:%M')})
                current_time += timedelta(minutes=30)

        current_time = busy_stop

    if current_time < stop:
        while current_time + timedelta(minutes=30) <= end_time:
            free_intervals.append(
                {'start': current_time.strftime('%H:%M'), 'stop': (current_time + timedelta(minutes=30)).strftime('%H:%M')})
            current_time += timedelta(minutes=30)
    return free_intervals


print(make_30_minute_intervals(start_time, end_time, busy))
