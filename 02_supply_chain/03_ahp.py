"""
Mestrado Profissional em Administração - UNP
Disciplina: Gestão da Cadeia de Suprimentos (Gestão de Operações)
Exercício B - Método AHP
Professora: Luciana Gondim de A. Guimarães
"""
print('\033c', end='')
import numpy as np

def menu_solucoes():
    solucoes = []
    while True:
        print("--- Menu de Soluções ---")
        print("1 - Inserir Solução")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criterio = input("\nDigite o nome da solução: ").strip()
            solucoes.append(criterio)            
            
        elif opcao == "2":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida!")
    print(f"Soluçôes: {solucoes}")

menu_solucoes()