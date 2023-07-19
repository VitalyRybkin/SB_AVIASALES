from view.run_service import RunService


def main():

    cmds = {
        'add': ' - ввод рейса',
        'output': ' - вывод всех рейсов',
        'search': ' - поиск рейса по номеру',
        'exit': ' - завершение работы'
    }

    run_service = RunService(cmds)
    run_service.run_service()


if __name__ == '__main__':
    main()
