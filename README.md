# Peterson-s-Algorithm

The Peterson's Algorithm é uma solução eficiente e simples para 
exclusão mútua entre dois processos. Ele utiliza duas variáveis: uma 
para indicar a intenção de entrar na seção crítica (flag) e outra para 
alternar a prioridade entre os processos (turn).

Funcionamento:

Cada processo ajusta sua flag para indicar sua intenção de entrar na seção crítica.

A variável "turn" é usada para decidir quem tem prioridade quando ambos os processos querem acessar a seção crítica simultaneamente.

O processo não prioritário aguarda enquanto o outro conclui a execução.

Este algoritmo garante exclusão mútua, ausência de deadlock e starvations, e é simples de implementar.
