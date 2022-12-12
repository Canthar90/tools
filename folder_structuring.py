import datetime
import os


def one_day_more(date_to_increase):
    """Function increasing day by 1"""
    inceased_date = date_to_increase + datetime.timedelta(days=1)
    year = int(inceased_date.strftime("%Y"))
    month = int(inceased_date.strftime("%m"))
    day = int(inceased_date.strftime("%d"))
    print("info", year, month, day)
    return inceased_date, year, month, day


def new_year_dir(month, year, flag):
    """Function making another year direcory"""
    try:
        if not flag:
            os.chdir("../")
            os.chdir("../")
        os.mkdir(str(year))
        year_dir = year
        os.chdir(str(year))
        
        os.mkdir(str(month))
        month_dir = month
        os.chdir(str(month))
    except FileExistsError:
        os.chdir(str(year))
        year_dir = year
        try:
            os.mkdir(str(month))
            month_dir = month
            os.chdir(str(month))
        except:
            month_dir = month
            os.chdir(str(month))
    return year_dir, month_dir


def new_month_dir(month):
    """Creating new month dir inside year dir"""
    try:
        if month < 10:
            os.chdir("../")
            os.mkdir(f"0{month}")
            os.chdir(f"0{month}")
            month_dir = month
        else:
            os.chdir("../")
            os.mkdir(str(month))
            os.chdir(str(month))
            month_dir = month       
    except FileExistsError:
        month_dir = month
        if month < 10:
            os.chdir(f"0{month}")
        else:
            os.chdir(str(month))
    return month_dir


def new_day_dir(working_date, work_year, work_month, work_day):
    """Making new day directory"""
    if work_day < 10:
        try:
            os.mkdir(f"0{work_day}")
            working_date, work_year, work_month, work_day = one_day_more(working_date)
        except FileExistsError:
            working_date, work_year, work_month, work_day = one_day_more(working_date)
    else:
        try:
            os.mkdir(f"{work_day}")
            working_date, work_year, work_month, work_day = one_day_more(working_date)
        except FileExistsError:
            working_date, work_year, work_month, work_day = one_day_more(working_date)
    return working_date, work_year, work_month, work_day


current_date = datetime.date.today()
start_month = int(current_date.strftime("%m"))
start_day = int(current_date.strftime("%d"))
start_year = int(current_date.strftime("%Y"))

working_date = current_date
work_month = start_month
work_day = start_day
work_year = start_year

target_date = current_date + datetime.timedelta(days=365)
target_month = int(target_date.strftime("%m"))
target_day = int(target_date.strftime("%d"))
target_year = int(target_date.strftime("%Y"))


end_flag = False
first_step = False
while not end_flag:
    if working_date == target_date:
        end_flag = True
        break
    
    if working_date == current_date and not first_step:
        
        work_par_dir, work_dir = new_year_dir(work_month, work_year, True)
        first_step = True
    else:
        if work_par_dir == work_year:
            print(work_par_dir == work_year)
            if work_month == work_dir and work_par_dir == work_year:
                
                if working_date.strftime("%a") == "Sun" or working_date.strftime("%a") == "Sat":
                    print("Weekend")
                    working_date, work_year, work_month, work_day = one_day_more(working_date)
                    continue
                else:
                    working_date, work_year, work_month, work_day = new_day_dir(working_date, work_year, work_month, work_day)
                    continue
            else: 
                work_dir = new_month_dir(work_month)
                continue
                
        else:
            work_par_dir, work_dir = new_year_dir(work_month, work_year, False)
            continue


input("Done script executed all missing dates in structure filled. \nCreated folder structure if missing in timespawn \nPress any key to exit ")