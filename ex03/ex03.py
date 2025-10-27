import os
from datetime import datetime

def smart_log(*args, **kwargs) -> None:
    
    level = kwargs.get("level") 
    use_timestamp = kwargs.get("timestamp", False)
    file_path = kwargs.get("save_to_file")
    use_color = kwargs.get("colored_output", kwargs.get("color_output", False))

    COLORS = {
        "info": "\033[94m",
        "debug": "\033[90m",
        "warning": "\033[93m",
        "error": "\033[91m",
        "ENDC": "\033[0m"
    }

    base_message = " ".join(str(arg) for arg in args)

    log_parts = []
    
    if use_timestamp:
        time_str = datetime.now().strftime("%H:%M:%S")
        log_parts.append(time_str)
        
    if level:
        level_str = "[{}]".format(level.upper())
        log_parts.append(level_str)
        
    log_parts.append(base_message)
    
    plain_log_line = " ".join(log_parts)

    if file_path:
            
            dir_name = os.path.dirname(file_path)
            if dir_name: 
                os.makedirs(dir_name, exist_ok=True) 

            with open(file_path, "a", encoding="utf-8") as f:
                f.write(plain_log_line + "\n")
        
    console_line = plain_log_line
    
    if use_color and level:
        color_code = COLORS.get(level.lower())
        if color_code:
            console_line = color_code + plain_log_line + COLORS['ENDC']
            
    print(console_line)

if __name__ == "__main__":
    smart_log("This is an info message.", level="info", timestamp=True, colored_output=True)
    smart_log("This is a debug message.", level="debug", timestamp=True, colored_output=True)
    smart_log("This is a warning message.", level="warning", timestamp=True, colored_output=True)
    smart_log("This is an error message.", level="error", timestamp=True, colored_output=True)