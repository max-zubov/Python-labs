#!/usr/bin/env python
# -*- coding: utf-8 -*-
from final_task import Matrix
import json


class matrixfile:

    def __init__(self, filename):
        self.filename=filename

    def __getcontent(self):
        with open(self.filename, "r") as f:
            content=f.read()
            return content   

    def write(self, mname, matr):
        content = self.__getcontent()
        with open(self.filename, "w") as f:
            de = json.JSONDecoder().decode(content) if content else {}
            de[mname] = matr
            en = json.JSONEncoder().encode(de)
            f.write(en)

    def read(self):
        return json.loads(self.__getcontent())    

    def delete(self, mname):
        content = self.__getcontent()
        with open(self.filename, "w") as f:
            de = json.JSONDecoder().decode(content) if content else {}
            try:
                del(de[mname])
            except:
                pass
            en = json.JSONEncoder().encode(de)
            f.write(en)

            
if __name__ == '__main__':
    
    mfile=matrixfile("matrs")
    mm=[]
    inchar=' '
    #пока не нажата q
    while inchar != 'q':
        #если количество матриц в списке меньше 2-х
        if len(mm)<2: 
            inchar=input('Введите {}-ю матрицу с консоли или выберите из имеющихся в файле.\n'.format(len(mm)+1) + \
                   ' для ввода с консоли нажмите 1 \n' + \
                   ' для выбора или удаления из файла нажмите 2 \n' + \
                   ' для выхода нажмите q \n')
            if inchar=='1':
                inchar=input('Вид ввода матрицы.\n' + \
                             ' двумерный список: 1\n' + \
                             ' рандомный список: 2\n' + \
                             ' отмена: любая клавиша.\n')
                if inchar=='1':
                    line = input('Введите массив в виде: [[1,2],[3,4]]\n')
                    try:
                        L=Matrix(json.loads(line))
                        mm.append(L.matr)
                    except:
                        pass
                elif inchar=='2':
                    try:
                        row=int(input('Введите количество строк:'))
                        col=int(input('Введите количество столбцов:'))
                        R=Matrix([],row,col)
                        mm.append(R.matr)
                    except:
                        pass
            elif inchar=='2':
                all=mfile.read()    
                for m in all:
                    print('{}: {}'.format(m,all[m]))
                inm=input('Введите имя выбранной матрицы.\n')
                inchar=input('Выберите действие над матрицей из файла.\n' + \
                             ' выбрать: s\n' + \
                             ' удалить: d\n' + \
                             ' отмена: любая клавиша.\n')
                if inchar == 's':
                    mm.append(all[inm])
                elif inchar == 'd':
                    mfile.delete(inm)
                   
        elif len(mm)==2: #матриц две, печатаем матрицы, их характеристики и действиe над ними
            M1=Matrix(mm[0])
            M2=Matrix(mm[1])
            print('Введены две матрицы:\n')
            print(str(M1))
            print(str(M2))
            inchar=input('Выберите действие над матрицами.\n' + \
                         ' сложение: +\n' + \
                         ' вычитание: -\n' + \
                         ' умножение: *\n' + \
                         ' отмена: любая клавиша.\n')
            mm=[]             
            try:
                if inchar == '+':
                    M3=M1+M2
                    mm.append(M3.matr)
                elif inchar == '-':
                    M3=M1-M2
                    mm.append(M3.matr)
                elif inchar == '*':
                    M3=M1*M2
                    mm.append(M3.matr)
            except:
                pass
                
        # уже есть одна матрица
        while len(mm)==1: 
        # матрицу можно проанализировать или сохранить
            print('Введена матрица:\n')
            M1=Matrix(mm[0])
            M1.draw()
            inchar=input('Выберите действие над матрицей:.\n' + \
                         ' анализ матрицы: 1\n' + \
                         ' транспонирование матрицы: 2\n' + \
                         ' ввод сдедующей матрицы: 3\n' + \
                         ' сохранение матрицы в файл: 4\n' + \
                         ' отмена: любая клавиша.\n')
            if inchar=='1':
                print('единичная -',M1.is_identity())
                print('квадратная -', M1.is_square())
                print('нулевая -', M1.is_zero())
                print('диагональная -',M1.is_diagonal())
            elif inchar=='2':
                try:
                    M1.transpose()
                    print('Транспонированная матрица:')
                    M1.draw()
                    del mm[0]
                    mm.append(M1.matr)
                except:
                    pass
            elif inchar=='3':
                break
            elif inchar=='4':
                all=mfile.read()    
                for m in all:
                    print('{}: {}'.format(m,all[m]))
                inm=input('Введите имя под которым сохранить матрицу.\n')
                mfile.write(inm, M1.matr)
            else:
                mm=[]            
