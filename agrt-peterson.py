
def peterson_algorithm():
    import threading
    import time

    flag = [False, False]
    turn = 0

    def process_0():
        nonlocal turn
        flag[0] = True
        turn = 1
        while flag[1] and turn == 1:
            pass
        print("Processo 0 na seção crítica")
        time.sleep(1)
        print("Processo 0 saindo da seção crítica")
        flag[0] = False

    def process_1():
        nonlocal turn
        flag[1] = True
        turn = 0
        while flag[0] and turn == 0:
            pass
        print("Processo 1 na seção crítica")
        time.sleep(1)
        print("Processo 1 saindo da seção crítica")
        flag[1] = False

    t0 = threading.Thread(target=process_0)
    t1 = threading.Thread(target=process_1)

    t0.start()
    t1.start()
    t0.join()
    t1.join()

# Para testar o algoritmo de Peterson, basta chamar a função:
# peterson_algorithm()

