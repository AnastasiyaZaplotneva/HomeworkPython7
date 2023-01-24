import model
import view

def work_process():
    choose = int(input('Если вы хотите добавить информацию в справочник, введите 1. Если получить информацию из справочника - 0: '))
    if choose:
        cont = view.add_contact()
        model.overwriting_data(cont)
    elif choose == 0:
        model.user_output_data()
    else:
        print('Вы ввели неверное значение')