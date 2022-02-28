import sys
import os

class color:
   PURPLE = '\033[95m'
   DARKCYAN = '\033[36m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'
   YELLOW = '\033[93m' 

def show_processes(an_array):
  print("\t\t\t \--PROCESOS--\ \t\t \n")
  print("Process ID\t| Process Size\t| Arrival Time\t| Irruption Time\n")
  for i in futures_processes:
    print(i.id_process," \t\t|",i.size_process ," \t\t|",i.TA , " \t\t|",i.TI , "\n")

def show_ready_processes():
  aux_band = 0 #para ver si los procesos en la cola de listos NO son el q esta en el cpu
  for j in ready_processes:
      if j == cpu.process_in_cpu and len(ready_processes) == 1:
        aux_band = 1
  print(color.BOLD,color.GREEN+"--Procesos en la cola de listos:\n" + color.END)
  if ((len(ready_processes)) != 0 and aux_band == 0):
    print("Process ID\t| Process Size\t| Arrival Time\t| Irruption Time\n")
    for j in ready_processes:
      if j != 0 and j != cpu.process_in_cpu:
        print(j.id_process," \t\t|",j.size_process ," \t\t|",j.TA , " \t\t|",j.TI_original,"\n")
  if aux_band == 1:
    print("No hay procesos en cola de listos")

def show_ended_processes():
  print(color.BOLD, color.RED+"--Procesos que ya terminaron:\n" + color.END)
  if len(ended_processes) == 0:
    print("Aun no terminaron procesos\n")
  else:
    print("Process ID\t| Process Size\t| Arrival Time\t| Irruption Time\n")
    for g in ended_processes:
      print(g.id_process," \t\t|",g.size_process ," \t\t|",g.TA , " \t\t|",g.TI ,"\n")

def show_RandS_processes():
  print(color.BOLD, color.YELLOW+" --Procesos en la cola de LyS:\n" + color.END)
  if len(ready_suspend_processes) == 0:
    print("Aun no hay procesos en cola de LyS\n")
  else:
    print("Process ID\t| Process Size\t| Arrival Time\t| Irruption Time\n")
    for g in ready_suspend_processes:
      print(g.id_process," \t\t|",g.size_process ," \t\t|",g.TA , " \t\t|",g.TI ,"\n")

def show_partitions(an_array):
  print("\n\--PARTITIONS--\ \t\t \n")
  print("PART ID\t\t| PART SIZE\t| PROCESS ID\t| INTERNAL FRAG\t| Start Address\n")
  print( "0"," \t\t|","100"," \t\t|","SO","\t\t|","--","\n")
  for i in partitions:
      if (i.proc_in_partition == 0):
        idprocess = '0'
      else:
        idprocess = i.proc_in_partition.id_process
      print(i.id_partition," \t\t|",i.size_partition ," \t\t|" , idprocess, " \t\t|", i.int_fragmentation, "\t\t|", i.start_address," \n")

def auditory():
  TRP = 0
  TEP = 0
  for g in array_auditory:
    TRPxProcess = g.a_LeftTime - g.a_TA
    TEPxProcess = TRPxProcess - g.a_TI
    TRP = TRP + TRPxProcess
    TEP = TEP + TEPxProcess
  TRP = round((TRP/cont_processes), 2)
  TEP = round((TEP/cont_processes), 2)
  print("\nTiempo de retorno promedio:",TRP)
  print("\nTiempo de espera promedio:",TEP,"\n")

class Auditory():
  def __init__(self, process_id, a_TA, a_TI, a_LeftTime):
      self.process_id = process_id
      self.a_TA = a_TA
      self.a_TI = a_TI
      self.a_LeftTime = a_LeftTime

class Partition_Class:
  def __init__(self, id_partition, size_partition, proc_in_partition, int_fragmentation, start_address):
      self.id_partition = id_partition
      self.size_partition = size_partition
      self.proc_in_partition = proc_in_partition
      self.int_fragmentation=int_fragmentation
      self.start_address=start_address

class Process_Class:
    def __init__(self, id_process, size_process, TA, TI, TI_original, TA_original, TI_ido):
      self.id_process = id_process
      self.size_process = size_process
      self.TA = TA
      self.TI = TI
      self.TI_original = TI_original
      self.TA_original = TA_original
      self.TI_ido = TI_ido

class Cpu_Class:
    def __init__(self, process_in_cpu, remaining_TI):
      self.process_in_cpu = process_in_cpu
      self.remaining_TI = remaining_TI

partitions=[Partition_Class(1,60,0,0,"0x110"), Partition_Class(2,120,0,0,"0x170"), Partition_Class(3,250,0,0,"0x290")]
cpu = Cpu_Class(0,sys.maxsize)
futures_processes = []
ended_processes = []
ready_processes = [] 
ready_suspend_processes = [] 
cont_processes = 0
array_auditory = []
id_process = 0
bandera_finaliza = 0
time = 0
band_size_detector = 1
band_hs = int(input("\nSi desea ingresar procesos ingrese 1, si desea usar un ejemplo pregrabado, ingrese 0: "))
if band_hs == 1:
    while band_size_detector != 0: 
        id_process = id_process + 1
        b = False
        print("\nIngrese valores de un proceso. Process size should be less than 250kb\n")
        while b==False:
            x = str(id_process)
            size_process=int(input( "Ingrese el size del proceso: " +x+": "))
            if size_process>250 or size_process<=0:
                print("\n ##### process size debe ser menor que 250k y mayor que 0kb...####\n")
                os.system("pause")    
            else:
                b=True
        x = str(id_process)
        a_better_text = ("\nIngrese TA del proceso "+x+": ")
        TA=int(input(a_better_text))
        TA_original = TA   
        a_better_text = ("\nIngrese TI del proceso "+x+": ") 
        TI=int(input(a_better_text))
        TI_original = TI
        TI_ido = 0
        new_proc= Process_Class(id_process, size_process, TA, TI, TI_original, TA_original, 0)
        futures_processes.append(new_proc)
        cont_processes=cont_processes+1
        if cont_processes < 10:
            band=int(input("\nDesea agregar otro proceso? 1 = Si, 0 = No: "))
            if band == 0: break
        else:
            print("\n No se pueden agregar mas de 10 procesos (restricciones TPI)\n")
            band=0
else:
  new_proc1= Process_Class(1, 30, 0, 2, 2, 0, 0)
  new_proc2= Process_Class(2, 30, 0, 5, 5, 0, 0)
  new_proc3= Process_Class(3, 30, 1, 8, 8, 1, 0)
  new_proc4= Process_Class(4, 30, 2, 4, 4, 2, 0)
  new_proc5= Process_Class(5, 30, 3, 2, 2, 3, 0)
  cont_processes=5
  futures_processes.append(new_proc1)
  futures_processes.append(new_proc2)
  futures_processes.append(new_proc3)
  futures_processes.append(new_proc4)
  futures_processes.append(new_proc5)
os.system("cls")
print("\n")
print("Estos son sus procesos, presione una tecla para comenzar la ejecucion\n\n")
show_processes(futures_processes)
os.system("pause") 
os.system("cls")
while((len(ended_processes) != cont_processes)):  #WHILE GENERAL
#--------------------- MEMORIA
    #el arreglo procesos arrivados siempre se pone a 0 para cargar los nuevos
    arrived_processes = []
    #cargamos en la cola de arrivados a los procesos que llegaron ahora
    for i in futures_processes:       
        if i.TA == time:
            arrived_processes.append(i)
            
    #borramos esos procesos del arreglo imaginario
    for x in arrived_processes:
        for j in futures_processes:
            if x == j:
                futures_processes.remove(j)

    #ordenamos el arreglo de arrivados y LyS por TI
    arrived_processes.sort(key=lambda p: p.TI)
    ready_suspend_processes.sort(key=lambda p: p.TI)
    #traemos a memoria principal los procesos en listo y suspendido 
    if len(ready_suspend_processes) != 0: 
        for j in ready_suspend_processes:    
            fragmin = sys.maxsize
            counter = 0
            position_in_partition = None
            for k in partitions:
                if(k.proc_in_partition == 0 and 0 <= (k.size_partition - j.size_process) < fragmin):
                    fragmin = k.size_partition - j.size_process
                    position_in_partition = counter
                counter += 1
            if position_in_partition != None:
                partitions[position_in_partition].proc_in_partition = j
                partitions[position_in_partition].int_fragmentation = fragmin
                ready_processes.append(j)
                ready_suspend_processes.remove(j)
                print("\nEl proceso",j.id_process,"se movio a la cola de Listos\n")
    #si no hay procesos en cola de lyS
    else:
        #la cpu esta ocupada? no
        if cpu.process_in_cpu == 0:
            #buscamos cual es la mejor particion para nuestros procesos nuevos (si hay o no)
            for ap in arrived_processes:
                fragmin = sys.maxsize
                counter = 0
                position_in_partition = None
                for k in partitions:
                    if(k.proc_in_partition == 0 and 0 <= (k.size_partition - ap.size_process) < fragmin):
                        fragmin = k.size_partition - ap.size_process
                        position_in_partition = counter
                    counter += 1
                    #lo cargamos en la mejor particion
                if position_in_partition != None:
                    partitions[position_in_partition].proc_in_partition = ap
                    partitions[position_in_partition].int_fragmentation = fragmin
                    #lo cargamos en el arreglo de listos y lo borramos de procesos recien arrivados
                    ready_processes.append(ap)
                    #no lo borro porque ya se borra solito dsp
                    
            #eliminamos de procesos recien arrivados a los que se asignaron a una particion
            for r in ready_processes:
                    for a in arrived_processes:
                        if r == a:
                            arrived_processes.remove(a)

            #arriba borramos al o a los procesos q se asignaron, y los que no, abajo los agregamos a LyS

            #y si quedaron procesos sin cargar? se van para LyS (y dsp se borran solos de arrived processes)
            if len(arrived_processes)!=0:
                for ap in arrived_processes:
                    print("\nEl proceso", ap.id_process,"se movio a la cola de LyS\n")
                    ready_suspend_processes.append(ap)

        #la cpu esta ocupada
        else:
            if len(arrived_processes) != 0:
                #vamos a ver si el proceso nuevo con menor Ti es menor que el que se esta ejecutando
                if arrived_processes[0].TI < cpu.remaining_TI:
                    #si lo es, vamos a ver si hay particiones libres
                    if len(ready_processes) < 2: #2 porque el q se esta ejecutando suma 1 mas (pero esta cargado en una particion)
                        #si hay, lo cargamos en algun lado con best fit y lo ponemos en la cpu sacando al otro
                        fragmin = sys.maxsize
                        counter = 0
                        position_in_partition = None
                        for k in partitions:
                            if(k.proc_in_partition == 0 and 0 <= (k.size_partition - arrived_processes[0].size_process) < fragmin):
                                fragmin = k.size_partition - arrived_processes[0].size_process
                                position_in_partition = counter
                            counter += 1
                            #lo cargamos en la mejor particion (ya sabemos que al menos, habia lugar en alguna particion)
                        if position_in_partition != None:
                            partitions[position_in_partition].proc_in_partition = arrived_processes[0]
                            partitions[position_in_partition].int_fragmentation = fragmin
                            print("\nEl proceso",arrived_processes[0].id_process,"quito al proceso",cpu.process_in_cpu.id_process,"por tener menor TI\n")
                            print("\nNO fue necesario mover al proceso en ejecucion a la cola de LyS\n") #porque no habian procesos en LyS
                            #resguardamos los valores del proceso viejo
                            cpu.process_in_cpu.TI = cpu.remaining_TI   
                            #lo volvemos a agregar a cola de listos
                            ready_processes.append(cpu.process_in_cpu)
                            #cargamos el nuevo proceso
                            cpu.process_in_cpu = arrived_processes[0]
                            cpu.remaining_TI = arrived_processes[0].TI 
                            #borramos el proceso nuevo de procesos recien arrivados
                            arrived_processes.remove(arrived_processes[0])
                            
                        #y ahora cargamos los otros nuevitos en algunas particiones (si hay)
                        fragmin = sys.maxsize
                        counter = 0
                        position_in_partition = None
                        for ap in arrived_processes:
                            for k in partitions:
                                if(k.proc_in_partition == 0 and 0 <= (k.size_partition - ap.size_process) < fragmin):
                                    fragmin = k.size_partition - ap.size_process
                                    position_in_partition = counter
                                counter += 1
                        if position_in_partition != None:
                            #lo cargamos en la mejor particion (ya sabemos que al menos, habia lugar en alguna particion)
                            partitions[position_in_partition].proc_in_partition = ap
                            partitions[position_in_partition].int_fragmentation = fragmin
                            ready_processes.append(ap)
                        else:
                            if len(arrived_processes)!=0:
                                for ap in arrived_processes:
                                    print("\nEl proceso", ap.id_process,"se movio a la cola de LyS\n")
                                    ready_suspend_processes.append(ap)

                    else:
                        #si no hay lugar, nos fijamos si entra en la particion del proceso que se esta ejecutando
                        #buscamos la particion del proceso que se esta ejecutando
                        counter = 0
                        position_cpu_partition = None
                        for k in partitions:
                            if(k.proc_in_partition == cpu.process_in_cpu):
                                position_cpu_partition = counter
                            counter += 1
                        #aca verificamos si el proceso nuevo ENTRA en la particion del que se estaba ejecutando
                        if partitions[position_cpu_partition].size_partition >= arrived_processes[0].size_process:
                            print("\nEl proceso",arrived_processes[0].id_process,"quito al proceso",cpu.process_in_cpu.id_process,"por tener menor TI\n")
                            print("\nFue necesario mover al proceso en ejecucion a la cola de LyS\n")
                            #resguardamos los valores del proceso viejo
                            cpu.process_in_cpu.TI = cpu.remaining_TI 
                            #lo mandamos a la cola de listos y suspendidos
                            ready_suspend_processes.append(cpu.process_in_cpu)
                            print("\nEl proceso", cpu.process_in_cpu.id_process,"se movio a la cola de LyS\n")
                            #cargamos en la particion del proceso viejo el nuevo proceso
                            partitions[position_cpu_partition].proc_in_partition = arrived_processes[0]
                            partitions[position_cpu_partition].int_fragmentation = partitions[position_cpu_partition].size_partition - arrived_processes[0].size_process
                            #sacamos de la cpu al proceso viejo poniendo al nuevo
                            cpu.process_in_cpu = arrived_processes[0]
                            cpu.remaining_TI = arrived_processes[0].TI 

                            #borramos el proceso nuevo de procesos recien arrivados
                            arrived_processes.remove(arrived_processes[0])
                            #y mandamos todos los otros nuevos a LyS
                            if len(arrived_processes)!=0:
                                for ap in arrived_processes:
                                    print("\nEl proceso", ap.id_process,"se movio a la cola de LyS\n")
                                    ready_suspend_processes.append(ap)
                        else:
                            #si no entra en la particion del proceso q se estaba ejecutando
                            #sacamos a algun otro y lo ponemos ahi
                            fragmin = sys.maxsize
                            counter = 0
                            position_in_partition = None
                            for k in partitions:
                                if(k.proc_in_partition != 0 and 0 <= (k.size_partition - arrived_processes[0].size_process) < fragmin):
                                    fragmin = k.size_partition - arrived_processes[0].size_process
                                    position_in_partition = counter
                                counter += 1
                                #ahora tenemos que resguardar el proceso que estaba en esa particion y mandarlo a LyS
                            if position_in_partition != None:
                                #mandamos el TI> a LyS
                                ready_suspend_processes.append(partitions[position_in_partition].proc_in_partition)
                                print("\nEl proceso",arrived_processes[0].id_process,"quito al proceso",cpu.process_in_cpu.id_process,"por tener menor TI\n")
                                print("\nFue necesario mover al proceso",partitions[position_in_partition].proc_in_partition.id_process,"de la cola de listos a la cola de LyS\n")
                                ready_processes.remove(partitions[position_in_partition].proc_in_partition)
                                #ponemos ahi el nuevo proceso
                                partitions[position_in_partition].proc_in_partition = arrived_processes[0]
                                partitions[position_in_partition].int_fragmentation = fragmin
                                #resguardamos los valores del proceso viejo
                                cpu.process_in_cpu.TI = cpu.remaining_TI 
                                #lo mandamos a la cola de listos
                                ready_processes.append(cpu.process_in_cpu)
                                #sacamos de la cpu al proceso viejo poniendo al nuevo
                                cpu.process_in_cpu = arrived_processes[0]
                                cpu.remaining_TI = arrived_processes[0].TI 
                                #borramos el proceso nuevo de procesos recien arrivados
                                arrived_processes.remove(arrived_processes[0])
                                #y mandamos todos los otros nuevos a LyS
                                if len(arrived_processes)!=0:
                                    for ap in arrived_processes:
                                        print("\nEl proceso", ap.id_process,"se movio a la cola de LyS\n")
                                        ready_suspend_processes.append(ap)
                else:
                    #si el proceso mas chico de los nuevos no tenia menor TI que el que se estaba ejecutando, simplemente
                    #metemos en memoria los que podamos por best fit, y los otros a LyS
                    fragmin = sys.maxsize
                    counter = 0
                    position_in_partition = None
                    for ap in arrived_processes:
                        for k in partitions:
                            if(k.proc_in_partition == 0 and 0 <= (k.size_partition - ap.size_process) < fragmin):
                                fragmin = k.size_partition - ap.size_process
                                position_in_partition = counter
                            counter += 1
                    if position_in_partition != None:
                        #lo cargamos en la mejor particion (ya sabemos que al menos, habia lugar en alguna particion)
                        partitions[position_in_partition].proc_in_partition = ap
                        partitions[position_in_partition].int_fragmentation = fragmin
                        ready_processes.append(ap)
                    #ahora borramos de arrived los que son ready
                    for r in ready_processes:
                        for a in arrived_processes:
                            if r == a:
                                arrived_processes.remove(a)
                    #y ahora mandamos los arrivados a listo y suspendido que quedaron
                    if len(arrived_processes)!=0:
                        for ap in arrived_processes:
                            print("\nEl proceso", ap.id_process,"se movio a la cola de LyS\n")
                            ready_suspend_processes.append(ap)

                    #Aca revisamos si el proceso ya no estaba cargado anteriormente en auditoria
                    a_band = 0
                    for g in array_auditory:
                        if g.process_id == cpu.process_in_cpu.id_process:
                            a_band = 1
                    #si no lo esta, actualizamos la auditoria con los datos del nuevo proceso
                    if a_band != 1:
                        new_auditory = Auditory(cpu.process_in_cpu.id_process, cpu.process_in_cpu.TA_original, cpu.process_in_cpu.TI_original, 0)
                        array_auditory.append(new_auditory)
        
#--------------------- CPU 

    print(color.BOLD, color.DARKCYAN+'\n #### CPU TIME = ',time,' ####\n'+ color.END)
    position_in_partition = None
    aux = 0
    minTI = sys.maxsize
    if cpu.process_in_cpu !=0 :
        #Verificamos si hay procesos con menor TI que el que se esta ejecutando
        counter = 0
        for p in partitions:
            if(p.proc_in_partition != 0 and p.proc_in_partition.TI < cpu.remaining_TI):      
                position_in_partition = counter
            counter += 1 

        if position_in_partition != None:
            #preguntamos si hay procesos en la cola de listo y suspendido
            if len(ready_suspend_processes) != 0:
                #resguardamos el proceso que se estaba ejecutando
                cpu.process_in_cpu.TI = cpu.remaining_TI 
                #lo mandamos a la cola de listos y suspendidos
                print("\nEl proceso", cpu.process_in_cpu.id_process,"se movio a la cola de LyS\n")
                ready_suspend_processes.append(cpu.process_in_cpu)
                #limpiamos su particion
                #buscar cual era la particion del proceso q se estaba ejecutando
                counter = 0
                position_cpu_partition = None
                for k in partitions:
                    if(k.proc_in_partition == cpu.process_in_cpu):
                        position_cpu_partition = counter
                    counter += 1
                partitions[position_cpu_partition].proc_in_partition = 0
                partitions[position_cpu_partition].int_fragmentation = 0
                #sacamos de los registros del procesador al proceso viejo poniendo al nuevo
                cpu.process_in_cpu = partitions[position_in_partition].proc_in_partition
                cpu.remaining_TI = partitions[position_in_partition].proc_in_partition.TI 
                #borramos el proceso nuevo de procesos listos
                ready_processes.remove(partitions[position_in_partition].proc_in_partition)
                #Aca revisamos si el proceso ya no estaba cargado anteriormente en auditoria
                a_band = 0
                for g in array_auditory:
                    if g.process_id == cpu.process_in_cpu.id_process:
                        a_band = 1
                #si no lo esta, actualizamos la auditoria con los datos del nuevo proceso
                if a_band != 1:
                    new_auditory = Auditory(cpu.process_in_cpu.id_process, cpu.process_in_cpu.TA_original, cpu.process_in_cpu.TI_original, 0)
                    array_auditory.append(new_auditory)
            else:
                #si no hay procesos en la cola de listos y suspendidos, simplemente dejamos al proceso que se estaba....
                #...ejecutando en la cola de listos con sus datos resguardados
                #resguardamos el proceso que se estaba ejecutando
                cpu.process_in_cpu.TI = cpu.remaining_TI 
                #lo mandamos a la cola de listos
                ready_processes.append(cpu.process_in_cpu)
                #sacamos de los registros de la cpu al proceso viejo poniendo al nuevo
                cpu.process_in_cpu = partitions[position_in_partition].proc_in_partition
                cpu.remaining_TI = partitions[position_in_partition].proc_in_partition.TI  
                #borramos el proceso nuevo de procesos listos
                ready_processes.remove(partitions[position_in_partition].proc_in_partition)
                #Aca revisamos si el proceso ya no estaba cargado anteriormente en auditoria
                a_band = 0
                for g in array_auditory:
                    if g.process_id == cpu.process_in_cpu.id_process:
                        a_band = 1
                #si no lo esta, actualizamos la auditoria con los datos del nuevo proceso
                if a_band != 1:
                    new_auditory = Auditory(cpu.process_in_cpu.id_process, cpu.process_in_cpu.TA_original, cpu.process_in_cpu.TI_original, 0)
                    array_auditory.append(new_auditory)
    else:
        #en memoria anteriormente habiamos cargado en las particiones los procesos recien arrivados
        #pero es recien en esta parte donde la cpu busca quien de todos esos es el que tiene que ejecutarse
        #en este punto no hay procesos nuevos (arrivados) (porque ya se cargaron anteriormente y los q sobran a LyS)
        #Verificamos cual es el proceso con menor TI de los procesos en listo (no hay procesos en la cpu)
        counter = 0
        for p in partitions:
            if(p.proc_in_partition != 0 and p.proc_in_partition.TI < minTI):      
                position_in_partition = counter
                minTI = p.proc_in_partition.TI
            counter += 1 
        #cargamos el proceso con menor TI a la cpu
        if position_in_partition != None:
            cpu.process_in_cpu = partitions[position_in_partition].proc_in_partition
            cpu.remaining_TI = partitions[position_in_partition].proc_in_partition.TI 
            #borramos el cargado de la cola de listos
            ready_processes.remove(partitions[position_in_partition].proc_in_partition)

            #Aca revisamos si el proceso ya no estaba cargado anteriormente en auditoria
            a_band = 0
            for g in array_auditory:
                if g.process_id == cpu.process_in_cpu.id_process:
                    a_band = 1
            #si no lo esta, actualizamos la auditoria con los datos del nuevo proceso
            if a_band != 1:
                new_auditory = Auditory(cpu.process_in_cpu.id_process, cpu.process_in_cpu.TA_original, cpu.process_in_cpu.TI_original, 0)
                array_auditory.append(new_auditory)

    band_time = 0
    #termina un proceso
    if(cpu.remaining_TI == 0): 
        for a in array_auditory:
            if cpu.process_in_cpu.id_process == a.process_id:
                a.a_LeftTime = time
        #lo guardamos en el arreglo de procesos terminados
        ended_processes.append(cpu.process_in_cpu)
        print('-----------------------')
        print('El proceso ', cpu.process_in_cpu.id_process, ' se ejecuto una ultima vez y termino.\n')
        print('Termino con ', cpu.remaining_TI, ' unidades de tiempo.')
        print('\nSu TI original era ', cpu.process_in_cpu.TI_original, ' unidades de tiempo.')
        print('-----------------------\n')
        show_RandS_processes()
        show_ready_processes()
        show_ended_processes()
        print(color.BOLD, color.PURPLE+'\n #### MEMORY TIME = ',time, " ####" + color.END) 
        #lo quito de la particion
        for j in partitions:
            if j.proc_in_partition != 0 and j.proc_in_partition.id_process == cpu.process_in_cpu.id_process:
                j.proc_in_partition = 0            
                j.int_fragmentation = 0
        show_partitions(partitions)
        #lo sacamos de la cpu
        cpu.process_in_cpu = 0
        cpu.remaining_TI = sys.maxsize
        band_time = 1

    if(cpu.process_in_cpu != 0):
        print('-----------------------')
        print('El proceso ', cpu.process_in_cpu.id_process, ' se esta ejecutando\n')
        print('Le quedan ', cpu.remaining_TI, ' unidades de tiempo.')
        print('\nSu TI original es ', cpu.process_in_cpu.TI_original, ' unidades de tiempo.')
        print('-----------------------\n')
        show_RandS_processes()
        show_ready_processes()
        show_ended_processes()
        cpu.remaining_TI -= 1
        print(color.BOLD, color.PURPLE+' #### MEMORY TIME = ',time, " ####" + color.END)
        show_partitions(partitions)   
    os.system("pause")  
    os.system("cls") 
    if band_time == 0: #si un proceso termino, otro entra al mismo tiempo, por eso este if
        time += 1
#Mostrar auditoria
os.system("cls") 
print("/////////////////////////////")
print('\nTERMINARON TODOS LOS PROCESOS!\n')
print("\nTiempo de CPU requerido:",time,"\n")
print("\n/////////////////////////////\n")

show_ended_processes()
print(color.BOLD,color.GREEN+"--Tabla de particiones vacias\n" + color.END)
show_partitions(partitions)
print("/////////////////////////////")
print('\nAUDITORIA:\n')
auditory()