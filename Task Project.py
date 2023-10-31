task_names =[]
task_statuses =[]
task_durations =[]
for i in range (200):
    answer = input ("add, display, remove, edit, search, mark, details, help, exit: ")
    if answer == "add":
        task = input ("add a task:")
        if task not in task_names:
            task_names.append(task)
            task_statuses.append(False)
            task_durations.append(None)
            print("added")
        else:
            print (f"{task}: alread exists!")
    elif answer == "display":
        if len(task_names) == 0:
            print ("Empty!")
        for (i, t) in enumerate(task_names):
            status = task_statuses[i]
            duration = task_durations[i]
            if duration:
                print (f"{i+1}) {t} ==> status: {status}, duration: {duration}")
            else:
                print (f"{i+1}) {t} ==> status: {status}")
    elif answer == "remove":
        task = input ("task name:")
        if task in task_names:
            ind = task_names.index (task)
            task_names.pop(ind)
            task_durations.pop(ind)
            task_statuses.pop(ind)
            print ("removed!")
        else:
            print(f"{task}: not found!")
    elif answer == "edit":
        old_task = input ("task name:")
        if old_task in task_names:
            ind = task_names.index (old_task)
            new_task = input ("new name of task:")
            if new_task not in task_names:
                task_names[ind] = new_task
            else:
                print(f"{new_task}: already exist!")
        else:
            print(f"{old_task}: not found!")
    elif answer == "search":
        task = input ("task name: ")
        if task in task_names:
            ind = task_names.index(task)
            duration = task_durations[ind]
            status = task_statuses[ind]
            print (f"{task} ==> status: {status} , duration: {duration}")
        else:
            print(f"{task}: not found!")
    elif answer == "mark":
        task = input ("task name:")
        if task in task_names:
            ind = task_names.index(task)
            start_time = input ("start time of task on this format (HH) :")
            end_time = input ("end time of task on this format (HH) :")
            h_start= start_time.isdigit()
            h_end = end_time.isdigit()
            if h_start and h_end:
                s_time =int (start_time)
                e_time = int(end_time)
                if s_time < e_time and 00 <= s_time <= 23 and 00 < e_time <= 24:
                    task_statuses[ind] = True
                    h_time = (e_time - s_time)
                    task_durations[ind] = h_time
                    print ("marked")
                else:
                    print ("time error!") 
            else:
                    print ("time format error!")
        else:
            print (f"{task}: not found!")
    elif answer == "details":
        total = len (task_names)
        donot = task_statuses.count(False)
        did = task_statuses.count(True)
        print (f"total: {total}")
        print (f"not mark : {donot}")
        print (f"marked: {did}")
        time = []
        for i in task_durations:
            if i:
                time.append(i)
        print (f"duration times: {sum(time)}")
    elif answer == "help":
        help_txt = """
        Tasks:
        -	add: Adds a new task.
        -	remove: Removes a specified task.
        -	edit: Edits a task.
        -	search: Searches for a task.
        -	display: Displays all tasks.
        -	mark: mark a task.
        -	details: displays details of each task
        -	help: Displays this help text.
        -	exit: Exits the program.
      """
        print (help_txt)
    elif answer == "exit":
        break
    elif answer == "":
        continue
    else:
        print (f"{answer} command not found!")