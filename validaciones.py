import re
from datetime import date

class Validacion:
    def is_int(variable):
        try:
            int(variable)
            return True
        except:
            return False
    
    def is_float(variable):
        try:
            float(variable)
            return True
        except:
            return False
    
    def is_string(variable):
        if isinstance(variable, str):
           return True
        else:
           return False
    
    def is_alphanumeric(variable,limite):
        try:
            patron = r"^[\w\s]{,"+str(limite)+"}$"
            resultado = re.findall(patron,variable)
            if resultado == []:
                return False
            else:
                return True
        except:
            return False
    
    def is_alphabetical(variable,limite):
        try:
            patron = r"^[a-zA-Z\s'á-úä-ü]{1,"+str(limite)+"}$"
            resultado = re.findall(patron,variable)
            if resultado == []:
                return False
            else:
                return True
        except:
            return False
    
    def is_email(variable):
        try:
            patron = r"^[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            resultado =re.findall(patron, variable)
            if resultado == []:
                return False
            else:
                return True
        except:
            return False
        
    def is_date(variable):
        try:
            patrones = [r"^[\d]{2}-[\d]{2}-[\d]{4}$",r"^[\d]{4}-[\d]{2}-[\d]{2}$"]
            for patron in patrones:
                resultado =re.findall(patron, variable)
                if resultado == []:
                    continue
                else:
                    return True
            return False
        except:
            return False
    
    def date_not_today(format,date_):
        today = date.today()
        today = today.strftime(format)
        if date_ == today:
            return False
        else:
            return True
            
    def is_in_combobox(variable,list_):
        for i in list_:
            if i == variable:
                return True
        return False
    
    def is_in_combobox_exept_0(variable,list_):
        if list_[0] == variable:
            return False
        for i in list_:
            if i == variable:
                return True
        return False
    
    def is_all_validated(validation):
        for val in validation:
            if val:
                continue
            else:
                return False       
        return True 

