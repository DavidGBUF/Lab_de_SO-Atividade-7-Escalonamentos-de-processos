# Definir processos com (Tempo de chegada, Tempo de execução, Prioridade)
processos = [
    {"id": 1, "chegada": 0, "execucao": 10, "prioridade": 3},
    {"id": 2, "chegada": 2, "execucao": 5, "prioridade": 1},
    {"id": 3, "chegada": 4, "execucao": 2, "prioridade": 2},
    {"id": 4, "chegada": 6, "execucao": 8, "prioridade": 4},
]

# Simulação FCFS (First-Come, First-Served)
def fcfs(processos):
    tempo_atual = 0
    tempo_espera_total = 0
    tempo_turnaround_total = 0
    tempo_resposta_total = 0

    print("Simulação FCFS:")
    for processo in sorted(processos, key=lambda p: p["chegada"]):
        if tempo_atual < processo["chegada"]:
            tempo_atual = processo["chegada"]

        tempo_espera = tempo_atual - processo["chegada"]
        tempo_turnaround = tempo_espera + processo["execucao"]
        tempo_resposta = tempo_espera

        tempo_espera_total += tempo_espera
        tempo_turnaround_total += tempo_turnaround
        tempo_resposta_total += tempo_resposta

        print(f"Processo {processo['id']}: Espera={tempo_espera}, Turnaround={tempo_turnaround}, Resposta={tempo_resposta}")
        tempo_atual += processo["execucao"]

    num_processos = len(processos)
    throughput = num_processos / tempo_atual
    print(f"Tempo médio de espera: {tempo_espera_total / num_processos}")
    print(f"Turnaround time médio: {tempo_turnaround_total / num_processos}")
    print(f"Tempo de resposta médio: {tempo_resposta_total / num_processos}")
    print(f"Throughput: {throughput:.2f} processos por unidade de tempo\n")

# Simulação SJF (Shortest Job First)
def sjf(processos):
    tempo_atual = 0
    tempo_espera_total = 0
    tempo_turnaround_total = 0
    tempo_resposta_total = 0
    processos_ordenados = sorted(processos, key=lambda p: (p["chegada"], p["execucao"]))
    
    print("Simulação SJF:")
    for processo in processos_ordenados:
        if tempo_atual < processo["chegada"]:
            tempo_atual = processo["chegada"]

        tempo_espera = tempo_atual - processo["chegada"]
        tempo_turnaround = tempo_espera + processo["execucao"]
        tempo_resposta = tempo_espera

        tempo_espera_total += tempo_espera
        tempo_turnaround_total += tempo_turnaround
        tempo_resposta_total += tempo_resposta

        print(f"Processo {processo['id']}: Espera={tempo_espera}, Turnaround={tempo_turnaround}, Resposta={tempo_resposta}")
        tempo_atual += processo["execucao"]

    num_processos = len(processos)
    throughput = num_processos / tempo_atual
    print(f"Tempo médio de espera: {tempo_espera_total / num_processos}")
    print(f"Turnaround time médio: {tempo_turnaround_total / num_processos}")
    print(f"Tempo de resposta médio: {tempo_resposta_total / num_processos}")
    print(f"Throughput: {throughput:.2f} processos por unidade de tempo\n")

# Simulação Round Robin (RR) com quantum de tempo
def round_robin(processos, quantum):
    tempo_atual = 0
    fila = processos[:]
    tempo_espera_total = 0
    tempo_turnaround_total = 0
    tempo_resposta_total = 0
    tempo_restante = {p["id"]: p["execucao"] for p in processos}
    resposta_inicial = {}

    print("Simulação Round Robin:")
    while fila:
        for processo in fila[:]:
            if tempo_atual < processo["chegada"]:
                tempo_atual = processo["chegada"]

            if processo["id"] not in resposta_inicial:
                resposta_inicial[processo["id"]] = tempo_atual - processo["chegada"]

            if tempo_restante[processo["id"]] > quantum:
                tempo_restante[processo["id"]] -= quantum
                tempo_atual += quantum
            else:
                tempo_atual += tempo_restante[processo["id"]]
                tempo_restante[processo["id"]] = 0
                fila.remove(processo)
                tempo_turnaround = tempo_atual - processo["chegada"]
                tempo_turnaround_total += tempo_turnaround
                tempo_espera = tempo_turnaround - processo["execucao"]
                tempo_espera_total += tempo_espera

        if not fila:
            break

    for processo in processos:
        tempo_resposta_total += resposta_inicial[processo["id"]]

    num_processos = len(processos)
    throughput = num_processos / tempo_atual
    print(f"Tempo médio de espera: {tempo_espera_total / num_processos}")
    print(f"Turnaround time médio: {tempo_turnaround_total / num_processos}")
    print(f"Tempo de resposta médio: {tempo_resposta_total / num_processos}")
    print(f"Throughput: {throughput:.2f} processos por unidade de tempo\n")

# Simulação Priority Scheduling
def priority_scheduling(processos):
    tempo_atual = 0
    tempo_espera_total = 0
    tempo_turnaround_total = 0
    tempo_resposta_total = 0
    processos_ordenados = sorted(processos, key=lambda p: (p["chegada"], p["prioridade"]))
    
    print("Simulação Priority Scheduling:")
    for processo in processos_ordenados:
        if tempo_atual < processo["chegada"]:
            tempo_atual = processo["chegada"]

        tempo_espera = tempo_atual - processo["chegada"]
        tempo_turnaround = tempo_espera + processo["execucao"]
        tempo_resposta = tempo_espera

        tempo_espera_total += tempo_espera
        tempo_turnaround_total += tempo_turnaround
        tempo_resposta_total += tempo_resposta

        print(f"Processo {processo['id']}: Espera={tempo_espera}, Turnaround={tempo_turnaround}, Resposta={tempo_resposta}")
        tempo_atual += processo["execucao"]

    num_processos = len(processos)
    throughput = num_processos / tempo_atual
    print(f"Tempo médio de espera: {tempo_espera_total / num_processos}")
    print(f"Turnaround time médio: {tempo_turnaround_total / num_processos}")
    print(f"Tempo de resposta médio: {tempo_resposta_total / num_processos}")
    print(f"Throughput: {throughput:.2f} processos por unidade de tempo\n")


# Executar simulações
fcfs(processos)
sjf(processos)
round_robin(processos, quantum=4)
priority_scheduling(processos)
