import os
import time

class OficinaMecanica:
    def __init__(self):
        self.services = []
        self.available_services = [
            {"name": "Troca de óleo", "price": 150.00},
            {"name": "Balanceamento", "price": 100.00},
            {"name": "Alinhamento", "price": 120.00},
            {"name": "Revisão geral", "price": 300.00}
        ]
        self.menu_actions = {
            1: self.register_service,
            2: self.delete_service,
            3: self.list_services,
            4: self.show_total_value,
            5: self.exit_system
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_menu(self):
        self.clear_screen()
        print("\033[1;34m--- Oficina Mecânica ---\033[0m\n")
        print("\033[1;32m1 - Cadastrar serviço\033[0m")
        print("\033[1;32m2 - Deletar serviço\033[0m")
        print("\033[1;32m3 - Listar serviços\033[0m")
        print("\033[1;32m4 - Mostrar valor total\033[0m")
        print("\033[1;32m5 - Sair\033[0m")

    def register_service(self):
        self.clear_screen()
        print("\033[1;34m--- Serviços Disponíveis ---\033[0m")
        for idx, service in enumerate(self.available_services, start=1):
            print(f"\033[1;33m{idx} - {service['name']} : R$ {service['price']:.2f}\033[0m")
        try:
            choice = int(input("\nEscolha o número do serviço para cadastrar: "))
            if choice < 1 or choice > len(self.available_services):
                print("\033[1;31mOpção inválida. Escolha um número válido.\033[0m\n")
                time.sleep(2)
                return
            selected_service = self.available_services[choice - 1]
            self.services.append(selected_service)
            print(f"\033[1;32mServiço '{selected_service['name']}' cadastrado com sucesso!\033[0m\n")
            time.sleep(2)
        except ValueError:
            print("\033[1;31mEntrada inválida. Por favor, insira um número.\033[0m\n")
            time.sleep(2)

    def delete_service(self):
        self.clear_screen()
        if not self.services:
            print("\033[1;31mNenhum serviço cadastrado para remover.\033[0m\n")
            time.sleep(2)
            return
        print("\033[1;34m--- Serviços Cadastrados ---\033[0m")
        for idx, service in enumerate(self.services, start=1):
            print(f"\033[1;33m{idx} - {service['name']} : R$ {service['price']:.2f}\033[0m")
        try:
            choice = int(input("\nEscolha o número do serviço para remover: "))
            if choice < 1 or choice > len(self.services):
                print("\033[1;31mOpção inválida. Escolha um número válido.\033[0m\n")
                time.sleep(2)
                return
            removed_service = self.services.pop(choice - 1)
            print(f"\033[1;32mServiço '{removed_service['name']}' removido com sucesso!\033[0m\n")
            time.sleep(2)
        except ValueError:
            print("\033[1;31mEntrada inválida. Por favor, insira um número.\033[0m\n")
            time.sleep(2)

    def list_services(self):
        self.clear_screen()
        if not self.services:
            print("\033[1;31mNenhum serviço cadastrado.\033[0m\n")
            time.sleep(2)
            return
        print("\033[1;34m--- Serviços Cadastrados ---\033[0m")
        for service in self.services:
            print(f"\033[1;33m- {service['name']} : R$ {service['price']:.2f}\033[0m")
        input("\n\033[1;32mPressione Enter para continuar...\033[0m")

    def show_total_value(self):
        self.clear_screen()
        total = sum(service["price"] for service in self.services)
        print(f"\033[1;34mO valor total dos serviços: R$ {total:.2f}\033[0m")
        input("\n\033[1;32mPressione Enter para continuar...\033[0m")

    def exit_system(self):
        print("\033[1;32mSaindo do sistema. Até mais!\033[0m")
        time.sleep(2)
        exit()

    def run(self):
        while True:
            self.show_menu()
            option = input("\033[1;33mEscolha uma opção: \033[0m")
            if not option.isdigit() or int(option) not in self.menu_actions:
                print("\033[1;31mOpção inválida. Por favor, escolha uma opção entre 1 e 5.\033[0m\n")
                time.sleep(2)
                continue
            self.menu_actions[int(option)]()


if __name__ == "__main__":
    oficina = OficinaMecanica()
    oficina.run()