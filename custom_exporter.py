import random
import time
from prometheus_client import start_http_server, Gauge, Counter, Summary

# Гейдж со значением 0..100 
student_metric = Gauge("custom_student_metric", "Synthetic student KPI 0..100")

# Счётчик вставок 
insert_counter = Counter("custom_insert_counter_total", "Inserted rows counter")

# Время цикла "обновления"
loop_time = Summary("custom_loop_seconds", "Time spent in update loop")

@loop_time.time()
def update_metrics():
    # Случайное значение метрики 
    value = random.randint(40, 100)
    student_metric.set(value)

    # Имитируем вставку новых строк: на каждом цикле +1..3
    inserts = random.randint(1, 3)
    insert_counter.inc(inserts)

if __name__ == "__main__":
    # Экспортёр слушает на 8000
    start_http_server(8000)
    print(" Custom exporter is running on :8000/metrics")
    while True:
        update_metrics()
        time.sleep(5)
