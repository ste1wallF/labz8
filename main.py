import mainey
#подключаем готовую схему чисел через созданный файл

em_num = int ( input ( 'Число сотруднников:  ' ) )
summ = 0
distance_list = []
price_list = []

for i in range( em_num ):
    distance = int( input( 'Расстояние до дома {0}-го сотрудника: '.format( i+1 ) ) )
    distance_list.append( distance )

for i in range( em_num ):
    price = int( input( 'Тариф {0}-го такси:  '.format( i+1 ) ) )
    price_list.append( price )

#Создаём копии списков
dis_list = distance_list[:] 
price_list = price_list[:]

#Так же создаем списки для хранения индексов наших значений
ind_list_a = []
ind_list_b = []

#В порядке возрастания и убывания значений переменных заполним списки индексами
max_dist = 0
for i in range( em_num ):                              
    index = dis_list.index( max( dis_list ) )
    ind_list_a.append( index )
    dis_list[ index ] = 0

for i in range( em_num ):
    index = price_list.index( min ( price_list ) )
    ind_list_b.append( index )
    price_list[ index ] = 10**10
    
#Поиск для каждого i-го в паре списков с индексами нужный индекс такси
print('Такси для клиента 1, 2, 3, ...:')

for i in range( em_num ):
    taxi_num = ind_list_b[ ind_list_a.index ( i ) ]
    print( taxi_num+1 )
for i in range( em_num ):
    summ += distance_list[ ind_list_a[ i ] ]*price_list[ ind_list_b[ i ] ]

#вывод итоговой суммы
print(summ)
print('Итоговая сумма:')
mainey.out(summ)